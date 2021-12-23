#Escreva um programa que obtenha um nome de um arquivo texto do usuário e crie um processo para executar o programa do sistema Windows bloco de notas (notepad) para abrir o arquivo.

import subprocess,sys

def cria_arquivo():
    nome = str(input("Digite o nome do arquivo:"))
    file = open(f"{nome}.txt", "w")
    file.write("This is my notepad!")
    file.close()


def abre_arquivo():
    arquivo = str(input("Digite o nome do arquivo que deseja abrir:"))
    print(subprocess.run(["notepad", f"{arquivo}.txt"]))


def main():
    print("1-Criar arquivo notepad\n2-Abrir arquivo notepad\n3-Fechar programa")
    while True:
        opção = int(input("Escolha uma opção:"))
        if opção == 1:
            cria_arquivo()
        elif opção == 2:
            abre_arquivo()
        elif opção == 3:
            sys.exit()
        else:
            print("Opção inválida")

main()