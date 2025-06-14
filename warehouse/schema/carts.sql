-- Cart metadata
CREATE TABLE IF NOT EXISTS carts (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    total NUMERIC,
    discounted_total NUMERIC,
    total_products INTEGER,
    total_quantity INTEGER,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

-- Cart products (one row per item in a cart)
CREATE TABLE IF NOT EXISTS cart_items (
    cart_id INTEGER REFERENCES carts(id),
    product_id INTEGER,
    title TEXT,
    price NUMERIC,
    quantity INTEGER,
    total NUMERIC,
    discount_percentage NUMERIC,
    discounted_price NUMERIC
);
