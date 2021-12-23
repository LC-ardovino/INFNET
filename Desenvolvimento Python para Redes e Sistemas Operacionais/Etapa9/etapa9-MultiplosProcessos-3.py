import multiprocessing, time, random

def somaProc(q1,q2):
    lista = q1.get()
    soma = 0
    for i in lista:
        soma = soma + i
    q2.put(soma)


if __name__ == "__main__":
    N = int(input("Entre com o tamanho do vetor:"))

    # Captura tempo inicial
    t_inicio = float(time.time())

    #Gera lista com valores aleatórios
    lista = []
    for i in range(N):
        lista.append(random.randint(-50,51))

    NProc = 8
    q_entrada = multiprocessing.Queue()

    q_saida = multiprocessing.Queue()

    lista_proc = []

    for i in range(NProc):
        ini = i + int(N/NProc)
        fim = (i + 1) * int(N / NProc)

        q_entrada.put(lista[ini:fim])
        p = multiprocessing.Process(target=somaProc, args=(q_entrada,q_saida,))
        p.start()
        lista_proc.append(p)

    for p in lista_proc:
        p.join()

    soma = 0
    for i in range(0,NProc):
        soma = soma + q_saida.get()
    # Captura tempo final
    t_fim = float(time.time())

    #Imprime o resultado e o tempo de execução
    print(f"Soma: {soma}")
    print(f"Tempo total: {t_fim - t_inicio}")