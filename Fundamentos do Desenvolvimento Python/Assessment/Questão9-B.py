#Escreva um programa que obtenha do usuário uma sigla do estado da região
# Centro-Oeste e apresenta suas informações correspondentes na tabela. O resultado deve
# apresentar apenas o conteúdo, sem formatação. Ou seja, as tags não devem aparecer. Não esqueça
# de checar se a sigla pertence à região.
import requests
from bs4 import BeautifulSoup

url = 'https://fgopassos.github.io/pagina_exemplo/estadosCentroOeste.html'#URL da página
requisiçao = requests.get(url)#requisição é uma variável criada para acessar a página web, pede uma requisição
requisiçao.encoding = requisiçao.apparent_encoding#obtém o formato de codificação, UTF-8
soup = BeautifulSoup(requisiçao.text,'lxml')#cria uma árvore de analise do código HTML do site.
linhas = soup.html.body.article.find_all('div', {'class': 'linha'})#cria uma árvore de analise do código HTML do site, mas apenas com a classe linha(possui os estados e as informações da tabela)

terminou = False#parametro para finalizar o loop while
estados = ['df', 'mt', 'go', 'ms']#lista com os estados do site
usr_choice = str#cria uma função que vai receber dados em string

while not terminou:
    sigla = str(input("Digite a sigla do estado do Centro Oeste:"))#input para receber o estado que será printado no final
    for l in linhas:#passará por cada elemento em linha
        estado = l.find_all('div', {'class': 'celula'})[0].text#vai guardar na variável estado as siglas dos estados que tem em linhas
        if sigla == estado.lower():#Analisa se a sigla passada tá em minúscula e se ela estiver ela vai continuar
            usr_choice = l.text#Guarda as informações referentes ao estado na variável usr_choice
            terminou = True#finaliza o Loop
        if sigla == estado.upper():
            usr_choice = l.text
            terminou = True

print(usr_choice)#Printa as informações