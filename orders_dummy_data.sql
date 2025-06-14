-- orders_dummy_data.sql
-- Dummy data for orders table

CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    order_date DATE,
    amount NUMERIC,
    product_id INTEGER
);

INSERT INTO orders (order_date, amount, product_id) VALUES
('2023-01-15', 250, 1),
('2023-01-17', 150, 2),
('2023-02-05', 200, 1),
('2023-02-18', 300, 3),
('2023-03-01', 450, 4),
('2023-03-21', 100, 2),
('2023-03-22', 500, 5),
('2023-04-10', 600, 1);
