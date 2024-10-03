import requests
 
BASE = "http://127.0.0.1:5000/"
TOKEN = "secrettoken123"
headers = {"Authorization": f"Bearer {TOKEN}"}
# Test PUT request to create a new course
response = requests.put(BASE + "car/1", json={"make": "TOYOTA", "model": "14.2","year": "2015", "price": 50000})
print("PUT /car/1:", response.json())
 
# Test GET request to retrieve the car
response = requests.get(BASE + "car/1")
print("GET /car/1:", response.json())
 
# Test PATCH request to update the car
response = requests.patch(BASE + "car/1", json={"make": "RAV4", "price": 10000})
print("PATCH /car/1:", response.json())
 
# Test GET request again to see the updated car
response = requests.get(BASE + "car/1")
print("GET /car/1:", response.json())
 
# Test DELETE request to delete the car
response = requests.delete(BASE + "car/1")
print("DELETE /car/1:", response.status_code)
 
# Test GET request again to see if the car is deleted
response = requests.get(BASE + "car/1")
if response.status_code == 404:
    print("GET /car/1: car not found (as expected)")
else:
    print("GET /car/1:", response.json())