import requests

# Simple demo call to the API
r = requests.get("http://localhost:8000/")
print(r.json())
