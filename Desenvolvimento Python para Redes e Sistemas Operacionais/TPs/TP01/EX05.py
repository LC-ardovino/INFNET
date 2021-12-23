#Escreva um programa que indique se um arquivo existe ou não. Caso exista, indique se é realmente um arquivo ou não.

import os
import sys

arquivo = input("Indique o nome do arquivo:")
caminho = os.path.abspath(arquivo)

if(os.path.exists(caminho)):
  print("O arquivo existe")
else:
  print("O arquivo não existe")
  sys.exit()

if os.path.isfile(arquivo):
  print("O dado fornecido é um arquivo e ele existe! ")

