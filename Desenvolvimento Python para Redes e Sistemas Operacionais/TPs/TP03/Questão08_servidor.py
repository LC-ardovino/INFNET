import socket,psutil
#python Questão08_servidor.py
HOST = socket.gethostname()  # Endereco IP do Servidor
PORT = 9991  # Porta que o Servidor está esperando
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)
print('Esperando receber na porta', PORT, '...')

(msg, cliente) = udp.recvfrom(1024)



print("Quantidade total de armazenamento:")
print(msg.decode('ascii'),'GB')
(msg2, cliente1) = udp.recvfrom(1024)
print("Quantidade livre de armazenamento:")
print(msg2.decode('ascii'),'GB')

udp.close()
input('Pressione qualquer tecla para sair...')