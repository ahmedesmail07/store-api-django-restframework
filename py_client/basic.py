import requests

endpoint = "https://www.facebook.com"  # Url Path
response = requests.get(endpoint)  # HTTP Get Request

print(response.text)  # Print The HTML content of the endpoint that refer to facebook

# API => JSON
# HTTP REQUEST => HTML

print(response.json())  # Print The JSON content of the endpoint that refer to facebook
print(response.status_code)  # Returns the actual status code in this case it will ==200
