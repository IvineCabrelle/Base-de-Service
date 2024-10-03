import requests
 
BASE = "http://127.0.0.1:5000/"
 
# Test PUT request to create a new course
response = requests.put(BASE + "course/1", json={"name": "Flask Basics", "description": "Introduction to Flask", "duration": 5})
print("PUT /course/1:", response.json())
 
# Test GET request to retrieve the course
response = requests.get(BASE + "course/1")
print("GET /course/1:", response.json())
 3
# Test PATCH request to update the course
response = requests.patch(BASE + "course/1", json={"name": "Flask Advanced", "duration": 10})
print("PATCH /course/1:", response.json())
 
# Test GET request again to see the updated course
response = requests.get(BASE + "course/1")
print("GET /course/1:", response.json())
 
# Test DELETE request to delete the course
response = requests.delete(BASE + "course/1")
print("DELETE /course/1:", response.status_code)
 
# Test GET request again to see if the course is deleted
response = requests.get(BASE + "course/1")
if response.status_code == 404:
    print("GET /course/1: Course not found (as expected)")
else:
    print("GET /course/1:", response.json())