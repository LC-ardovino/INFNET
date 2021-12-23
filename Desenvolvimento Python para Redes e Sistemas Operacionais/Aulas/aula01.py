#sets/conjuntos
#Posso adicionar qualquer valor que seja único

S = {'red','green',13,True}
print(S)

#Transformando uma estrutura em set:

elemento = ('abc')
conjunto = set(elemento)
print(conjunto)

#Organizando os elementos de uma lista em um conjunto:

lista = [1,2,3,4,5,6]
conjunto = set(lista)
print(conjunto)

#Para adicionar uma string a um set, usa-se .update e .add qualquer tipo de valor, mas só 1 por vez:
conjunto = {1, 2, 3, 4, 5}
conjunto.update("6","fgde")
print(conjunto)

#Fazendo a união de dois conjuntos:
A = {'red','green','blue'}
B = {'yellow','red','orange'}
print(A|B)

#Printa os elementos de A que n se repetem em B:
print(A-B)

#Diferença simetrica entre A e B:
print(A^B)







