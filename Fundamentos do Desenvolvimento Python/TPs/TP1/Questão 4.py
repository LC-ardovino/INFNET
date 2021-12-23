#Escreva um programa em Python que calcule o fatorial de um dado número N usando um while. Use as mesmas
# especificações do item anterior.

def fatorial(N):
    cont = 1
    fat = 1
    while cont<= N:
        fat *= cont
        cont += 1
    print(f"O fatorial de {N}! é:", end='')
    for n in range(N, 0, -1):
        print(f'{n}{"x" if n > 1 else "="}', end='')
    print(fat)

#PROGRAMA PRINCIPAL

N = int(input("Digite um numero inteiro que queira fatorar: "))
if N<0:
    print("O valor fornecido é impossível de fatorar.")
fatorial(N)