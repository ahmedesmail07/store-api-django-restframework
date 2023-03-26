import requests

endpoint = "http://localhost:8000/api/products/create-list/"

response = requests.get(
    endpoint,
)
print(response.json())


# Returns All The DB Content
