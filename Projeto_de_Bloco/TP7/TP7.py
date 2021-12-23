#Crie uma ou mais funções que retornem ou apresentem as seguintes informações de redes: IP, gateway, máscara de subrede.

import psutil
import time


def item1():
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
    print("----------------------------------------------------------------------------------------------------------"*2)


#Crie uma ou mais funções que retornem ou apresentem as seguintes informações de redes: Uso de dados de rede por interface.

def item2():
    io_status = psutil.net_io_counters(pernic=True)
    nomes = []
    for i in io_status:
        nomes.append(str(i))
    for j in nomes:
        print(j)
        print("\t" + str(io_status[j]))
    for i in range(4):
        time.sleep(1)
        io_status = psutil.net_io_counters(pernic=True)
    for j in nomes:
        print(j)
        print("\t" + str(io_status[j]))






#Crie uma ou mais funções que retornem ou apresentem as seguintes informações de redes: Uso de dados de rede por processos.

def item3():
    a = psutil.net_io_counters().bytes_sent
    b = psutil.net_io_counters().bytes_recv
    c = psutil.net_io_counters().packets_sent
    d = psutil.net_io_counters().packets_recv

    time.sleep(1)

    vazao_s = psutil.net_io_counters().bytes_sent - a
    vazao_r = psutil.net_io_counters().bytes_recv - b

    a = a/1024/1024/1024
    b = b/1024/1024/1024
    #print("")
    #print(f"Informações do uso de dados por processos na Rede:")
    #print(f"Gbytes enviados:{a}")
    #print(f"Gbytes recebidos:{b}")
    #print(f"Pacotes enviados: {c}")
    #print(f"Pacotes recebidos: {d}")
    #print("")
    #print(f"Vazão de bytes enviados: {vazao_s}")
    #print(f"Vazão de bytes recebidos: {vazao_r}")
    text = (f"Informações do uso e dados por processos na Rede:\nGbytes enviados:{a}\nGbytes recebidos:{b}\nPacotes enviados: {c}\nPacotes recebidos: {d}\nVazão de bytes enviados: {vazao_s}\nVazão de bytes recebidos: {vazao_r}")
    print(text)


item1()
#item2()
#item3()


