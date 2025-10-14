#!/usr/bin/env python3

import requests
import yaml

# 🔑 Replace this with your Raindrop.io Personal Access Token
API_TOKEN = "3e921b34-b31a-447a-8335-b4aab6fc6d49"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

# --- Helpers ---

def fetch_collections():
    """Fetch all collections (folders)"""
    resp = requests.get("https://api.raindrop.io/rest/v1/collections", headers=headers).json()
    if "items" not in resp:
        raise Exception("Error fetching collections: " + str(resp))
    return resp["items"]

def fetch_bookmarks(collection_id):
    """Fetch all bookmarks in a collection"""
    url = f"https://api.raindrop.io/rest/v1/raindrops/{collection_id}"
    items, page = [], 0
    while True:
        page += 1
        resp = requests.get(url, headers=headers, params={"page": page, "perpage": 50}).json()
        batch = resp.get("items", [])
        if not batch:
            break
        for b in batch:
            items.append({
                "title": b["title"],
                "url": b["link"],
                "excerpt": b.get("excerpt", ""),
                "tags": b.get("tags", [])
            })
    return items

def build_tree(collections, parent=None):
    """Recursively build folder structure"""
    tree = []
    for col in [c for c in collections if c.get("parent") == parent]:
        node = {
            "category": col["title"],
            "id": col["_id"],
            "links": fetch_bookmarks(col["_id"]),
            "children": build_tree(collections, col["_id"])
        }
        tree.append(node)
    print(f"Tree: {tree}")
    return tree

def export_to_yaml(data, filename="../_data/bookmarks.yml"):
    """Save nested structure to YAML"""
    with open(filename, "w", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True, sort_keys=False)
    print(f"✅ Exported {filename}")

# --- Main ---
if __name__ == "__main__":
    print("📂 Fetching collections...")
    collections = fetch_collections()
    print(f"Found {len(collections)} collections")

    print("🔗 Building nested structure...")
    nested_data = build_tree(collections)

    print("💾 Exporting to YAML...")
    export_to_yaml(nested_data)
