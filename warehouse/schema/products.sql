CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    title TEXT,
    description TEXT,
    category TEXT,
    price NUMERIC,
    discountPercentage NUMERIC,
    rating NUMERIC,
    stock INTEGER,
    brand TEXT,
    sku TEXT,
    weight NUMERIC,
    warrantyInformation TEXT,
    shippingInformation TEXT,
    availabilityStatus TEXT,
    returnPolicy TEXT,
    minimumOrderQuantity INTEGER,
    thumbnail TEXT


);

--Dimension Table
CREATE TABLE IF NOT EXISTS product_dimensions (
    product_id INTEGER REFERENCES products(id),
    width NUMERIC,
    height NUMERIC,
    depth NUMERIC
);


--Meta table
CREATE TABLE IF NOT EXISTS product_meta (

    product_id INTEGER REFERENCES products(id),
    createdAt TIMESTAMP,
    updatedAt TIMESTAMP,
    barcode TEXT,
    qrCode TEXT

);

--Tags

CREATE TABLE IF NOT EXISTS product_tags (
    product_id INTEGER REFERENCES products(id),
    tag TEXT
);

--Reviews

CREATE TABLE IF NOT EXISTS product_reviews (
    product_id INTEGER REFERENCES products(id),
    rating NUMERIC,
    comment TEXT,
    review_date TIMESTAMP,
    reviewer_name TEXT,
    reviewer_email TEXT
);


CREATE TABLE IF NOT EXISTS product_images (
 product_id INTEGER REFERENCES products(id),
 image_url TEXT
);