import requests


endpoint = "http://localhost:8000/api/products/1/update"

data = {"title": "Hello", "price": "120.00"}
response = requests.put(endpoint, json=data)
print(response.json())
