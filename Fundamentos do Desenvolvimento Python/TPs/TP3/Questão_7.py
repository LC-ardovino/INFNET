#Escreva um programa em Python que realiza operações de inclusão e remoção em listas. Seu programa deve perguntar ao usuário qual operação deseja fazer: (código)
#Mostrar lista;
#Incluir elemento;
#Remover elemento;
#Apagar todos os elementos da lista.


def exibe_menu():
    print("1-Mostrar lista.")
    print("2-Incluir elemento.")
    print("3-Remover elemento.")
    print("4-Apagar todos os elementos da lista.")

def adiciona(lista):
    elemento = input("Digite o item que se deseja incluir na lista:")
    lista.append(elemento)

def remove(lista):
    removendo = input("Digite o elemento que se deseja remover da lista:")
    if removendo in lista:
        lista.remove(removendo)
    else:
        print("Elemento inválido.")

def limpando(lista):
    print("Limpando lista....")
    lista.clear()

def main():
    lista = []
    while True:
        exibe_menu()
        opção = int(input("Escolha uma das opções:"))
        if opção == 1:
           print(lista)
        elif opção == 2:
            adiciona(lista)
        elif opção == 3:
            remove(lista)
        elif opção == 4:
            limpando(lista)
        else:
            print("Opção inválida.")

main()