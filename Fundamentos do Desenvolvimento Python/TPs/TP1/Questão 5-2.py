#Dada uma tupla, retorne 2 tuplas onde cada uma representa uma metade da tupla original.

def metade(tupla_nomes):
    lista = list(tupla_nomes)
    A = lista[:len(lista)//2]
    B = lista[len(lista)//2:]
    novo_A=tuple(A)
    novo_B=tuple(B)
    print(novo_A)
    print(novo_B)

#PROGRAMA PRINCIPAL

tupla_nomes = ("luiz","eduardo","vitória","júlia","marcos","carlos")

metade(tupla_nomes)
