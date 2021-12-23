lista = []
while True:
    frases = str(input(f'Escreva uma frase: '))
    lista.append(frases)
    if frases == 'sair':
        print(lista)
        print(lista.count('eu'))
        break