
import json

import requests

URL_NAME = "https://brasilapi.com.br/api/pix/v1/participants"

resposta = requests.get(URL_NAME)

pixs = json.loads(resposta.text) # PARSING DE JSON PARA PYTHON

print(len(pixs)) 

for pix in pixs:
    print(pix['nome'], pix['ispb'])