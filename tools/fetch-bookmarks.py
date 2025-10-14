#!/usr/bin/env python3

import requests, yaml

API_TOKEN = "3e921b34-b31a-447a-8335-b4aab6fc6d49"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

# 1. Get all collections (folders)
collections = requests.get(
    "https://api.raindrop.io/rest/v1/collections",
    headers=headers
).json()["items"]

def fetch_bookmarks(collection_id):
    url = f"https://api.raindrop.io/rest/v1/raindrops/{collection_id}"
    items = []
    page = 0
    while True:
        page += 1
        resp = requests.get(
            url,
            headers=headers,
            params={"page": page, "perpage": 50}
        ).json()
        batch = resp.get("items", [])
        if not batch:
            break
        for item in batch:
            items.append({
                "title": item["title"],
                "url": item["link"],
                "excerpt": item.get("excerpt", ""),
                "tags": item.get("tags", [])
            })
    return items

# 2. Build structured data
data = []
for col in collections:
    col_id = col["_id"]       # this is the correct ID
    col_title = col["title"]  # folder name
    bookmarks = fetch_bookmarks(col_id)
    data.append({
        "category": col_title,
        "links": bookmarks
    })

# 3. Save to Jekyll data file
with open("../_data/bookmarks.yml", "w", encoding="utf-8") as f:
    yaml.dump(data, f, allow_unicode=True, sort_keys=False)

print("✅ Bookmarks exported successfully!")

