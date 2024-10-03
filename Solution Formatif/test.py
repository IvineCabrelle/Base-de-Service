# -*- coding: utf-8 -*-
import requests

BASE = "http://127.0.0.1:5000/"

# Définir un jeton d'authentification pour tester les requêtes
TOKEN = "secrettoken123"  # Remplacez par un jeton valide

# Ajouter un en-tête d'authentification avec le jeton
headers = {"Authorization": f"Bearer {TOKEN}"}

# Test PUT request to create a new order
response = requests.put(BASE + "order/1", json={"product_name": "Widget A", "quantity": 5, "price": 25.00, "order_date": "2023-07-24"}, headers=headers)
print("PUT /order/1:", response.json())

# Test GET request to retrieve the order
response = requests.get(BASE + "order/1", headers=headers)
print("GET /order/1:", response.json())

# Test PATCH request to update the order
response = requests.patch(BASE + "order/1", json={"quantity": 10, "price": 50.00}, headers=headers)
print("PATCH /order/1:", response.json())

# Test GET request again to see the updated order
response = requests.get(BASE + "order/1", headers=headers)
print("GET /order/1:", response.json())

# Test DELETE request to delete the order
response = requests.delete(BASE + "order/1", headers=headers)
print("DELETE /order/1:", response.status_code)

# Test GET request again to see if the order is deleted
response = requests.get(BASE + "order/1", headers=headers)
if response.status_code == 404:
    print("GET /order/1: order not found (as expected)")
else:
    print("GET /order/1:", response.json())


