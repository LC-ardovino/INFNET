import socket, random
HOST = ''
PORT = 9999 # Porta que o Servidor esta
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)
print('Esperando receber na porta', PORT, '...')
while True:
    (msg, cliente) = udp.recvfrom(1024)
#print(cliente, msg.decode('ascii'))
# Decodifica mensagem em UTF-8:
    if '$' == msg.decode('utf-8'):
        print("Fechando conexao com", str(cliente), "...")
        cliente.close()
        break
    elif '?' in msg.decode('utf-8'):
        resp = random.randint(0,1)
        msg = "Sim\n"
    if resp == 0:
        msg = "Nao\n"
    else:
        msg = "Ok... " + msg.decode('utf-8')
    udp.sendto (msg.encode('utf-8'), cliente)
input("Pressione qualquer tecla para sair...")
udp.close()