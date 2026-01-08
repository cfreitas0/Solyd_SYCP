import json

import requests

URL = "https://brasilapi.com.br/api/banks/v1"

def requisicao(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            return resposta.text
    except:
        print('Erro na conexão', url)


def parsing(textoResposta):
    try:
        return json.loads(textoResposta) # PARSING DE JSON PARA PYTHON
    except:
        print('Erro ao fazer Parsing')





