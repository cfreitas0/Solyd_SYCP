
import requests

from bs4 import BeautifulSoup

url_carros = "https://www.comprecar.com.br/buscar?cidade=355030&pp=120"

def buscar_marca(url):
  try:
    resposta = requests.get(url)
    if resposta.status_code == 200:
      return resposta.text
    else:
      print('Erro ao fazer Req.', )
  except Exception as error:
    print('Erro => : ', error)


def parsing(resposta_html):
  try:
    soup = BeautifulSoup(resposta, 'html.parser')
    return soup
  except Exception as error:
    print('Erro ao fazer o Parsing html => ', error)


def pegar_links(soup):
  card_main = soup.find("ul", class_="row vehicle-list-row")
  card_links = card_main.find_all("a")

  links = []
  for card in card_links:
    link = card['href']
    links.append(link)

  return links 


resposta = buscar_marca(url_carros)
if resposta:
  soup = parsing(resposta)
  if soup:
    links = pegar_links(soup)


  print()
  print(links,'\n')
  print()