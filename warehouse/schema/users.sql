CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    maiden_name TEXT,
    age INTEGER,
    gender TEXT,
    email TEXT,
    phone TEXT,
    username TEXT,
    password TEXT,
    birth_date DATE,
    image TEXT,
    blood_group TEXT,
    height NUMERIC,
    weight NUMERIC,
    eye_color TEXT,
    domain TEXT,
    ip TEXT
);

CREATE TABLE IF NOT EXISTS user_hair (
    user_id INTEGER REFERENCES users(id),
    hair_color TEXT,
    hair_type TEXT
);

CREATE TABLE IF NOT EXISTS user_address (
    user_id INTEGER REFERENCES users(id),
    street_address TEXT,
    city TEXT,
    state TEXT,
    postal_code TEXT,
    latitude NUMERIC,
    longitude NUMERIC
);

CREATE TABLE IF NOT EXISTS user_company (
    user_id INTEGER REFERENCES users(id),
    company_name TEXT,
    title TEXT,
    department TEXT
);
