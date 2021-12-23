#Obtenha, usando requests ou urllib, a página HTML https://fgopassos.github.io/pagina_exemplo/estadosCentroOeste.html dentro de seu programa em Python e faça:
#Imprima o conteúdo referente apenas à tabela apresentada na página indicada.

import requests
from bs4 import BeautifulSoup

url = 'https://fgopassos.github.io/pagina_exemplo/estadosCentroOeste.html'#URL da página
requisiçao = requests.get(url)#requisição é uma variável criada para acessar a página web, pede uma requisição
requisiçao.encoding = requisiçao.apparent_encoding#obtém o formato de codificação, UTF-8
soup = BeautifulSoup(requisiçao.text,'lxml')#cria uma árvore de analise do código HTML do site.
tabela = soup.html.body.find('div', {'class': 'tabela'})#obtém apenas do HTML a parte referente a tabela

print(tabela.get_text())#printa a tabela em texto