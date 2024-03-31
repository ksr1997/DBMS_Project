-- Store Table
CREATE TABLE Store (
    store_id VARCHAR(10) PRIMARY KEY,
    store_name VARCHAR(100),
    address VARCHAR(255),
    city VARCHAR(100),
    country VARCHAR(100),
    phone_number VARCHAR(20)
);

-- Customer Table
CREATE TABLE Customer (
    customer_id VARCHAR(10) PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    address VARCHAR(255),
    phone_number VARCHAR(20)
);

-- Seller Table
CREATE TABLE Seller (
    seller_id VARCHAR(10) PRIMARY KEY,
    seller_name VARCHAR(100),
    address VARCHAR(255),
    phone_number VARCHAR(20),
    email VARCHAR(100),
    joined_year NUMERIC
);

-- Product Table
CREATE TABLE Product (
    product_id VARCHAR(10) PRIMARY KEY,
    name VARCHAR(100),
    brand VARCHAR(100),
    price NUMERIC,
    qty_left_in_stock NUMERIC,
    manf_date DATE,
    exp_date DATE,
    manufacturer VARCHAR(100),
    disease VARCHAR(100)
);

-- Sale Table
CREATE TABLE Sale (
    sale_id VARCHAR(10) PRIMARY KEY,
    sale_date DATE,
    order_id VARCHAR(10),
    product_id VARCHAR(10),
    price NUMERIC,
    store_id VARCHAR(10),
    seller_id VARCHAR(10),
    customer_id VARCHAR(10),
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (product_id) REFERENCES Product(product_id),
    FOREIGN KEY (store_id) REFERENCES Store(store_id),
    FOREIGN KEY (seller_id) REFERENCES Seller(seller_id),
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
);
