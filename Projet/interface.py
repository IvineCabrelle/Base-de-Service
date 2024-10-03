import tkinter as tk
from tkinter import messagebox
import requests

# Configuration de base pour l'API
BASE = "http://127.0.0.1:5000/"
TOKEN = "secrettoken123"  # Remplacez par un jeton valide
headers = {"Authorization": f"Bearer {TOKEN}"}

def send_request(method, endpoint, json_data=None):
    try:
        if method == 'PUT':
            response = requests.put(BASE + endpoint, json=json_data, headers=headers)
        elif method == 'GET':
            response = requests.get(BASE + endpoint, headers=headers)
        elif method == 'PATCH':
            response = requests.patch(BASE + endpoint, json=json_data, headers=headers)
        elif method == 'DELETE':
            response = requests.delete(BASE + endpoint, headers=headers)
        else:
            raise ValueError("Invalid HTTP method")

        response.raise_for_status()  # Vérifie les erreurs HTTP
        print(f"Response from {method} {endpoint}: {response.json()}")  # Affiche la réponse dans le terminal
        return response
    except requests.RequestException as e:
        messagebox.showerror("Error", f"Request failed: {str(e)}")
        print(f"Request failed: {str(e)}")  # Affiche l'erreur dans le terminal
        return None

def validate_entries():
    try:
        quantity = int(quantity_entry.get())
        price = float(price_entry.get())
        return quantity, price
    except ValueError:
        messagebox.showerror("Input Error", "Quantity and Price must be numbers.")
        return None, None

def put_order():
    quantity, price = validate_entries()
    if quantity is None or price is None:
        return

    json_data = {
        "product_name": product_name_entry.get(),
        "quantity": quantity,
        "price": price,
        "order_date": date_entry.get()
    }
    response = send_request('PUT', f"order/{order_id_entry.get()}", json_data)
    if response:
        messagebox.showinfo("Response", f"PUT /order/{order_id_entry.get()}: {response.json()}")
        print(f"PUT /order/{order_id_entry.get()}: {response.json()}")  # Affiche la réponse dans le terminal

def get_order():
    response = send_request('GET', f"order/{order_id_entry.get()}")
    if response:
        messagebox.showinfo("Response", f"GET /order/{order_id_entry.get()}: {response.json()}")
        print(f"GET /order/{order_id_entry.get()}: {response.json()}")  # Affiche la réponse dans le terminal

def patch_order():
    quantity, price = validate_entries()
    if quantity is None or price is None:
        return

    json_data = {
        "quantity": quantity,
        "price": price
    }
    response = send_request('PATCH', f"order/{order_id_entry.get()}", json_data)
    if response:
        messagebox.showinfo("Response", f"PATCH /order/{order_id_entry.get()}: {response.json()}")
        print(f"PATCH /order/{order_id_entry.get()}: {response.json()}")  # Affiche la réponse dans le terminal

def delete_order():
    response = send_request('DELETE', f"order/{order_id_entry.get()}")
    if response:
        if response.status_code == 204:
            messagebox.showinfo("Response", "DELETE /order: Success")
            print("DELETE /order: Success")  # Affiche le succès dans le terminal
        else:
            messagebox.showinfo("Response", f"DELETE /order: {response.status_code}")
            print(f"DELETE /order: {response.status_code}")  # Affiche le code de statut dans le terminal

def search_order():
    product_name = search_entry.get()
    if not product_name:
        messagebox.showerror("Input Error", "Product name cannot be empty.")
        return

    response = send_request('GET', f"ordersearch/{product_name}")
    if response:
        try:
            data = response.json()
            messagebox.showinfo("Response", f"GET /ordersearch/{product_name}: {data}")
            print(f"GET /ordersearch/{product_name}: {data}")  # Affiche la réponse dans le terminal
        except ValueError as e:
            messagebox.showerror("Error", f"Failed to decode JSON response: {str(e)}")
            print(f"Failed to decode JSON response: {str(e)}")  # Affiche l'erreur de décodage JSON
    else:
        print("No response received or failed request.")


# Création de l'interface Tkinter
app = tk.Tk()
app.title("Order Management")

tk.Label(app, text="Order ID").grid(row=0, column=0)
order_id_entry = tk.Entry(app)
order_id_entry.grid(row=0, column=1)

tk.Label(app, text="Product Name").grid(row=1, column=0)
product_name_entry = tk.Entry(app)
product_name_entry.grid(row=1, column=1)

tk.Label(app, text="Quantity").grid(row=2, column=0)
quantity_entry = tk.Entry(app)
quantity_entry.grid(row=2, column=1)

tk.Label(app, text="Price").grid(row=3, column=0)
price_entry = tk.Entry(app)
price_entry.grid(row=3, column=1)

tk.Label(app, text="Order Date (YYYY-MM-DD)").grid(row=4, column=0)
date_entry = tk.Entry(app)
date_entry.grid(row=4, column=1)

tk.Button(app, text="Create Order (PUT)", command=put_order).grid(row=5, column=0, columnspan=2, pady=5)
tk.Button(app, text="Retrieve Order (GET)", command=get_order).grid(row=6, column=0, columnspan=2, pady=5)
tk.Button(app, text="Update Order (PATCH)", command=patch_order).grid(row=7, column=0, columnspan=2, pady=5)
tk.Button(app, text="Delete Order (DELETE)", command=delete_order).grid(row=8, column=0, columnspan=2, pady=5)

tk.Label(app, text="Search Product").grid(row=9, column=0)
search_entry = tk.Entry(app)
search_entry.grid(row=9, column=1)
tk.Button(app, text="Search Orders", command=search_order).grid(row=10, column=0, columnspan=2, pady=5)

app.mainloop()
