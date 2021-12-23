import requests
from bs4 import BeautifulSoup

url = "https://www.gta.ufrj.br/grad/06_1/wap/"

# Usando requests
html = requests.get(url+"index.html").text
soup = BeautifulSoup(html,"lxml")
print(soup)

