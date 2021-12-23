import requests
from bs4 import BeautifulSoup

# 241 é o código da cidade do Rio de Janeiro no site
url = "http://www.cptec.inpe.br/cidades/tempo/241"

requisicao = requests.get(url)

# Testando se a conexão funcionou
if requisicao.status_code != 200:
  requisicao.raise_for_status()

#requisicao.encoding = 'utf-8' # Mudar o enconding (acentuação)
html = requisicao.text
soup = BeautifulSoup(html, "lxml")

for div_previsao in soup.find_all('div', class_='previsao'):
    d = {}
    for div_prev in div_previsao.find_all('div', class_='prev'):
        for c in div_prev.find_all('div', class_='c2'):
            d[c.contents[0]] = c.b.text
        for c in div_prev.find_all('div', class_='c3'):
            d[c.contents[0]] = c.b.text
        for c in div_prev.find_all('div', class_='c4'):
            d[c.contents[0]] = c.b.text
        for c in div_prev.find_all('div', class_='c5'):
            d[c.contents[0]] = c.b.text
        for c in div_prev.find_all('div', class_='c6'):
            d[c.contents[0]] = c.b.text
        print(d)