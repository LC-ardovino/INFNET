# Escreva uma função que receba uma string e um número inteiro x e rotacione a string x posições para a
# esquerda. Assuma que a string tem pelo menos x caracteres. Isto é, utilizando como entradas a
# string “aeiou” e o inteiro 3, o resultado da sua função deve ser “ouaei”.


def rotacionando(palavra, numero):
    Lfirst = palavra[0:numero]
    Lsecond = palavra[numero:]
    rotacionada = Lsecond + Lfirst
    print(f"Rotacionando a string {palavra} {numero} posições para a esquerda, iremos obter a nova string {rotacionada}.")

#Programa Principal

palavra = str(input("Digite uma palavra:"))
numero = int(input("Informe um número:"))
if numero >= len(palavra):
    print("Número inválido.")
    quit()
rotacionando(palavra,numero)