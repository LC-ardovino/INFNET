import psutil

nome = input("Entre com o nome do processo a ser buscado: ")
ip = psutil.pids()
lista_pid = []
for i in ip:
    p = psutil.Process(i)
    if p.name() == nome:
        lista_pid.append(str(i))

if len(lista_pid) > 0:
    print(f"O(s) PID(s) de {nome} são:")
    print(','.join(lista_pid))
else:
    print(nome,"não está executando no momento.")