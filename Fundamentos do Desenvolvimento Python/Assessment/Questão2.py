#Usando o Thonny, escreva um programa em Python que some todos os números pares de 1 até um
# dado n, inclusive. O dado n deve ser obtido do usuário. No final, escreva o valor do
# resultado desta soma.

def soma_numeros_impares(N):
    soma = 0
    for i in range(1, N+1):
        if i % 2 == 0:
            soma += i
    print(f"A soma dos números pares de 1 a {N} é {soma}")


#Programa principal:

N = int(input("Digite o número inteiro desejado: "))

soma_numeros_impares(N)