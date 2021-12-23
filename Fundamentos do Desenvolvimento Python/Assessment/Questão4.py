#Escreva um programa em Python que leia um vetor de 5 números inteiros e o apresente na ordem
# inversa. Imprima o vetor no final. Use listas.

n1= int(input("Digite um número inteiro:"))
n2= int(input("Digite um número inteiro:"))
n3= int(input("Digite um número inteiro:"))
n4= int(input("Digite um número inteiro:"))
n5= int(input("Digite um número inteiro:"))

lista =[n1,n2,n3,n4,n5]
lista.reverse()
print(lista)