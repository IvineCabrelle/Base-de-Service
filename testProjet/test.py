# -*- coding: utf-8 -*-
import pytest
import requests

BASE = "http://127.0.0.1:5000/"
TOKEN = "secrettoken123"  # Remplacez par un jeton valide
HEADERS = {"Authorization": f"Bearer {TOKEN}"}

def test_put_order():
    response = requests.put(BASE + "order/1", json={
        "product_name": "Widget A",
        "quantity": 5,
        "price": 25.00,
        "order_date": "2023-07-24"
    }, headers=HEADERS)
    assert response.status_code == 201
    assert response.json()['product_name'] == "Widget A"

def test_get_order():
    response = requests.get(BASE + "order/1", headers=HEADERS)
    assert response.status_code == 200
    assert response.json()['product_name'] == "Widget A"

def test_patch_order():
    response = requests.patch(BASE + "order/1", json={
        "quantity": 10,
        "price": 50.00
    }, headers=HEADERS)
    assert response.status_code == 200
    assert response.json()['quantity'] == 10

def test_delete_order():
    response = requests.delete(BASE + "order/1", headers=HEADERS)
    assert response.status_code == 204

def test_get_order_after_deletion():
    response = requests.get(BASE + "order/1", headers=HEADERS)
    assert response.status_code == 404

def test_search_orders():
    response = requests.get(BASE + "ordersearch/Widget A", headers=HEADERS)
    assert response.status_code == 404  # Pas de résultat attendu après suppression

if __name__ == "__main__":
    pytest.main()
