#O servidor repetidamente recebe a requisição do cliente, captura a informação da quantidade total e disponível de memória há no servidor e envia a resposta ao cliente de volta.

import socket,psutil,sys

HOST = socket.gethostname()  # Endereco IP do Servidor
PORT = 9991  # Porta que o Servidor está esperando
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)
print('Esperando receber na porta', PORT, '...')

def memoria_disponivel():
    memoria = psutil.disk_usage('C:\\')
    memoria_disponivel = round((memoria[2]) / 1073741824)
    memoria_disponivel = str(memoria_disponivel)
    return memoria_disponivel

def memoria_total():
    memoria = psutil.disk_usage('C:\\')
    memoria_total = round((memoria[0]) / 1073741824)
    memoria_total = str(memoria_total)
    return(memoria_total)

while True:
    (msg, cliente) = udp.recvfrom(1024)
    print("Opção:",msg)
    resp = msg.decode("utf-8")
    if resp == "1":
        dados = memoria_total()
        byte = dados.encode("utf-8")
        udp.sendto(byte,cliente)
    elif resp == '2':
        dados = memoria_disponivel()
        byte = dados.encode("utf-8")
        udp.sendto(byte, cliente)
    else:
        sys.exit()
udp.close()