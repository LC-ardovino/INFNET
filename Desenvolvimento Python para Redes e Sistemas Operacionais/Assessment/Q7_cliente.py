#Escreva um programa cliente e servidor sobre UDP em Python que:
#O cliente envia para o servidor o pedido de obtenção da quantidade total e disponível de memória no servidor e espera receber a resposta durante 5s. Caso passem os 5s, faça seu programa cliente tentar novamente mais 5 vezes (ainda esperando 5s a resposta) antes de desistir.

import socket

def menu():
    print("1-informar a memória total:\n"
          "2-Informar a memória disponível:")

def main():
    menu()
    while True:
        HOST = socket.gethostname()  # Endereco IP do Servidor
        PORT = 9991  # Porta que o Servidor está esperando
        udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        dest = (HOST, PORT)
        resp = str(input("Digite a opção desejada:"))
        udp.sendto(resp.encode("utf-8"),dest)
        try:
            data, server = udp.recvfrom(1024)
            mem_total = data.decode(encoding='utf-8') + 'GB'
            print(mem_total)
        except:
            print("Time out")

    udp.close()

main()
