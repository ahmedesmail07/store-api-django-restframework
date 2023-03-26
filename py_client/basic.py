import requests

endpoint = "https://www.facebook.com"  # Url Path
response = requests.get(endpoint)  # HTTP Get Request
endpoint_local = "http://127.0.0.1:8000/"
response_loacl = requests.get(endpoint_local)

print(response.text)  # Print The HTML content of the endpoint that refer to facebook
print(
    response.text
)  # Print The HTML content of the endpoint_local that refer to LOCAL HOST
# API => JSON
# HTTP REQUEST => HTML

print(response.json())  # Print The JSON content of the endpoint that refer to facebook
print(response.status_code)  # Returns the actual status code in this case it will ==200
