
#Exemplo de um programa que mostra as informações dos sockets do tipo “inet”:
import time
import psutil
import socket

#for i in psutil.net_connections():
    #print(i)

#obtendo informações de processos usando redes.
def exercicio1():
    a = psutil.net_io_counters().bytes_sent
    b = psutil.net_io_counters().bytes_recv
    c = psutil.net_io_counters().packets_sent
    d = psutil.net_io_counters().packets_recv

    time.sleep(1)

    vazao_s = psutil.net_io_counters().bytes_sent - a
    vazao_r = psutil.net_io_counters().bytes_recv - b

    a = a/1024/1024/1024
    b = b/1024/1024/1024

    print(f"Gbytes enviados:{a}")
    print(f"Gbytes recebidos:{b}")
    print(f"Pacotes enviados: {c}")
    print(f"Pacotes recebidos: {d}")
    print("")
    print(f"Vazão de bytes enviados: {vazao_s}")
    print(f"Vazão de bytes recebidos: {vazao_r}")


def obtem_nome_familia(familia):
    if familia == socket.AF_INET:
        return ("IPv4")
    elif familia == socket.AF_INET6:
        return ("IPv6")
    elif familia == socket.AF_UNIX:
        return ("Unix")
    else:
        return ("-")

def obtem_tipo_socket(tipo):
    if tipo == socket.SOCK_STREAM:
        return("TCP")
    elif tipo == socket.SOCK_DGRAM:
        return("UDP")
    elif tipo == socket.SOCK_RAW:
        return("IP")
    else:
        return("-")

for i in psutil.pids():
    p = psutil.Process(i)
    conn = p.connections()
    if len(conn) > 0:
        if conn[0].status.ljust(13) != "ESTABLISHED":
            endl = conn[0].laddr.ip.ljust(11)
            portl = str(conn[0].laddr.port).ljust(5)
            endr = conn[0].laddr.ip.ljust(13)
            portr = str(conn[0].laddr.port).ljust(5)
        print(str(i).ljust(5),"End. Tipo Status Endereço Local. Endereço Remoto Porta R. ")
        print("    ",obtem_nome_familia(conn[0].family),""+ obtem_tipo_socket(conn[0].type)," "+ conn[0].status.ljust(13),endl,portl," "+ endr," "+portr)


exercicio1()




