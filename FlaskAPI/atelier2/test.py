from urllib import response
import requests

#definit la base de l'url
BASE = "http://127.0.0.1:5000/"

#Envoie une requete get a l'url /helloword
response= requests.get(BASE + "helloword")

#Affiche la reponse json de l'api
print(response.json())