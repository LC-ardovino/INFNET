import socket, psutil
#python Questão08_cliente.py
HOST = socket.gethostname()  # Endereco IP do Servidor
PORT = 9991                  # Porta que o Servidor está esperando
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)

memoria = psutil.disk_usage('C:\\')
memoria_total = round((memoria[0])/1073741824)
memoria_total = str(memoria_total)

memoria_disponivel = round((memoria[2])/1073741824)
memoria_disponivel = str(memoria_disponivel)

udp.sendto(memoria_total.encode('utf-8'), dest)
udp.sendto(memoria_disponivel.encode('utf-8'), dest)


udp.close()