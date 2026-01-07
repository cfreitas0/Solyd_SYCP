import json

import requests

URL = "https://brasilapi.com.br/api/banks/v1"

resposta = requests.get(URL)

bancos = json.loads(resposta.text) # PARSING DE JSON PARA PYTHON


for banco in bancos:
    print('Nome: ', banco['fullName'])
    print('Código: ', banco['code'])
    print('Ispb: ', banco['ispb'],'\n')
    print('========================================')

print('Total de bancos:', len(bancos), 'Instituições')
print('========================================')