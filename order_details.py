import sqlite3
import tkinter as tk
from tkinter import messagebox

# mydbect to the Mysql database

# Create the main window
root = tk.Tk()
root.title('CRUD Operations - Order Details')

# Define the function to add a new order detail
def add_order_detail():
    mydb = mysql.connector.connect(host='localhost', port=3306, user='root', password='admin', database='ecommerce')
    c = mydb.cursor()
    order_id = order_id_var.get()
    product_id = product_id_var.get()
    quantity = quantity_var.get()
    price = price_var.get()
    c.execute("INSERT INTO order_details (order_id, product_id, quantity, price) VALUES (%s, %s, %s, %s)", (order_id, product_id, quantity, price))
    mydb.commit()
    messagebox.showinfo('Success', 'Order detail added successfully.')

# Define the function to update an existing order detail
def update_order_detail():
    mydb = mysql.connector.connect(host='localhost', port=3306, user='root', password='admin', database='ecommerce')
    c = mydb.cursor()
    order_detail_id = order_detail_id_var.get()
    order_id = order_id_var.get()
    product_id = product_id_var.get()
    quantity = quantity_var.get()
    price = price_var.get()
    c.execute("UPDATE order_details SET order_id=%s, product_id=%s, quantity=%s, price=%s WHERE order_detail_id=%s", (order_id, product_id, quantity, price, order_detail_id))
    mydb.commit()
    messagebox.showinfo('Success', 'Order detail updated successfully.')

# Define the function to delete an existing order detail
def delete_order_detail():
    mydb = mysql.connector.connect(host='localhost', port=3306, user='root', password='admin', database='ecommerce')
    c = mydb.cursor()
    order_detail_id = order_detail_id_var.get()
    c.execute("DELETE FROM order_details WHERE order_detail_id=%s", (order_detail_id,))
    mydb.commit()
    messagebox.showinfo('Success', 'Order detail deleted successfully.')

# Define the function to view all order details
def view_order_details():
    mydb = mysql.connector.connect(host='localhost', port=3306, user='root', password='admin', database='ecommerce')
    c = mydb.cursor()
    c.execute("SELECT * FROM order_details")
    rows = c.fetchall()
    for row in rows:
        print(row)


# Create the input fields
order_detail_id_label = tk.Label(root, text='Order Detail ID')
order_detail_id_label.grid(row=0, column=0)
order_detail_id_var = tk.StringVar()
order_detail_id_entry = tk.Entry(root, textvariable=order_detail_id_var)
order_detail_id_entry.grid(row=0, column=1)

order_id_label = tk.Label(root, text='Order ID')
order_id_label.grid(row=1, column=0)
order_id_var = tk.StringVar()
order_id_entry = tk.Entry(root, textvariable=order_id_var)
order_id_entry.grid(row=1, column=1)

product_id_label = tk.Label(root, text='Product ID')
product_id_label.grid(row=2, column=0)
product_id_var = tk.StringVar()
product_id_entry = tk.Entry(root, textvariable=product_id_var)
product_id_entry.grid(row=2, column=1)

quantity_label = tk.Label(root, text='Quantity')
quantity_label.grid(row=3, column=0)
quantity_var = tk.StringVar()
quantity_entry = tk.Entry(root, textvariable=quantity_var)
quantity_entry.grid(row=3, column=1)

price_label = tk.Label(root, text='Price')
price_label.grid(row=4, column=0)
price_var = tk.StringVar()
price_entry = tk.Entry(root, textvariable=price_var)
price_entry.grid(row=4, column=1)

# Create the buttons
add_button = tk.Button(root, text='Add Order Detail', command=add_order_detail)
add_button.grid(row=5, column=0)

update_button = tk.Button(root, text='Update Order Detail', command=update_order_detail)
update_button.grid(row=5, column=1)
delete_button = tk.Button(root, text='Delete Order Details', command=delete_order_detail)
delete_button.grid(row=5, column=3)

view_button = tk.Button(root, text='View Order Details', command=view_order_details)
view_button.grid(row=5, column=4)
# delete_button = tk.Button(root)

root.mainloop()

mydb.close()

