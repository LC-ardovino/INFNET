import socket, psutil, pickle

#Servidor recebe conexão do cliente e obtém os dados;
#Servidor envia os dados ao cliente e continua esperando por mais requisições.
#O processo servidor termina quando o servidor recebe a mensagem ‘fim’.

socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
porta = 9999
socket_servidor.bind((host, porta))
socket_servidor.listen()
print("Servidor de nome", host, "esperando conexão na porta", porta)
(socket_cliente,addr) = socket_servidor.accept()
print("Conectado a:", str(addr))


while True:
    msg = socket_cliente.recv(4)
    if msg.decode('ascii') == 'fim':
        break
    # Gera a lista de resposta
    resposta = []
    resposta.append(psutil.cpu_percent())
    mem = psutil.virtual_memory()
    mem_percent = mem.used / mem.total
    resposta.append(mem_percent)
    # Prepara a lista para o envio
    bytes_resp = pickle.dumps(resposta)
    # Envia os dados
    socket_cliente.send(bytes_resp)
# Fecha socket do servidor e cliente
socket_cliente.close()
socket_servidor.close()