# Ecommerce

									Ecommerce System


This database Model is a management tool that helps Customers to order products online and manage their profiles.

For creating the database we've used MYSQL which is a free and popular DBMS.

This model has 4 tables listed below:
1.) customers:


customer_id INTEGER PRIMARY KEY,

name TEXT NOT NULL,

email TEXT UNIQUE NOT NULL,

address TEXT NOT NULL 

2.) orders

order_id INTEGER PRIMARY KEY,

order_date DATE NOT NULL,

customer_id INTEGER NOT NULL,


3.) order_details

order_detail_id INTEGER 

order_id INTEGER NOT NULL,

product_id INTEGER NOT NULL,

quantity INTEGER NOT NULL,

price REAL NOT NULL
    
4.)products
   
   product_id INTEGER PRIMARY KEY ,
   
   product_name varchar(25) NOT NULL,
   
   manufacturer varchar(25) NOT NULL
