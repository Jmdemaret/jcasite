#!/usr/bin/env python3
"""
Récupère les avis Google du Judo Club Anderlecht via SerpAPI et écrit
google-reviews.json.

La période de conservation est lue depuis content.json
(clé `googleReviewsPeriodMonths`). Valeur par défaut : 12 mois.
Valeur 0 = tous les avis (pas de filtre).

Pagination : on boucle sur plusieurs pages de SerpAPI pour récupérer
plus que les ~8 avis de la première page. Max 5 pages (≈ 40 avis).

Secrets GitHub requis :
  SERPAPI_KEY       — clé API SerpAPI
  GOOGLE_PLACE_ID   — Place ID Google Maps (ChIJ…)
"""
import json
import os
import sys
import time
import urllib.parse
import urllib.request

SERPAPI_KEY = os.environ.get("SERPAPI_KEY", "").strip()
PLACE_ID    = os.environ.get("GOOGLE_PLACE_ID", "").strip()
OUT_FILE    = "google-reviews.json"
MAX_PAGES   = 5   # max 5 pages = ~40 avis récupérés

def write_empty(reason):
    with open(OUT_FILE, "w", encoding="utf-8") as f:
        json.dump({"reviews": [], "fetched_at": int(time.time()), "error": reason},
                  f, ensure_ascii=False, indent=2)

if not SERPAPI_KEY or not PLACE_ID:
    missing = []
    if not SERPAPI_KEY: missing.append("SERPAPI_KEY")
    if not PLACE_ID:    missing.append("GOOGLE_PLACE_ID")
    print("❌ Secret(s) manquant(s) : " + ", ".join(missing))
    write_empty("missing secrets: " + ", ".join(missing))
    sys.exit(1)

# Lire la période depuis content.json (défaut : 12 mois)
period_months = 12
try:
    with open("content.json", "r", encoding="utf-8") as f:
        cfg = json.load(f)
    period_months = int(cfg.get("googleReviewsPeriodMonths", 12))
except Exception as e:
    print(f"(content.json non lu, défaut 12 mois — {e})")

cutoff_seconds = period_months * 30 * 24 * 3600 if period_months > 0 else 0
cutoff_ts = time.time() - cutoff_seconds if cutoff_seconds else 0
print(f"Période de conservation : {'tous les avis' if period_months==0 else str(period_months)+' mois'}")

def fetch_page(params):
    url = "https://serpapi.com/search.json?" + urllib.parse.urlencode(params)
    with urllib.request.urlopen(url, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))

# Page 1
base_params = {
    "engine":   "google_maps_reviews",
    "place_id": PLACE_ID,
    "hl":       "fr",
    "sort_by":  "newestFirst",
    "api_key":  SERPAPI_KEY,
}
print(f"Fetching page 1 for place_id={PLACE_ID[:15]}…")
try:
    data = fetch_page(base_params)
except Exception as e:
    print(f"SerpAPI error page 1: {e}")
    write_empty(f"serpapi page 1 failed: {e}")
    sys.exit(1)

if data.get("error"):
    print(f"SerpAPI returned error: {data['error']}")
    write_empty(f"serpapi error: {data['error']}")
    sys.exit(1)

place_info = data.get("place_info") or {}
all_raw = list(data.get("reviews") or [])

# Pagination : on récupère next_page_token tant qu'il existe et qu'on n'a pas dépassé MAX_PAGES
next_token = (data.get("serpapi_pagination") or {}).get("next_page_token")
page = 1
while next_token and page < MAX_PAGES:
    page += 1
    print(f"Fetching page {page}…")
    try:
        params = dict(base_params)
        params["next_page_token"] = next_token
        time.sleep(1)   # courtoisie SerpAPI
        d = fetch_page(params)
    except Exception as e:
        print(f"SerpAPI error page {page}: {e}")
        break
    if d.get("error"):
        print(f"SerpAPI returned error on page {page}: {d['error']}")
        break
    all_raw.extend(d.get("reviews") or [])
    next_token = (d.get("serpapi_pagination") or {}).get("next_page_token")

# Filtrage par période
reviews = []
for r in all_raw:
    iso = r.get("iso_date") or ""
    ts = 0
    if iso:
        try:
            ts = int(time.mktime(time.strptime(iso[:19], "%Y-%m-%dT%H:%M:%S")))
        except Exception:
            ts = 0
    if cutoff_ts and ts and ts < cutoff_ts:
        continue
    user = r.get("user") or {}
    reviews.append({
        "author":   user.get("name", ""),
        "rating":   r.get("rating", 0),
        "text":     (r.get("snippet") or "").strip(),
        "time":     ts,
        "relative": r.get("date", ""),
        "profile_photo": user.get("thumbnail", ""),
        "language": r.get("language", "fr"),
    })

out = {
    "place_name":         place_info.get("title", "") or "Judo Club Anderlecht",
    "place_url":          f"https://www.google.com/maps/place/?q=place_id:{PLACE_ID}",
    "rating":             place_info.get("rating", 0),
    "total":              place_info.get("reviews", 0),
    "reviews":            reviews,
    "period_months":      period_months,
    "pages_fetched":      page,
    "returned_by_serpapi": len(all_raw),
    "kept_recent":        len(reviews),
    "cutoff_iso":         (time.strftime("%Y-%m-%d", time.gmtime(cutoff_ts)) if cutoff_ts else "aucun"),
    "fetched_at":         int(time.time()),
    "source":             "serpapi",
}

with open(OUT_FILE, "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print(f"✓ Wrote {OUT_FILE}: {len(reviews)} review(s) kept out of {len(all_raw)} returned "
      f"({page} page(s)). Place rating: {place_info.get('rating', '?')} ({place_info.get('reviews', '?')} avis total)")
