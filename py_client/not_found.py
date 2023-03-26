import json
import requests

endpoint = "http://localhost:8000/api/products/1232332323"

response = requests.get(
    endpoint,
)
print(response.json())
