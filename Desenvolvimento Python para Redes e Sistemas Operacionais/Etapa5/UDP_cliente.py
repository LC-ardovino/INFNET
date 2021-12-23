import socket

HOST = socket.gethostname()  # Endereco IP do Servidor
PORT = 5000                  # Porta que o Servidor está esperando
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)
msg = input("Entre com a mensagem:\n")
udp.sendto(msg.encode('ascii'), dest)
udp.close()
