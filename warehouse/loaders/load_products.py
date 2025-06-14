import os
import json
import psycopg

DATA_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../Data/api_raw/products.json"))
SCHEMA_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../warehouse/schema/products.sql"))


DB_CONFIG = {
    "dbname": "retaildb",
    "user": "retail",
    "password": "retail",
    "host": "pgdb",
    "port": "5432"
}


def load_products():
    with open(DATA_FILE) as f:
        return json.load(f)


def create_tables(cur):
    with open(SCHEMA_FILE) as f:
        cur.execute(f.read())

def insert_product(cur, p):
    cur.execute("""
        INSERT INTO products (
    
        id, title, description, category, price, discountPercentage,rating, stock, brand, sku, weight, warrantyInformation, shippingInformation, availabilityStatus, returnPolicy, minimumOrderQuantity, thumbnail) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
        %s, %s, %s, %s) ON CONFLICT (id) DO NOTHING """, (


        p["id"], p["title"], p["description"], p["category"], p["price"], p["discountPercentage"], p["rating"], p["stock"], p.get("brand"), p.get("sku"),
        p.get("weight"), p.get("warrantyInformation"), p.get("shippingInformation"), p.get("availabilityStatus"),
        p.get("returnPolicy"), p.get("minimumOrderQuantitiy"), p["thumbnail"]
    )

    )

    dim = p.get("dimensions", {})
    if dim:
        cur.execute("""
            INSERT INTO product_dimensions (product_id, width, height, depth)
            VALUES (%s, %s, %s, %s) 
        """, (p["id"], dim.get("width"), dim.get("height"), dim.get("depth")))


    meta = p.get("meta", {})
    if meta:
        cur.execute("""
            INSERT INTO product_meta (product_id, createdAt, updatedAt, barcode, qrCode)
            VALUES (%s, %s, %s, %s, %s)
            """, (p["id"], meta.get("createdAt"), meta.get("updatedAt"), meta.get("barcode"), meta.get("qrCode"))
                        )

  #Tags

    for tag in p.get("tags", []):
        cur.execute("INSERT INTO product_tags (product_id, tag) VALUES (%s, %s)",
                    (p["id"], tag))

    for img in p.get("images", []):
        cur.execute("INSERT INTO product_images (product_id, image_url) VALUES (%s, %s)",
                    (p["id"],img))

    for r in p.get("reviews", []):
        cur.execute("INSERT INTO product_reviews (product_id, rating, comment, review_date, reviewer_name, reviewer_email) VALUES (%s, %s, %s, %s, %s, %s)",
                    (p["id"], r.get("rating"), r.get("comment"), r.get("date"), r.get("reviewerName"), r.get("reviewerEmail")))


def main():

    conn = psycopg.connect(**DB_CONFIG)
    cur = conn.cursor()

    create_tables(cur)
    print("Products table created")

    products = load_products()
    for p in products:
        insert_product(cur, p)

    conn.commit()
    cur.close()
    conn.close()
    print(f"Inserted {len(products)} products and related records")


if __name__ == "__main__":
    main()


