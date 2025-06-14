import os
import json
import psycopg
from datetime import datetime

DATA_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../Data/api_raw/users.json"))
SCHEMA_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), "../schema/users.sql"))

DB_CONFIG = {
    "dbname": "retaildb",
    "user": "retail",
    "password": "retail",
    "host": "pgdb",
    "port": "5432"
}

def load_users():
    with open(DATA_FILE) as f:
        return json.load(f)

def create_tables(cur):
    with open(SCHEMA_FILE) as f:
        cur.execute(f.read())

def insert_user(cur, u):
    # Users table
    cur.execute("""
        INSERT INTO users (
            id, first_name, last_name, maiden_name, age, gender,
            email, phone, username, password, birth_date, image,
            blood_group, height, weight, eye_color, domain, ip
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (id) DO NOTHING
    """, (
        u["id"], u["firstName"], u["lastName"], u.get("maidenName"), u["age"], u["gender"],
        u["email"], u["phone"], u["username"], u["password"], u.get("birthDate"),
        u.get("image"), u.get("bloodGroup"), u.get("height"), u.get("weight"),
        u.get("eyeColor"), u.get("domain"), u.get("ip")
    ))

    # Hair table
    if "hair" in u:
        cur.execute("""
            INSERT INTO user_hair (user_id, hair_color, hair_type)
            VALUES (%s, %s, %s)
        """, (u["id"], u["hair"].get("color"), u["hair"].get("type")))

    # Address table
    if "address" in u:
        addr = u["address"]
        coords = addr.get("coordinates", {})
        cur.execute("""
            INSERT INTO user_address (
                user_id, street_address, city, state, postal_code, latitude, longitude
            ) VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            u["id"], addr.get("address"), addr.get("city"), addr.get("state"),
            addr.get("postalCode"), coords.get("lat"), coords.get("lng")
        ))

    # Company table
    if "company" in u:
        company = u["company"]
        cur.execute("""
            INSERT INTO user_company (user_id, company_name, title, department)
            VALUES (%s, %s, %s, %s)
        """, (
            u["id"], company.get("name"), company.get("title"), company.get("department")
        ))

def main():
    conn = psycopg.connect(**DB_CONFIG)
    cur = conn.cursor()

    create_tables(cur)
    print("✅ User tables created")

    users = load_users()
    for u in users:
        insert_user(cur, u)

    conn.commit()
    cur.close()
    conn.close()
    print(f"✅ Loaded {len(users)} users successfully")

if __name__ == "__main__":
    main()
