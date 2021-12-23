#Obtenha, usando requests ou urllib, o conteúdo sobre as PyLadies no link http://brasil.pyladies.com/about e:
#Conte todas as palavras no corpo da página, e indique quais palavras apareceram apenas uma vez.
import requests
from bs4 import BeautifulSoup as bs
import re#Este módulo fornece operações de correspondência de expressão regular semelhantes às encontradas em Perl.
from collections import Counter#Módulo que permitirá eu criar um dicionário a partir da lista de palavras e contar a quantidade de elementos repetidos


url = 'http://brasil.pyladies.com/about/'#obtenho a url da página
requisiçao = requests.get(url)#requisição é uma variável criada para acessar a página web, pede uma requisição
requisiçao.encoding = requisiçao.apparent_encoding#obtém o formato de codificação, UTF-8
soup = bs(requisiçao.text,'lxml')#cria uma árvore de analise do código HTML do site.

palavras = 0#variável para guardar o número de palavras
ladies = 0#variável para guardar o número de ladies que apareceu
lista_palavras = []# lista de palavras
apenas_um = []# lista com as palavras que apareceram 1 vez

for item in soup.html.body.article.find_all('div'):#vai passar pelo código HTML mas apenas onde tem as palavras
    lista_palavras = [re.sub('\W+', '', word).lower()#adiciona a lista as palavras do texto separado por virgula
for word in item.text.split()]
    palavras = len(lista_palavras)#conta a quantidade de palavras na lista_palavras


dicionario = dict(Counter(lista_palavras))#cria um dicionário junto com o número de palavras que cada aparece

ladies = dicionario['ladies']#substitui o valor 0 pelo número de vezes que ladies aparece(dados no dicionário)

for key, value in dicionario.items():#no for ele analisa cada chave e valor do dicionário, caso o número de vezes que a palavra apareceu seja 1 ele adiciona a palavra a lista apenas_um
    if value == 1:
        apenas_um.append(key)

#print(f"O total de palavras é {palavras}")#printa a quantidade de palavras da página.
#print(f"Aparecem apenas {len(apenas_um)} palavras uma vez.")#printa a quantidade de palavras que só foram escritas 1 vez
#print(f"Ladies apareceu apenas {ladies} vezes.")#printa a quantidade de palavras que só apareceram 1 vez