#Escreva um programa em Python que leia um vetor de números de tamanho t. Leia t previamente. Em seguida, faça seu programa verificar quantos números iguais a 0 existem nele.

from random import choices, sample

cont = 0
tamanho = int(input("Digite o tamanho do vetor:"))
valores = range(0,10)
print(f"A lista a seguir possui {tamanho} elementos aleatórios de 0 a 10.")
lista = (choices(valores,k = tamanho))
print(lista)
iguais_0 = lista.count(0)
print(f"A quantidade de vezes que o número 0 apareceu na lista foi:{iguais_0}")

