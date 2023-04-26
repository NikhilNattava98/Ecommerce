INSERT INTO customers (name, email, address) VALUES
('John Doe', 'johndoe@gmail.com', '123 Main St'),
('Jane Smith', 'janesmith@yahoo.com', '456 Oak Ave'),
('Bob Johnson', 'bjohnson@hotmail.com', '789 Elm St'),
('Alice Lee', 'alicelee@gmail.com', '234 Maple Rd'),
('Sam Wilson', 'samwilson@gmail.com', '567 Pine St');

-- Insert 5 rows into the orders table
INSERT INTO orders (order_date, customer_id) VALUES
('2023-04-24', 1),
('2023-04-24', 2),
('2023-04-25', 3),
('2023-04-25', 4),
('2023-04-25', 5);

INSERT INTO order_details (order_id, product_id, quantity, price) VALUES
(1, 1, 2, 19.99),
(1, 2, 1, 29.99),
(2, 3, 3, 9.99),
(3, 2, 2, 29.99),
(4, 4, 1, 49.99);

INSERT INTO products (product_id, product_name, manufacturer) VALUES
(101, 'Jeans', 'Levis'),
(102, 'Shoes', 'Woodland'),
(103, 'Laptop', 'HP'),
(104, 'Mobile', 'Apple'),
(105, 'Earphones', 'Realme');




