#Escreva uma função em Python que leia uma tupla contendo números inteiros, retorne uma lista
# contendo somente os números ímpares e uma nova tupla contendo somente os elementos
# nas posições pares.

def lendo(tupla_inteiros):
    lista = list(tupla_inteiros)
    impares = []
    pares = []
    for i in lista:
        if i%2 ==1:
            impares.append(i)
    for i in lista:
        if i%2 ==0:
            pares.append(i)
    tupla_nova = tuple(pares)
    print(f"Lista dos valores ímpares:{impares}")
    print(f"A tupla dos valores pares é:{tupla_nova}")


#Programa Principal

tupla_inteiros = (1,2,3,4,5,6,7,8,9,10)
lendo(tupla_inteiros)