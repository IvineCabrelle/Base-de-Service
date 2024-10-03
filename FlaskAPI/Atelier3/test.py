import requests
BASE = "http://127.0.0.1:5000/"

#Envoie une requete get a l'url /helloword
response= requests.get(BASE + "helloword")
print ('Helloworld', response.json())

response= requests.get(BASE + "goodbyewold")
print ('goodbyeworld', response.json())

response= requests.get(BASE + "users")
print ('Users', response.json())

response= requests.get(BASE + "user/1")
print ('User 1', response.json())

response= requests.get(BASE + "user/999")
print ('User 999', response.json())