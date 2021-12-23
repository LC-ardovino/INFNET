#Escreva um programa em Python que leia diversas frases até a palavra “Sair” ser digitada. Indique quais frases apresentam a palavra “eu”.


def analisa_eu(lista,frase):
    if "eu" in frase:
        lista.append(frase)


def main():
    lista = []
    while True:
        frase = str(input("Digite uma frase: "))
        if frase == 'sair':
            print(lista)
            break
        analisa_eu(lista,frase)

main()
