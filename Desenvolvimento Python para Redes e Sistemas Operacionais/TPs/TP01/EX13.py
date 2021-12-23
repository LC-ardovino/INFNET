#Usando o módulo ‘subprocess’ de Python, crie um processo externo e imprima o PID dele.
import subprocess
import psutil

processo = subprocess.Popen('calc')
pid = processo.pid
p = psutil.Process(pid)

print(f"O processo:{p.name()} possui o PID {pid}.")


