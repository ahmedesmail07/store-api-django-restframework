import requests

endpoint = "https://www.facebook.com"  # Url Path
response = requests.get(endpoint)  # HTTP Get Request

print(response.text)  # Print The HTML content of the endpoint that refer to facebook
