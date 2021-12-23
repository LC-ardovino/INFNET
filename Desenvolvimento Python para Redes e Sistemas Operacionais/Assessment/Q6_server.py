#O servidor recebe a requisição do cliente, captura o nome dos arquivos no diretório em questão e envia a resposta ao cliente de volta.

import os,socket,sys,threading

bind_ip = socket.gethostname()
bind_port = 9999
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def start_server():
    server.bind((bind_ip, bind_port))
    server.listen(5)
    print("[*] Escutando no endereço: %s:%d" % (bind_ip, bind_port))

def lista_arquivos(data):
    lista = []
    for diretorio, subpastas, arquivos in os.walk(data):
        for arquivo in arquivos:
            arq = (os.path.join(arquivo))
            lista.append(arq)
    return f"{lista[0]}\n{lista[1]}\n{lista[2]}\n{lista[3]}\n{lista[4]}\n{lista[5]}\n{lista[6]}\n{lista[7]}\n{lista[8]}"

def handle_client(client_socket):
    request = client_socket.recv(1024)
    print("[*] Recebido: %s" % request)
    request_data = request.decode('utf-8')
    print(request_data)
    files = lista_arquivos(request_data)
    client_socket.send(files.encode('utf-8'))


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


