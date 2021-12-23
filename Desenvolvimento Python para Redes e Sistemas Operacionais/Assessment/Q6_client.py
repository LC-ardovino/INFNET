#Escreva um programa cliente e servidor sobre TCP em Python em que:
#O cliente envia para o servidor o nome de um diretório e recebe a lista de arquivos (apenas arquivos) existente nele.

import socket,sys

pasta = 'C:\\Users\\DESKTOP\\PycharmProjects\\Infnet\\Desenvolvimento Python para Redes e Sistemas Operacionais\\Assessment'


target_host = socket.gethostname()
target_port = 9999
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

diret = input("Digite o caminho do diretório:")

client.connect((target_host, target_port))
client.send(diret.encode("utf-8"))
response = client.recv(4096)
print("\n")
print("Listando arquivos do diretório: ", target_host, target_port)
print(response.decode('utf-8'))
print("\n")
client.close()

if __name__ == "__main__":
    sys.exit()
