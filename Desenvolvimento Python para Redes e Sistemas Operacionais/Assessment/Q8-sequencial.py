#sequencialmente (sem concorrência);

import random

vetorA = []
vetorB = []

def fatorial(n):
    fat = n
    for i in range(n - 1, 1, -1):
        fat = fat * i
    vetorB.append(fat)

def main():
    vetor = int(input("Digite o tamanho do vetor:"))
    for i in range(1,vetor+1):
        vet = random.randint(1,10)
        vetorA.append(vet)
    for i in vetorA:
        fatorial(i)

    print("Vetor original:")
    print(vetorA)
    print("Novo vetor:")
    print(vetorB)

main()