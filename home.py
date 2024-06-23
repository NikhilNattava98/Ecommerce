import mysql.connector
import tkinter as tk
from tkinter import messagebox

# mydbect to the Mysql database

        
 
# Create the main window
root = tk.Tk()
root.title('CRUD Operations')

# Define the function to add a new customer
def add_customer():
    mydb = mysql.connector.connect(host='localhost', port=3306, user='root', password='admin', database='ecommerce')
    c = mydb.cursor()
    name = name_var.get()
    email = email_var.get()
    address = address_var.get()
    c.execute("INSERT INTO customers (name, email, address) VALUES (%s, %s, %s)", (name, email, address))
    mydb.commit()
    messagebox.showinfo('Success', 'Customer added successfully.')

# Define the function to update an existing customer
def update_customer():
    mydb = mysql.connector.connect(host='localhost', port=3306, user='root', password='admin', database='ecommerce')
    c = mydb.cursor()
    customer_id = customer_id_var.get()
    name = name_var.get()
    email = email_var.get()
    address = address_var.get()
    c.execute("UPDATE customers SET name=%s, email=%s, address=%s WHERE customer_id=%s", (name, email, address, customer_id))
    mydb.commit()
    messagebox.showinfo('Success', 'Customer updated successfully.')

# Define the function to delete an existing customer
def delete_customer():
    mydb = mysql.connector.connect(host='localhost', port=3306, user='root', password='admin', database='ecommerce')
    c = mydb.cursor()
    customer_id = customer_id_var.get()
    values = (customer_id,)
    c.execute("DELETE FROM customers WHERE customer_id=%s", values)
    mydb.commit()
    messagebox.showinfo('Success', 'Customer deleted successfully.')

# Define the function to view all customers
def view_customers():
    mydb = mysql.connector.connect(host='localhost', port=3306, user='root', password='admin', database='ecommerce')
    c = mydb.cursor()
    c.execute("SELECT * FROM customers")
    rows = c.fetchall()
    for row in rows:
        print(row)

# Create the input fields
customer_id_label = tk.Label(root, text='Customer ID')
customer_id_label.grid(row=0, column=0)
customer_id_var = tk.StringVar()
customer_id_entry = tk.Entry(root, textvariable=customer_id_var)
customer_id_entry.grid(row=0, column=1)

name_label = tk.Label(root, text='Name')
name_label.grid(row=1, column=0)
name_var = tk.StringVar()
name_entry = tk.Entry(root, textvariable=name_var)
name_entry.grid(row=1, column=1)

email_label = tk.Label(root, text='Email')
email_label.grid(row=2, column=0)
email_var = tk.StringVar()
email_entry = tk.Entry(root, textvariable=email_var)
email_entry.grid(row=2, column=1)

address_label = tk.Label(root, text='Address')
address_label.grid(row=3, column=0)
address_var = tk.StringVar()
address_entry = tk.Entry(root, textvariable=address_var)
address_entry.grid(row=3, column=1)

# Create the buttons
add_button = tk.Button(root, text='Add Customer', command=add_customer)
add_button.grid(row=4, column=0)

update_button = tk.Button(root, text='Update Customer', command=update_customer)
update_button.grid(row=4, column=1)

delete_button = tk.Button(root, text='Delete Customer', command=delete_customer)
delete_button.grid(row=4, column=2)

view_button = tk.Button(root, text='View Customers', command=view_customers)
view_button.grid(row=5, column=1)

# Start the main loop
root.mainloop()

mydb.close()
