import requests

url = "http://climatedataapi.worldbank.org/climateweb/rest/v1/country/mavg/tas/1980/1999/BRA.csv"

#Usando requests
csv = requests.get(url).text
linhas = csv.splitlines()
for lin in linhas:
    colunas = lin.split(',')#extrai valores separados por vírgula