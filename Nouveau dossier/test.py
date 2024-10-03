# -*- coding: utf-8 -*-
import requests

BASE = "http://127.0.0.1:5000/"

# D�finir un jeton d'authentification pour tester les requ�tes
TOKEN = "secrettoken123"  # Remplacez par un jeton valide

# Ajouter un en-t�te d'authentification avec le jeton
headers = {"Authorization": f"Bearer {TOKEN}"}

# Tester la requ�te GET sur la ressource Student avec ID 1
response = requests.get(BASE + "student/1", headers=headers)
print("GET Student 1:", response.json())

# Tester la requ�te PUT pour ajouter un nouvel �tudiant
response = requests.put(BASE + "student/1", json={"name": "John Doe", "age": 22, "grade": 85.5}, headers=headers)
print("PUT Student 1:", response.json())

# Tester la requ�te PUT pour ajouter un nouvel �tudiant
response = requests.put(BASE + "student/2", json={"name": "John Doe", "grade": 85.5}, headers=headers)
print("PUT Student 2:", response.json())


# Tester la requ�te GET sur la ressource Student avec ID 1 apr�s l'ajout
response = requests.get(BASE + "student/1", headers=headers)
print("GET Student 1:", response.json())

# Tester la requ�te DELETE pour supprimer l'�tudiant avec ID 1
response = requests.delete(BASE + "student/1", headers=headers)
print("DELETE Student 1:", response.status_code)

# Tester la requ�te GET sur la ressource Student avec ID 1 apr�s la suppression
response = requests.get(BASE + "student/1", headers=headers)
print("GET Student 1:", response.status_code)
