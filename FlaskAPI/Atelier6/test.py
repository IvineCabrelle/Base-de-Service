import requests

BASE_URL = "http://127.0.0.1:5000/"  

HEADERS = {'Content-Type': 'application/json'}

# Fonction pour obtenir le jeton d'authentification
def get_auth_token():
    url = BASE_URL + '/auth'  # Endpoint où l'authentification est gérée
    response = requests.post(url, json={'username': 'your_username', 'password': 'your_password'}, headers=HEADERS)
    data = response.json()
    return data['access_token']

# Obtenir le jeton d'authentification
token = get_auth_token()
HEADERS['Authorization'] = 'Bearer ' + token

# Tester la requête GET sur la ressource Product avec ID 1
def test_get_product():
    
    url = BASE_URL + '/product/1'
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        print('GET Product with ID 1:', response.json())
    elif response.status_code == 404:
        print('Product with ID 1 not found.')

# Tester la requête PUT pour ajouter un nouveau produit
def test_add_product():
    url = BASE_URL + '/product/1'
    data = {'name': 'Product 1', 'price': 19.99}
    response = requests.put(url, json=data, headers=HEADERS)
    if response.status_code == 201:
        print('PUT Product:', response.json())
    elif response.status_code == 400:
        print('Failed to add product. Product may already exist.')

# Tester la requête GET sur la ressource Product avec ID 1 après l'ajout
def test_get_product_after_add():
    url = BASE_URL + '/product/1'
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        print('GET Product after PUT:', response.json())
    elif response.status_code == 404:
        print('Product with ID 1 not found after adding.')

# Tester la requête DELETE pour supprimer le produit avec ID 1
def test_delete_product():
    url = BASE_URL + '/product/1'
    response = requests.delete(url, headers=HEADERS)
    if response.status_code == 204:
        print('DELETE Product:', response.status_code)
    elif response.status_code == 404:
        print('Failed to delete product. Product with ID 1 not found.')

# Tester la requête GET sur la ressource Product avec ID 1 après la suppression
def test_get_product_after_delete():
    url = BASE_URL + '/product/1'
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 404:
        print('GET Product after DELETE:', response.status_code)
    elif response.status_code == 200:
        print('Product with ID 1 still exists after deletion.')

# Exécution des tests
def run_tests():
    print('Running tests...')
    test_get_product()
    test_add_product()
    test_get_product_after_add()
    test_delete_product()
    test_get_product_after_delete()

if __name__ == '__main__':
    run_tests()
