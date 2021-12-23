#Escreva um programa em Python que leia um arquivo texto e apresente na tela o seu conteúdo reverso.
#caminho atual = C:\\Users\\DESKTOP\\PycharmProjects\\Infnet\\Desenvolvimento Python para Redes e Sistemas Operacionais\\Assessment
import os
import sys

caminho = input("Digite um caminho:")
lista = os.listdir(caminho)
while True:
    arq = str(input("Digite o nome do arquivo:")+".txt")
    if arq in lista:
        with open(arq,"r") as arquivo:
            texto = arquivo.read()
            texto_reverso = texto[::-1]
        print(texto_reverso)
        sys.exit()
    else:
        print("Arquivo inválido:")