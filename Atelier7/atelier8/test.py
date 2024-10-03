import requests

BASE = "http://127.0.0.1:5000/"
TOKEN = "secrettoken123"
headers = {"Authorization": f"Bearer {TOKEN}"}

def test_put():
    url = BASE + "video/1"
    payload = {
        "name": "Flask Tutorial",
        "description": "Comprehensive guide to Flask",
        "likes": 150,
        "views": 2000
    }
    response = requests.put(url, json=payload, headers=headers)
    print("PUT /video/1:", response.json())

def test_get():
    url = BASE + "video/1"
    response = requests.get(url, headers=headers)
    print("GET /video/1:", response.json())

def test_patch():
    url = BASE + "video/1"
    payload = {
        "name": "Flask Deep Dive",
        "likes": 200
    }
    response = requests.patch(url, json=payload, headers=headers)
    print("PATCH /video/1:", response.json())

def test_get_updated():
    url = BASE + "video/1"
    response = requests.get(url, headers=headers)
    print("GET /video/1 (after update):", response.json())

def test_delete():
    url = BASE + "video/1"
    response = requests.delete(url, headers=headers)
    print("DELETE /video/1:", response.status_code)

def test_get_deleted():
    url = BASE + "video/1"
    response = requests.get(url, headers=headers)
    if response.status_code == 404:
        print("GET /video/1: Video not found (as expected)")
    else:
        print("GET /video/1:", response.json())

if __name__ == "__main__":
    test_put()
    test_get()
    test_patch()
    test_get_updated()
    test_delete()
    test_get_deleted()
