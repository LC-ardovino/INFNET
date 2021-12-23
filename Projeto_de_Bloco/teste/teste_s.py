import socket
import threading
import sys
import psutil
import os
import sched
import time
import ipaddress

bind_ip = socket.gethostname()
bind_port = 9991
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def start_server():
    server.bind((bind_ip, bind_port))
    server.listen(5)
    print("[*] Escutando no endereço: %s:%d" % (bind_ip, bind_port))



def staggered_scheeduling():

    start = time.time()
    print("Iniciando as chamadas escalonadas.")
    scheduler = sched.scheduler(time.time, time.sleep)
    scheduler.enter(1, 1, get_network_interfaces_details(), ())
    scheduler.enter(2, 1, list_process, ("python3",))
    scheduler.run()
    end = time.time()
    total = abs(end - start)
    data = ("Finalizando as chamadas escalonadas..." + (f" Tempo total: {total:.0f} segundos"))
    return data

def get_network_interfaces_details(interface):
    data = []
    data.append("IPv4: " + psutil.net_if_addrs()[interface][0][1] + " | " + "IPv6: " + psutil.net_if_addrs()[interface][1][1] + " | " + "Máscara: " + psutil.net_if_addrs()[interface][0][2])
    data_string = " ".join((data))
    return data_string



def handle_client(client_socket):
    request = client_socket.recv(1024)
    print("[*] Recebido: %s" % request)
    request_data = request.decode('utf-8')
    data = request_data.split(",")
    if data[0] == "1":
        data = staggered_scheeduling()
        client_socket.send(bytes(data, 'utf-8'))
    elif data[0] == "2":
        interfaces = get_network_interfaces_details()
        client_socket.send(bytes(interfaces, 'utf-8'))
        sys.exit()
    print(client_socket.getpeername())
    client_socket.close()

def main():
    start_server()
    while True:
        client, addr = server.accept()
        print("[*] Nova conexão realizada pelo cliente %s:%d" % (addr[0], addr[1]))
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()
main()
if __name__ == "__main__":
    sys.exit(main())