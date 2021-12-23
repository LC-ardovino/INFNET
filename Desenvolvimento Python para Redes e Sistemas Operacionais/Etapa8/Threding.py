#Threads é um artifício de sistemas operacionais que permite criar novos fluxos de execução de um processo
#Em Python 3, existe um módulo chamado ‘threading’ que permite criar threads. Como você já sabe, thread é um fluxo alternativo de execução de um processo e ele compartilha o mesmo espaço de endereçamento deste processo.
import threading
import time

def thread1(num):#exemplo de criação de duas threads
    print(f"Olá mundo da thread {num}")

#t0 = threading.Thread(target=thread1,args=(0,))
#t0.start()

#t1 = threading.Thread(target=thread1,args=(1,))
#t1.start()

#t0.join() # espera thread 0
#t1.join() # espera thread 1

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#Exemplo de criação de N threads.
#Ao executar o programa a saída pode ser fora de ordem pq as threads operam em paralelo, em alguns computadores isso pode ser mais frequente ou não
def thread2(num):
    print(f"Olá mundo da thread {num}.")

#Nthreads = 4
#lista_threads = []

#for i in range(Nthreads):
#    t = threading.Thread(target=thread2,args=(i,))
#    t.start()
#    lista_threads.append(t)
#for t in lista_threads:
#    t.join()

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#Criando programas sequenciais e paralelos.
#Problema:criar um programa que, dada uma lista de valores fracionários, calcula 10% de cada um deles e substitui o valor antigo da lista por este novo valor.

def sequencial():
    lista = [11,12,13,14,15,16,17,18,19]
    tamanho = len(lista)
    for i in range(tamanho):
        lista[i] = lista[i] * 0.1

    print(lista)

#Código Paralelo(com 2 threats):
def calcPorcent(lista, inicio, fim):
    for i in range(inicio, fim):
        lista[i] = lista[i] * 0.1


lista = [1.3, 10.4, 40.0, 59.87, 33.01, 101.4]
tamanho = len(lista)

t0 = threading.Thread(target=calcPorcent,args=(lista,0,int(tamanho/2)))
t0.start()

t1 = threading.Thread(target=calcPorcent,args=(lista,int(tamanho/2),tamanho))
t1.start()

t0.join() # espera thread 0
t1.join() # espera thread 1


#print(lista)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#Código sequencial 5

N = 1000

# Apenas preenchendo a lista de forma simplificada:
lista = []
for i in range(N):
    lista.append(20)

# Realiza o cálculo
for i in range(N):
    lista[i] = lista[i] * 0.1

# A impressão da lista será comentada, pois ela é muito grande
#print(lista)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#Código 6-paralelo

def calcPorcent(lista,inicio,fim):
    for i in range(inicio,fim):
        lista[i] = lista[i] * 0.1

N = 100000

#Apenas preenchendo de forma simplificada
lista = []
for i in range(N):
    lista.append(20)

Nthreads = 4 # Número de threads a ser criada

lista_threads = []

for i in range(Nthreads):
    ini = i * int(N/Nthreads)
    fim = (i+1) * int(N/Nthreads)
    t = threading.Thread(target=calcPorcent, args=(lista, ini, fim))
    t.start()
    lista_threads.append(t)
for t in lista_threads:
    t.join() # Espera as threads terminarem


#print(lista)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#Código7-Problema + medição do tempo

N = 100000000

#Captura tempo inicial

t_inicio = float(time.time())

#Preenchendo a lista de forma simplificada
lista = []
for i in range(N):
    lista.append(20)

#Realiza o cálculo
for i in range(N):
    lista[i] = lista[i] * 0.1

#Captura o tempo final
t_fim = float(time.time())

#print(f"Tempo total sequencial em segundos:{t_fim-t_inicio}")

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#Código 8
def calcPorcent(lista,inicio,fim):
    for i in range(inicio,fim):
        lista[i] = lista[i] * 0.1

#Captura tempo inicial
t_inicio = float(time.time())

N = 1000000 # Tamanho da lista

#Apenas preenchendo a lista de forma simplificada:
lista = []
for i in range(N):
    lista.append(20)

Nthreads = 4 # Número de threads a ser criado

lista_threads = []
for i in range(Nthreads):
    ini = i * int(N/Nthreads) # início do intervalo da lista
    fim = (i + 1) * int(N/Nthreads) # fim do intervalo da lista
    t = threading.Thread(target=calcPorcent, args=(lista,ini,fim))
    t.start() # inicia thread
    lista_threads.append(t) # guarda a thread

for t in lista_threads:
    t.join() # Espera as threads terminarem

# Captura tempo final
t_fim = float(time.time())
#print(f"Tempo total Paralelo em segundos:{t_fim-t_inicio}")


