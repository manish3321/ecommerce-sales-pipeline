import requests
import json
import os

BASE_URL = "https://dummyjson.com"
ENDPOINTS = ["products", "users", "carts"]
OUTPUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data/api_raw"))

MAX_LIMIT = 100  # max allowed per request by API
TARGET_TOTAL = 1000

os.makedirs(OUTPUT_DIR, exist_ok=True)

def fetch_paginated(endpoint):
    all_items = []
    for skip in range(0, TARGET_TOTAL, MAX_LIMIT):
        url = f"{BASE_URL}/{endpoint}?limit={MAX_LIMIT}&skip={skip}"
        res = requests.get(url)
        if res.status_code == 200:
            data = res.json()
            if isinstance(data, dict) and 'products' in data:
                all_items.extend(data['products'])
            elif 'users' in data:
                all_items.extend(data['users'])
            elif 'carts' in data:
                all_items.extend(data['carts'])
            else:
                print(f"Unexpected format for {endpoint}")
        else:
            print(f"Error fetching {endpoint} (skip={skip})")
            break
    return all_items

if __name__ == "__main__":
    for ep in ENDPOINTS:
        items = fetch_paginated(ep)
        with open(f"{OUTPUT_DIR}/{ep}.json", "w") as f:
            json.dump(items, f, indent=2)
        print(f"Fetched {len(items)} records from {ep}")

