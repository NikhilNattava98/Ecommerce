import sqlite3
import tkinter as tk
import mysql.connector
from tkinter import messagebox


# Create the main window
root = tk.Tk()
root.title('CRUD Operations')

# Define the function to add a new order
def add_order():
    mydb = mysql.connector.connect(host='localhost', port=3306, user='root', password='admin', database='ecommerce')
    c = mydb.cursor()
    order_date = order_date_var.get()
    customer_id = customer_id_var.get()
    c.execute("INSERT INTO orders (order_date, customer_id) VALUES (%s, %s)", (order_date, customer_id))
    mydb.commit()
    messagebox.showinfo('Success', 'Order added successfully.')

# Define the function to update an existing order
def update_order():
    mydb = mysql.connector.connect(host='localhost', port=3306, user='root', password='admin', database='ecommerce')
    c = mydb.cursor()
    order_id = order_id_var.get()
    order_date = order_date_var.get()
    customer_id = customer_id_var.get()
    c.execute("UPDATE orders SET order_date=?, customer_id=? WHERE order_id=%s", (order_date, customer_id, order_id))
    mydb.commit()
    messagebox.showinfo('Success', 'Order updated successfully.')

# Define the function to delete an existing order
def delete_order():
    mydb = mysql.connector.connect(host='localhost', port=3306, user='root', password='admin', database='ecommerce')
    c = mydb.cursor()
    order_id = order_id_var.get()
    c.execute("DELETE FROM orders WHERE order_id=%s", (order_id,))
    mydb.commit()
    messagebox.showinfo('Success', 'Order deleted successfully.')

# Define the function to view all orders
def view_orders():
    mydb = mysql.connector.connect(host='localhost', port=3306, user='root', password='admin', database='ecommerce')
    c = mydb.cursor()
    c.execute("SELECT * FROM orders")
    rows = c.fetchall()
    for row in rows:
        print(row)

# Create the input fields
order_id_label = tk.Label(root, text='Order ID')
order_id_label.grid(row=0, column=0)
order_id_var = tk.StringVar()
order_id_entry = tk.Entry(root, textvariable=order_id_var)
order_id_entry.grid(row=0, column=1)

order_date_label = tk.Label(root, text='Order Date')
order_date_label.grid(row=1, column=0)
order_date_var = tk.StringVar()
order_date_entry = tk.Entry(root, textvariable=order_date_var)
order_date_entry.grid(row=1, column=1)

customer_id_label = tk.Label(root, text='Customer ID')
customer_id_label.grid(row=2, column=0)
customer_id_var = tk.StringVar()
customer_id_entry = tk.Entry(root, textvariable=customer_id_var)
customer_id_entry.grid(row=2, column=1)

# Create the buttons
add_button = tk.Button(root, text='Add Order', command=add_order)
add_button.grid(row=3, column=0)

update_button = tk.Button(root, text='Update Order', command=update_order)
update_button.grid(row=3, column=1)

delete_button = tk.Button(root, text='Delete Order', command=delete_order)
delete_button.grid(row=3, column=2)

view_button = tk.Button(root, text='View Orders', command=view_orders)
view_button.grid(row=4, column=1)

# Start the main loop
root.mainloop()

mydb.close()
