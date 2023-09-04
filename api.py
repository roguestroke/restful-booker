import requests


response = requests.get("http://localhost:3001/booking")
print(response.text)