import psutil

#Lista todos os processos que estão executando na máquina:

print(psutil.pids())

#Indica se determinado processo existe de acordo com o pid

pid = int(input("Informe um pid válido:"))
print(psutil.pid_exists(pid))
