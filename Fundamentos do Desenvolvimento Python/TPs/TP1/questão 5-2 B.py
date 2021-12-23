tupla_nomes = ("luiz","eduardo","vitória","júlia","marcos","carlos")
lista = list(tupla_nomes)
A = lista[:len(lista) // 2]
B = lista[len(lista) // 2:]
novo_A = tuple(A)
novo_B = tuple(B)
print(novo_A)
print(novo_B)
