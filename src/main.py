"""Sync TMDB lists to catalog JSONs."""
import os, json, requests
from pathlib import Path
from config import TMDB_LISTS, OUTPUT_DIR

TMDB_API_KEY = os.environ.get("TMDB_API_KEY", "")
BASE = "https://api.themoviedb.org/3"

def fetch_list(list_id):
    items = []
    page = 1
    while True:
        r = requests.get(f"{BASE}/list/{list_id}",
            params={"api_key": TMDB_API_KEY, "language": "en-US", "page": page}, timeout=30)
        r.raise_for_status()
        data = r.json()
        items.extend(data.get("items", []))
        if page >= data.get("total_pages", 1):
            break
        page += 1
    return items

def main():
    Path(OUTPUT_DIR).mkdir(exist_ok=True)
    catalog = {"catalogs": []}
    for name, list_id, media_type in TMDB_LISTS:
        print(f"Syncing {name}...")
        try:
            items = fetch_list(list_id)
            ids = [i["id"] for i in items if i.get("id")]
            with open(f"{OUTPUT_DIR}/{name}.json", "w") as f:
                json.dump({"tmdb_ids": ids, "media_type": media_type}, f)
            catalog["catalogs"].append({"name": name, "count": len(ids)})
            print(f"  {len(ids)} items")
        except Exception as e:
            print(f"  ERROR: {e}")
    with open(f"{OUTPUT_DIR}/index.json", "w") as f:
        json.dump(catalog, f, indent=2)
    print("Done")

if __name__ == "__main__":
    main()
