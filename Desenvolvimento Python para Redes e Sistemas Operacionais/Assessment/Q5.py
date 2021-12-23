#Seu programa deve somar elemento por elemento de cada arquivo e
# imprimir o resultado na tela. Isto é, o primeiro elemento de a.txt
# deve ser somado ao primeiro elemento de b.txt, segundo elemento de a.txt deve ser
# somado ao segundo elemento de b.txt, e assim sucessivamente. Caso um arquivo tenha mais
# elementos que o outro, os elementos que sobrarem do maior devem ser somados a zero.
# caminho atual = C:\\Users\\DESKTOP\\PycharmProjects\\Infnet\\Desenvolvimento Python para Redes e Sistemas Operacionais\\Assessment
import os

lista1 = []
lista2 = []
caminho = input("Digite um caminho:")
lista = os.listdir(caminho)

def programa(lista,lista1,lista2):
    while True:
        arq = str(input("Digite o nome do primeiro arquivo:")+".txt")
        if arq in lista:
            with open(arq,"r") as arquivo:
                texto = arquivo.read()

        else:
            print("Arquivo 1 inválido.")
            continue

        arq2 = str(input("Digite o nome do segundo arquivo:")+".txt")
        if arq2 in lista:
            with open(arq2,"r") as arquivo:
                texto2 = arquivo.read()

        else:
            print("Arquivo 2 inválido.")
            continue

        lista1.append(texto)
        lista1 = texto.split()
        lista2.append(texto2)
        lista2 = texto2.split()

        for i in range(0,len(lista1)):
            soma = lista1[i] +lista2[i]
            print(soma)
        break
programa(lista,lista1,lista2)
while True:
    resp = str(input("Deseja continuar?S/N").upper())
    if resp == "S":
        programa(lista,lista1,lista2)
    else:
        print("Finalizando programa...")
        break
