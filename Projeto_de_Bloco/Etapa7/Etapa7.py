import psutil
import time
interfaces = psutil.net_if_addrs()
nomes = []
# Obtém os nomes das interfaces primeiro
for i in interfaces:
    nomes.append(str(i))
status = psutil.net_if_stats()
# Depois, imprimir os valores:
for i in nomes:
    print(i+":")
    print(str(status[i]))
    for j in interfaces[i]:
        print("\t"+str(j))
    print("---------------------------------------"*3)



