#Dada uma tupla, retorne uma nova tupla com todos os elementos invertidos.

def invertendo(tuplas_indices):
    lista = list(tuplas_indices)
    nova_tupla = tuple(reversed(lista))
    print(nova_tupla)

#PROGRAMA PRINCIPAL

tuplas_indices = (0,1,2,3,4,5,6,7,8,9,10)
invertendo(tuplas_indices)