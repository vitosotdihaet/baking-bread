import requests
import json

with open("tests/signup.json") as fl:
    data = json.load(fl)

x = requests.post("http://localhost:5000/signup", json=data)
print(x)