import requests
import json
from time import sleep

with open("signup.json") as fl:
    signup_data = json.load(fl)

response = requests.post("http://localhost:5000/login", json=signup_data) # logs in with signup_data
print(response, response.content)

parsed = json.loads(response.content)

token = parsed['access_token']

response = requests.get("http://localhost:5000/user-access", headers = {'Authorization': 'Bearer {}'.format(token)}) # makes get request with a token
print(response, response.content)

response = requests.get("http://localhost:5000/admin-access", headers = {'Authorization': 'Bearer {}'.format(token)})
print(response, response.content)

