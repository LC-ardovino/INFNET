#Teste todos os 3 programas da questão 8, capture os tempos de execução deles e compare-os, explicando os resultados de tempos. Varie o valor de N em 1.000.000, 5000.000, 10.000.000 (ou escolha números maiores ou melhores de acordo com a velocidade de processamento do computador utilizado para testes).


import random,time

vetorA = []
vetorB = []



def fatorial(n):

    fat = n
    for i in range(n - 1, 1, -1):
        fat = fat * i
    vetorB.append(fat)

def main():
    vetor = int(input("Digite o tamanho do vetor:"))
    t_inicial = float(time.time())
    for i in range(1,vetor+1):
        vet = random.randint(1,10)
        vetorA.append(vet)
    for i in vetorA:
        fatorial(i)

    t_fim = float(time.time())
    print("Vetor original:")
    print(vetorA)
    print("Novo vetor:")
    print(vetorB)
    print(f"Tempo total {t_fim - t_inicial}")
main()