import sqlite3
import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title('CRUD Operations - Products')

# Define the function to add a new order detail
def add_product_detail():
    mydb = mysql.connector.connect(host='localhost', port=3306, user='root', password='admin', database='ecommerce')
    c = mydb.cursor()
    product_id = product_id_var.get()
    product_name = product_name_var.get()
    manufacturer = manufacturer_var.get()
    c.execute("INSERT INTO products (product_id, product_name, manufacturer) VALUES (%s,%s,%s)", (product_id, product_name, manufacturer))
    mydb.commit()
    messagebox.showinfo('Success', 'Product detail added successfully.')

# Define the function to update an existing Product detail
def update_product_detail():    
    mydb = mysql.connector.connect(host='localhost', port=3306, user='root', password='admin', database='ecommerce')
    c = mydb.cursor()
    product_id = product_id_var.get()
    product_name = product_name_var.get()
    manufacturer = manufacturer_var.get()
    c.execute("UPDATE products SET product_name=%s, manufacturer=%s WHERE product_id=%s",       
    (product_name, manufacturer, product_id))
    mydb.commit()
    messagebox.showinfo('Success', 'product detail updated successfully.')

# Define the function to delete an existing product detail
def delete_product_detail():
    mydb = mysql.connector.connect(host='localhost', port=3306, user='root', password='admin', database='ecommerce')
    c = mydb.cursor()
    product_id = product_id_var.get()
    c.execute("DELETE FROM products WHERE order_detail_id=%s", (product_id))
    mydb.commit()
    messagebox.showinfo('Success', 'Product detail deleted successfully.')

# Define the function to view all order details
def view_product_details():
    mydb = mysql.connector.connect(host='localhost', port=3306, user='root', password='admin', database='ecommerce')
    c = mydb.cursor()
    c.execute("SELECT * FROM products")
    rows = c.fetchall()
    for row in rows:
        print(row)


# Create the input fields
order_detail_id_label = tk.Label(root, text='Product ID')
order_detail_id_label.grid(row=0, column=0)
order_detail_id_var = tk.StringVar()
order_detail_id_entry = tk.Entry(root, textvariable=product_id_var.get())
order_detail_id_entry.grid(row=0, column=1)

order_id_label = tk.Label(root, text='Product Name')
order_id_label.grid(row=1, column=0)
order_id_var = tk.StringVar()
order_id_entry = tk.Entry(root, textvariable=product_name)
order_id_entry.grid(row=1, column=1)

product_id_label = tk.Label(root, text='manufacturer')
product_id_label.grid(row=2, column=0)
product_id_var = tk.StringVar()
product_id_entry = tk.Entry(root, textvariable=manufacturer)
product_id_entry.grid(row=2, column=1)


# Create the buttons
add_button = tk.Button(root, text='Add Product Detail', command=add_product_detail)
add_button.grid(row=5, column=0)

update_button = tk.Button(root, text='Update Product Detail',command=update_product_detail)
update_button.grid(row=5, column=1)
delete_button = tk.Button(root, text='Delete Product Details', command=delete_product_detail)
delete_button.grid(row=5, column=3)

view_button = tk.Button(root, text='View Product Details', command=view_product_details)
view_button.grid(row=5, column=4)
# delete_button = tk.Button(root)

root.mainloop()

mydb.close()

