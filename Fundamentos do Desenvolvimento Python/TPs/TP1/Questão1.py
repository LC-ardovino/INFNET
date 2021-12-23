# Escreva uma função em Python que some todos os números ímpares de 1 até um dado N, inclusive. O número
# N deve ser obtido do usuário. Ao final, escreva o valor do resultado desta soma.

def soma_numeros_impares(N):
    soma = 0
    for i in range(1, N+1):
        if i % 2 == 1:
            soma += i
    print(f"A soma dos números ímpares de 1 a {N} é {soma}")


#Programa principal:

N = int(input("Digite o número inteiro desejado: "))

soma_numeros_impares(N)