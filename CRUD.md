CRUD on Customer Table:

INSERT INTO customers (name, email, address) VALUES ('Ramesh', 'ramesh@gmail.com','Hyderbad');

UPDATE customers SET name='Suresh', email='suresh@gmail.com', address='Guntur' WHERE customer_id=1";

DELETE FROM customers WHERE customer_id=1;

SELECT * FROM customers;


CRUD on Oder_details Table:

INSERT INTO order_details (order_id, product_id, quantity, price) VALUES (10, 101, 5, 600);

UPDATE order_details SET order_id=2, product_id=33, quantity=66, price=1000 WHERE order_detail_id=10;

DELETE FROM order_details WHERE order_detail_id='100';

SELECT * FROM order_details;




CURD ON order Table:

INSERT INTO orders (order_date, customer_id) VALUES ('2023-04-24', 1);

UPDATE orders SET order_date='2023-04-26', customer_id=10 WHERE order_id=11;

DELETE FROM orders WHERE order_id=10;

SELECT * FROM orders;



CRUD on Products Table:

INSERT INTO products (product_id, product_name, manufacturer) VALUES (10,'Apple','Apple');

UPDATE products SET product_name=Iphone, manufacturer=apple WHERE product_id=10

DELETE FROM products WHERE product_id=100;

SELECT * FROM products;
