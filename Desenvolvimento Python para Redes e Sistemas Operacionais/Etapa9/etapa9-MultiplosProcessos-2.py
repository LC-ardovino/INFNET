import threading, time, random

def somaThread(lista,soma_parcial,id):
    soma = 0
    for i in lista:
        soma = soma + i
    soma_parcial[id] = soma

N = int(input("Entre com o tamanho do vetor:"))

# Gera lista com valores aleatórios
lista = []
for i in range(N):
    lista.append(random.randint(-50,51))

Nthreads = 4 # Número de threads a ser criado
#Captura tempo inicial
t_inicio = float(time.time())
#Vetor para salvar a soma parcial de cada thread
soma_parcial =Nthreads * [0]

lista_threads = []
for i in range(Nthreads):
    ini = i * int(N/Nthreads)
    fim = (i + 1)*int(N/Nthreads)
    t = threading.Thread(target=somaThread, args=(lista[ini:fim],soma_parcial,i))
    t.start()
    lista_threads.append(t)

for t in lista_threads:
    t.join()

soma = 0
for i in soma_parcial:
    soma = soma + i

t_fim = float(time.time())
print(f"Soma:{soma}")
print(f"Tempo total {t_fim - t_inicio}")