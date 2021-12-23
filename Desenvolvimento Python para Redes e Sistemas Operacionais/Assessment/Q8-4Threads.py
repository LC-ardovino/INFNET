#usando o módulo threading com 4 threads;

import queue,threading,random

def fatorial(n):
  fat = n
  for i in range(n - 1, 1, -1):
    fat = fat * i

  return (fat)


def fatorialProcesso(vetor,q,start,end):
  for item in vetor[start:end]:
    factorial = fatorial(item)
    q.put(factorial)

  return

def comProcessos(vetor,list_size,thread_num):
  q = queue.Queue()

  resposta = []

  listaDeProcessos = []

  for i in range(thread_num):

    start = i * int(list_size // thread_num)

    end = (i + 1) * int(list_size // thread_num)

    p = threading.Thread(target=fatorialProcesso,args=(vetor,q, start,end))

    p.start()

    listaDeProcessos.append(p)

    for p in listaDeProcessos:
      p.join()

  while q.qsize() > 0:
    resposta.append(q.get())

  return resposta


if __name__ == "__main__":
  n_threads = 4
  VETOR_A = []
  vetor = int(input("Digite o tamanho do vetor:"))

  for i in range(1, vetor + 1):
    vet = random.randint(1, 10)
    VETOR_A.append(vet)

  list_size = len(VETOR_A)

  print("Vetor original:")
  print(VETOR_A)
  print("Novo vetor:")
  print(comProcessos(VETOR_A,list_size,n_threads))
