#!/usr/bin/env python3
"""
Récupère les avis Google Places pour le Judo Club Anderlecht, filtre ceux
des 6 derniers mois, et écrit le résultat dans google-reviews.json.

Secrets GitHub requis :
  - GOOGLE_API_KEY   : clé API Google Cloud (Places API activée)
  - GOOGLE_PLACE_ID  : identifiant de la fiche Google (ex: ChIJ...)
"""
import json
import os
import sys
import time
import urllib.parse
import urllib.request

API_KEY   = os.environ.get("GOOGLE_API_KEY", "").strip()
PLACE_ID  = os.environ.get("GOOGLE_PLACE_ID", "").strip()
OUT_FILE  = "google-reviews.json"
SIX_MONTHS = 180 * 24 * 3600  # seconds

if not API_KEY or not PLACE_ID:
    print("GOOGLE_API_KEY or GOOGLE_PLACE_ID missing — writing empty file.")
    with open(OUT_FILE, "w", encoding="utf-8") as f:
        json.dump({"reviews": [], "fetched_at": int(time.time()), "error": "missing secrets"}, f, ensure_ascii=False, indent=2)
    sys.exit(0)

params = {
    "place_id": PLACE_ID,
    "fields": "name,rating,user_ratings_total,reviews,url",
    "language": "fr",
    "reviews_sort": "newest",
    "key": API_KEY,
}
url = "https://maps.googleapis.com/maps/api/place/details/json?" + urllib.parse.urlencode(params)

with urllib.request.urlopen(url, timeout=20) as resp:
    data = json.loads(resp.read().decode("utf-8"))

if data.get("status") != "OK":
    print(f"Google API error: {data.get('status')} — {data.get('error_message','')}")
    with open(OUT_FILE, "w", encoding="utf-8") as f:
        json.dump({"reviews": [], "fetched_at": int(time.time()), "error": data.get("status")}, f, ensure_ascii=False, indent=2)
    sys.exit(0)

result = data.get("result", {})
all_reviews = result.get("reviews", [])
cutoff = time.time() - SIX_MONTHS

reviews = []
for r in all_reviews:
    t = r.get("time", 0)
    if t < cutoff:
        continue
    reviews.append({
        "author": r.get("author_name", ""),
        "rating": r.get("rating", 0),
        "text":   r.get("text", "").strip(),
        "time":   t,
        "relative": r.get("relative_time_description", ""),
        "profile_photo": r.get("profile_photo_url", ""),
        "language": r.get("language", ""),
    })

out = {
    "place_name":   result.get("name", ""),
    "place_url":    result.get("url", ""),
    "rating":       result.get("rating", 0),
    "total":        result.get("user_ratings_total", 0),
    "reviews":      reviews,
    "returned_by_google": len(all_reviews),
    "kept_recent":  len(reviews),
    "cutoff_iso":   time.strftime("%Y-%m-%d", time.gmtime(cutoff)),
    "fetched_at":   int(time.time()),
}

with open(OUT_FILE, "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print(f"Wrote {OUT_FILE}: {len(reviews)} review(s) kept out of {len(all_reviews)} returned.")
