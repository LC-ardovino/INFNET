#Escreva um programa que imprima apenas o caminho absoluto de um arquivo com nome relativo. A impressão não deve conter o nome do arquivo, apenas o caminho.

import os
caminho = os.path.abspath("EX07.py")
print(os.path.split(caminho))