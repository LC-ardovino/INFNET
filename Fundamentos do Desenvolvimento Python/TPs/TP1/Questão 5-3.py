#Dada uma tupla e um elemento, elimine esse elemento da tupla.

def elimina(tuplas_indices):
    lista = list(tuplas_indices)
    removivel = int(input("Digite um número de 0-10, que se queira remover da Tupla:"))
    if removivel>10 or removivel<0:
        print("Número inválido.")
        quit()
    lista.remove(removivel)
    nova_tupla = tuple(lista)
    print(nova_tupla)

#Programa Principal

tuplas_indices = (0,1,2,3,4,5,6,7,8,9,10)

elimina(tuplas_indices)