#Escreva um programa em Python, usando o módulo ‘psutil’, que imprima o tempo de CPU em segundos por núcleo.

import psutil, time

psutil.cpu_times(percpu = True)
for i in range(10):
    time.sleep(0.1)
    print(psutil.cpu_times(percpu = True))