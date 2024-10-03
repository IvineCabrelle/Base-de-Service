import requests

BASE="http://127.0.0.1:5000/"

response=requests.get(BASE+"video/1")
print("GET Video 1:", response.json())

response=requests.put(BASE+"video/1",{"name":"Video 1","views":100,"likes":10})

print("PUT Video 1:", response.json())

response=requests.get(BASE+"video/1")
print("GET Video 1:", response.json())

response=requests.delete(BASE+"video/1")
print("DELETE Video 1:", response.status_code)

response=requests.get(BASE+"video/1")
print("GET Video 1:", response.status_code)



