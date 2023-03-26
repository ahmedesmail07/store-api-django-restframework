import requests
import json

endpoint = "http://localhost:8000/api/products/create/"

response = requests.post(
    endpoint,
)
print(response.json())
