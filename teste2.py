import socket, psutil, os

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
endereço = socket.gethostbyname('localhost')
porta =  9991
origem = (endereço, porta)
udp.bind(origem)


path = os.getcwd()
armazemento = psutil.disk_usage(path)

livre = psutil.disk_usage(path).free
total = psutil.disk_usage(path).total
gb_total = total /1024/1024/1024
gb_livre = livre /1024/1024/1024
resposta = f'O computador tem {(round(gb_total, 2))} GB de capacidade de armazenamento e {(round(gb_livre, 2))} GB livre.'


print('Esperando receber na porta', porta, '...')
print("Conectado a:", str(origem))
(msg, cliente) = udp.recvfrom(1024)
print(cliente, msg.decode('utf-8'))

udp.sendto(resposta.encode('utf-8'), origem )
udp.close()
input('Pressione qualquer tecla para sair...')
