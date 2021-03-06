#Protocolo TCP
#A cada 2 segundos, requisita ao servidor as informações de memória e CPU e Exibe as informações formatadas na tela conforme as atualizações;

import socket,pickle
import time

def imprime(l):
    texto = ''
    for i in l:
        texto = texto + '{:>8.2f}'.format(i)
    print(texto)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Tenta se conectar ao servidor
    s.connect((socket.gethostname(), 9999))
    msg = ' '
    print('{:>8}'.format('%CPU') + '{:>8}'.format('%MEM'))
    for i in range(10):
        # Envia mensagem vazia apenas para indicar a requisição
        s.send(msg.encode('ascii'))
        bytes = s.recv(1024)
        # Converte os bytes para lista
        lista = pickle.loads(bytes)
        imprime(lista)
        time.sleep(2)
    msg = 'fim'
    s.send(msg.encode('ascii'))
except Exception as erro:
  print(str(erro))
s.close()

input("Pressione qualquer tecla para sair...")
