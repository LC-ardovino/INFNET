#Escreva um programa que mostre a quantidade de bytes (em KB) de cada arquivo em um diretório.

import os
arquivo = input("Indique o nome do arquivo:")
os.stat(arquivo)
bytes = os.stat(arquivo).st_size
KB = bytes/1024
print(f"O arquivo {arquivo} possui {KB} KB.")