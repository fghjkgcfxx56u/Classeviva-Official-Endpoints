import requests
import json
from classeviva.variabili import intestazione
from classeviva.collegamenti import Collegamenti as C

def id_():
    with open('username.txt', 'r') as f:
        id__ = f.read()
    return id__

def password_():
    with open('password.txt', 'r') as f:
        user__ = f.read()
    return user__

response = requests.post(
    C.accesso,
    data=f'{{"ident": null, "pass": "{password_()}", "uid": "{id_()}"}}',
    headers=intestazione
)
token = response.json()["token"]
print(response.json())
print(token)


i_ = intestazione.copy()
i_["Z-Auth-Token"] = token
'''
print(requests.get(
    "https://web.spaggiari.eu/rest/v1/students/{}/subjects".format(id_().removeprefix("S")),
    headers=i_
).json())
print(requests.get(
    "https://web.spaggiari.eu/rest/v1/students/{}/agenda/{}/20220301/20220602".format(
        id_().removeprefix("S"),
        "AGNT"
    ),
    headers=i_
).json())
'''
print(json.dumps(requests.get(
    "https://web.spaggiari.eu/rest/v1/students/{}/schoolbooks".format(
        id_().removeprefix("S"),
    ),
    headers=i_
).json(), indent=4))