#Usando Python, faça o que se pede (código):
#Crie uma lista vazia;
#Adicione os elementos: 1, 2, 3, 4 e 5,  usando append();
#Imprima a lista;
#Agora, remova os elementos 3 e 6 (não esqueça de checar se eles estão na lista);
#Imprima a lista modificada;
#Imprima também o tamanho da lista usando a função len();
#Altere o valor do último elemento para 6 e imprima a lista modificada.

lista = []
lista.append(1)
lista.append(2)
lista.append(3)
lista.append(4)
lista.append(5)
print(lista)
print(f"O tamanho da lista é {len(lista)}.")
if 6 or 3 in lista:
    if 6 in lista:
        lista.remove(6)
    lista.remove(3)
    print(lista)
    print(f"O tamanho da lista modificada é {len(lista)}.")

lista.pop()
lista.append(6)
print(lista)