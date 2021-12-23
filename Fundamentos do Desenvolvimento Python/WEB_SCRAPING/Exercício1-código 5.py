import requests

url = "http://climatedataapi.worldbank.org/climateweb/rest/v1/country/mavg/tas/1980/1999/BRA.csv"

CSV = requests.get(url).text
linhas = CSV.splitlines()

for i in range(1,len(linhas)):
    colunas = linhas[1].split(',')
    soma = 0
    print(colunas)
    for c in range(4, len(colunas)):
        soma = soma + float(colunas[c])
    print(colunas[0],soma/(len(colunas)-4))