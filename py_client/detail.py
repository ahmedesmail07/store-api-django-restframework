import requests


endpoint = "http://localhost:8000/api/products/1"

response = requests.get(
    endpoint,
)
print(response.json())
# response = requests.post(
#     endpoint,
#     json={
#         "title": "Wow Great Testing",
#         "content": "This is the best test wow thanks",
#         "price": "123",
#     },
# )
