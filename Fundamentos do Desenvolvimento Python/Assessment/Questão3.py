#Usando o Thonny, escreva uma função em Python chamada potencia. Esta função deve obter como
# argumentos dois números inteiros, A e B, e calcular AB usando multiplicações
# sucessivas (não use a função de python math.pow) e retornar o resultado da operação. Depois, crie
# um programa em Python que obtenha dois números inteiros do usuário e indique o resultado de AB
# usando a função.
def potencia(A,B):
    potencia = 1
    cont = 1
    while cont<= B:
        potencia = potencia *A
        cont+=1
    print(f"O valor da potenciação é:{potencia}")

A = int(input("Digite o valor da base:"))
B = int(input("Digite o valor do expoente:"))
potencia(A,B)