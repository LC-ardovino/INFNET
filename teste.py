import socket

udp_c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
endereço = socket.gethostbyname('localhost')
porta =  9991
destino = (endereço, porta)



print('Esperando receber na porta', porta, '...')
dado = 'Cliente Solicitando ao servidor a quantidade total e disponível de armazenamento do disco principal...'
udp_c.sendto(dado.encode('utf-8'), destino)

(msg, cliente) = udp_c.recvfrom(1024)
print(cliente, msg.decode('utf-8'))

udp_c.close()
input('Pressione qualquer tecla para sair...')