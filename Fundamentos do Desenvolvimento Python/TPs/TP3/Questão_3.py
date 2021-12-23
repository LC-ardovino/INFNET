#Escreva um programa em Python que leia um vetor de 10 palavras e mostre-as na ordem inversa de leitura.

vetor = []
palavra1 = str(input("Digite uma palavra:"))
vetor.append(palavra1)
palavra2 = str(input("Digite uma palavra:"))
vetor.append(palavra2)
palavra3 = str(input("Digite uma palavra:"))
vetor.append(palavra3)
palavra4 = str(input("Digite uma palavra:"))
vetor.append(palavra4)
palavra5 = str(input("Digite uma palavra:"))
vetor.append(palavra5)

novo_vetor = list(reversed(vetor))
print(novo_vetor)