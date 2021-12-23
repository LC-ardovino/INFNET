import os
import subprocess
import time, sched
import psutil


def processo():
    print("luiz")
def arquivo():
    print("carlos")






def escalonamento_principal():
    start = time.time()
    print("Iniciando as chamadas escalonadas.")
    scheduler = sched.scheduler(time.time, time.sleep)
    scheduler.enter(1, 1, processo)
    scheduler.enter(2, 1, arquivo)
    scheduler.run()
    end = time.time()
    total = round(abs(end - start))

    data = ("Finalizando as chamadas escalonadas..." + (f" Tempo total: {total} segundos"))
    print(data)

escalonamento_principal()

