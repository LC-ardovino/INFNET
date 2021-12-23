import multiprocessing

def funcProcess(i):
    print(f"Olá mundo da thread {i}!")

if __name__ == "__main__":
    p0 = multiprocessing.Process(target=funcProcess, args=(0,))
    p0.start() # Inicia processo 0

    p1 = multiprocessing.Process(target=funcProcess, args=(1,))
    p1.start() # Inicia processo 1

    p0.join() # espera processo 0
    p1.join() # espera processo 1

    input("Digite qualquer coisa para sair:")






