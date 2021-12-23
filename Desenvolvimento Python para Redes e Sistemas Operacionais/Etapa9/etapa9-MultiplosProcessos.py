import multiprocessing
import time, random

N=int(input("Entre com o tamanho do vetor:"))

# Captura tempo inicial
t_inicio=float(time.time())

# Gera lista com valores aleatórios
lista=[]
for i in range(N):
    lista.append(random.randint(-50,51))

# Faz o cálculo da soma dos valores do vetor/lista
soma = 0
for i in lista:
    soma = soma +i

#Captura tempo final
t_fim=float(time.time())

#Imprime o resultado e o tempo de execução
print(f"Soma:{soma}")
print(f"Tempo total:{t_fim-t_inicio}")

