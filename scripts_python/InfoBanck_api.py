import json

import requests

URL_NAME = "https://brasilapi.com.br/api/banks/v1"

resposta = requests.get(URL_NAME)

bancks = json.loads(resposta.text) # PARSING DE JSON PARA PYTHON

print(len(bancks)) 

for banck in bancks:
    print(banck['fullName'], banck['code'])