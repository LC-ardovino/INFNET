#Indique uma maneira de criar um processo externo ao seu programa usando o módulo ‘os’ e usando o módulo ‘subprocess’ de Python. Dê um exemplo de cada.

import subprocess
import os


def usando_OS():
    #Executando a calculadora usando o módulo OS
    os.system("calc")

def usando_SUBPROCESS():
    #Executando o notepad usando o módulo subprocess
    print(subprocess.run(["notepad", "arq_texto.txt"]))

usando_OS()
usando_SUBPROCESS()

