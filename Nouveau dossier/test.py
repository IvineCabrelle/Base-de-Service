# -*- coding: utf-8 -*-
import requests

BASE = "http://127.0.0.1:5000/"

# Définir un jeton d'authentification pour tester les requêtes
TOKEN = "secrettoken123"  # Remplacez par un jeton valide

# Ajouter un en-tête d'authentification avec le jeton
headers = {"Authorization": f"Bearer {TOKEN}"}

# Tester la requête GET sur la ressource Student avec ID 1
response = requests.get(BASE + "student/1", headers=headers)
print("GET Student 1:", response.json())

# Tester la requête PUT pour ajouter un nouvel étudiant
response = requests.put(BASE + "student/1", json={"name": "John Doe", "age": 22, "grade": 85.5}, headers=headers)
print("PUT Student 1:", response.json())

# Tester la requête PUT pour ajouter un nouvel étudiant
response = requests.put(BASE + "student/2", json={"name": "John Doe", "grade": 85.5}, headers=headers)
print("PUT Student 2:", response.json())


# Tester la requête GET sur la ressource Student avec ID 1 après l'ajout
response = requests.get(BASE + "student/1", headers=headers)
print("GET Student 1:", response.json())

# Tester la requête DELETE pour supprimer l'étudiant avec ID 1
response = requests.delete(BASE + "student/1", headers=headers)
print("DELETE Student 1:", response.status_code)

# Tester la requête GET sur la ressource Student avec ID 1 après la suppression
response = requests.get(BASE + "student/1", headers=headers)
print("GET Student 1:", response.status_code)
