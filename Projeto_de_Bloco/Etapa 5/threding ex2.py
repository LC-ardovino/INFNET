import sched
import threading
import time

scheduler = sched.scheduler(time.time, time.sleep)

# Seta um contador global a ser modificado por cada thread
contador = 0


def aumenta_contador(nome):
    global contador
    print('EVENTO:', time.ctime(), nome)
    contador += 1
    print('Contador atual:', contador)


print('Inicio:', time.ctime())
e1 = scheduler.enter(2, 1, aumenta_contador, ('E1',))
e2 = scheduler.enter(3, 1, aumenta_contador, ('E2',))

# Inicia a thread para executar os eventos
t = threading.Thread(target=scheduler.run)
t.start()

# Volta para a thread principal, cancela o primeiro evento com a informação no e1
scheduler.cancel(e1)

# Esperar que o escalonador termine de executar o restante das threads
t.join()

print('Contador final:', contador)