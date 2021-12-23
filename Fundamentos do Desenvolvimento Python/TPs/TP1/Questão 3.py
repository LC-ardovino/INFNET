#Escreva uma função em Python que calcule o fatorial de um dado número N usando um for. O fatorial
# de N=0 é um. O fatorial de N é (para N > 0): N x (N-1) x (N-2) x … x 3 x 2 x 1. Por exemplo, para N=5 o
# fatorial é: 5 x 4 x 3 x 2 x 1 = 120. Se N for negativo, exiba uma mensagem indicando que não é possível
# calcular seu fatorial.

def fatorial(N):
    fat = 1

    print(f"O fatorial de {N}! é:", end='')
    for n in range(N, 0, -1):
        fat *= n
        print(f'{n}{"x" if n > 1 else "="}', end='')
    print(fat)

#PROGRAMA PRINCIPAL

N = int(input("Digite um numero inteiro que queira fatorar: "))
if N<0:
    print("O valor fornecido é impossível de fatorar.")
fatorial(N)