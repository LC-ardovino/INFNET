#1-Dada uma tupla e um elemento, verifique se o elemento existe na tupla e retorne o indice do mesmo.

def verificador(elemento_vogais, elemento_numero):
    vogais_tupla = ('a','e','i','o','u')
    if elemento_vogais in vogais_tupla:
        print(f"A vogal fornecida está na Tupla. ")
    else:
        print(f"A vogal fornecida não está na Tupla. ")
    numero_tupla = (0,1,2,3,4,5,6,7,8,9,10)
    if elemento_numero in numero_tupla:
        print(f"O número {elemento_numero} está na Tupla.")
    else:
        print(f"O número {elemento_numero} não está na Tupla.")

#PROGRAMA PRINCIPAL

elemento_vogais = str(input("Digite uma vogal: ")).lower()
elemento_numero = int(input("Digite um número inteiro de 0-10: "))

verificador(elemento_vogais, elemento_numero)