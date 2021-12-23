#Teste todos os 3 programas da questão 8, capture os tempos de execução deles e compare-os, explicando os resultados de tempos. Varie o valor de N em 1.000.000, 5000.000, 10.000.000 (ou escolha números maiores ou melhores de acordo com a velocidade de processamento do computador utilizado para testes).

import multiprocessing,random,time

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
  q = multiprocessing.Queue()

  resposta = []

  listaDeProcessos = []

  for i in range(thread_num):
    start = i * int(list_size // thread_num)

    end = (i + 1) * int(list_size // thread_num)

    p = multiprocessing.Process(target=fatorialProcesso, args=(vetor,q, start,end))

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
  t_inicial = float(time.time())
  for i in range(1, vetor + 1):
    vet = random.randint(1, 10)
    VETOR_A.append(vet)
  t_fim = float(time.time())
  list_size = len(VETOR_A)

  print("Vetor original:")
  print(VETOR_A)
  print("Novo vetor:")
  print(comProcessos(VETOR_A,list_size,n_threads))
  print(f"Tempo total {t_fim - t_inicial}")