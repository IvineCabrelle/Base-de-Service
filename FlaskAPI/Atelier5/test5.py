import requests

BASE="http://127.0.0.1:5000/"

TOKEN="secrettoken123"

headers={"Authorization":f"Bearer{TOKEN}"}

response=requests.get(BASE+"student/1",headers=headers)

print("GET Student 1:", response.json())

response=requests.put(BASE+"student/1",{"name":"John Doe","age":22,"grade":85.5},headers=headers)

print("PUT Student 1:", response.json())

response=requests.get(BASE+"student/1",headers=headers)
print("GET Student 1:", response.json())

response=requests.delete(BASE+"student/1",headers=headers)
print("DELETE Student 1:", response.status_code)

response=requests.get(BASE+"student/1",headers=headers)
print("GET Student 1:", response.status_code)



