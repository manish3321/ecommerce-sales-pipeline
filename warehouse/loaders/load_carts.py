import os
import json
import psycopg
from datetime import datetime

DATA_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../Data/api_raw/carts.json"))
SCHEMA_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), "../schema/carts.sql"))

DB_CONFIG = {
    "dbname": "retaildb",
    "user": "retail",
    "password": "retail",
    "host": "pgdb",
    "port": "5432"
}

def load_carts():
    with open(DATA_FILE) as f:
        return json.load(f)

def create_tables(cur):
    with open(SCHEMA_FILE) as f:
        cur.execute(f.read())

def insert_cart(cur, cart):
    cur.execute("""
        INSERT INTO carts (
            id, user_id, total, discounted_total,
            total_products, total_quantity, created_at, updated_at
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (id) DO NOTHING
    """, (
        cart["id"], cart["userId"], cart["total"], cart["discountedTotal"],
        cart["totalProducts"], cart["totalQuantity"],
        cart.get("createdAt"), cart.get("updatedAt")
    ))

    for item in cart.get("products", []):
        cur.execute("""
            INSERT INTO cart_items (
                cart_id, product_id, title, price, quantity,
                total, discount_percentage, discounted_price
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            cart["id"], item["id"], item["title"], item["price"], item["quantity"],
            item["total"], item.get("discountPercentage"), item.get("discountedPrice")
        ))

def main():
    conn = psycopg.connect(**DB_CONFIG)
    cur = conn.cursor()

    create_tables(cur)
    print("✅ Cart tables created")

    carts = load_carts()
    for cart in carts:
        insert_cart(cur, cart)

    conn.commit()
    cur.close()
    conn.close()
    print(f"✅ Loaded {len(carts)} carts and items successfully")

if __name__ == "__main__":
    main()
