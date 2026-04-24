#!/usr/bin/env python3
"""
Récupère les avis Google du Judo Club Anderlecht via SerpAPI et écrit
google-reviews.json. Filtre les 6 derniers mois.

Pourquoi SerpAPI et pas Google Cloud Places API ?
- Inscription en 2 min (email + mot de passe, pas de carte bancaire)
- 100 requêtes/mois gratuites = largement suffisant (1/semaine = 4/mois)
- Pas de Cloud Console à naviguer

Secrets GitHub requis :
  SERPAPI_KEY       — clé API SerpAPI (https://serpapi.com)
  GOOGLE_PLACE_ID   — Place ID de la fiche Google (ChIJ…)
                      Trouvable via https://developers.google.com/maps/documentation/places/web-service/place-id
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
SIX_MONTHS  = 180 * 24 * 3600

def write_empty(reason):
    with open(OUT_FILE, "w", encoding="utf-8") as f:
        json.dump({"reviews": [], "fetched_at": int(time.time()), "error": reason},
                  f, ensure_ascii=False, indent=2)

if not SERPAPI_KEY or not PLACE_ID:
    print(f"Missing secrets (SERPAPI_KEY={'yes' if SERPAPI_KEY else 'NO'}, "
          f"GOOGLE_PLACE_ID={'yes' if PLACE_ID else 'NO'})")
    write_empty("missing secrets")
    sys.exit(0)

params = {
    "engine":   "google_maps_reviews",
    "place_id": PLACE_ID,
    "hl":       "fr",
    "sort_by":  "newestFirst",
    "api_key":  SERPAPI_KEY,
}
url = "https://serpapi.com/search.json?" + urllib.parse.urlencode(params)
print(f"Calling SerpAPI for place_id={PLACE_ID[:15]}…")

try:
    with urllib.request.urlopen(url, timeout=30) as resp:
        data = json.loads(resp.read().decode("utf-8"))
except Exception as e:
    print(f"SerpAPI error: {e}")
    write_empty(f"serpapi request failed: {e}")
    sys.exit(0)

if data.get("error"):
    print(f"SerpAPI returned error: {data['error']}")
    write_empty(f"serpapi error: {data['error']}")
    sys.exit(0)

place_info = data.get("place_info") or {}
all_reviews = data.get("reviews") or []
cutoff = time.time() - SIX_MONTHS

reviews = []
for r in all_reviews:
    # SerpAPI renvoie iso_date ("2024-09-12T10:00:00") + date ("il y a 2 mois")
    iso = r.get("iso_date") or ""
    ts = 0
    if iso:
        try:
            ts = int(time.mktime(time.strptime(iso[:19], "%Y-%m-%dT%H:%M:%S")))
        except Exception:
            ts = 0
    if ts and ts < cutoff:
        continue  # avis trop vieux
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
    "place_url":          place_info.get("address", "") and
                          f"https://www.google.com/maps/place/?q=place_id:{PLACE_ID}" or "",
    "rating":             place_info.get("rating", 0),
    "total":              place_info.get("reviews", 0),
    "reviews":            reviews,
    "returned_by_serpapi": len(all_reviews),
    "kept_recent":        len(reviews),
    "cutoff_iso":         time.strftime("%Y-%m-%d", time.gmtime(cutoff)),
    "fetched_at":         int(time.time()),
    "source":             "serpapi",
}

with open(OUT_FILE, "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print(f"✓ Wrote {OUT_FILE}: {len(reviews)} review(s) kept out of {len(all_reviews)} returned. "
      f"Place rating: {place_info.get('rating', '?')} ({place_info.get('reviews', '?')} avis total)")
