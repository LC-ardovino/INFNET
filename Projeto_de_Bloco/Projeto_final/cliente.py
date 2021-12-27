import socket
import sys

def Processo_do_sistema():
    target_host = socket.gethostname()
    target_port = 9999
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect((target_host, target_port))
    client.send("1".encode('utf-8'))
    response = client.recv(4096)
    print("\n")
    print("Analisando processos do sistema: ", target_host, target_port)
    titulo = '{:^7}'.format("PID")
    titulo = titulo + '{:^11}'.format("# Threads")
    titulo = titulo + '{:^26}'.format("Criação")
    titulo = titulo + '{:^9}'.format("T. Usu.")
    titulo = titulo + '{:^9}'.format("T. Sis.")
    titulo = titulo + '{:^12}'.format("Mem. (%)")
    titulo = titulo + '{:^12}'.format("RSS")
    titulo = titulo + '{:^12}'.format("VMS")
    titulo = titulo + " Executável"
    print(titulo)

    print(response.decode('utf-8'))
    print("\n")
    client.close()


def Diretorios_e_Arquivos():
    target_host = socket.gethostname()
    target_port = 9999
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect((target_host, target_port))
    client.send("2".encode('utf-8'))
    response = client.recv(4096)
    print("\n")
    print("Listando os Diretórios e arquivos: ", target_host, target_port)
    print(response.decode('utf-8'))
    print("\n")
    client.close()

def Chamadas_escalonadas():
    target_host = socket.gethostname()
    target_port = 9999
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect((target_host, target_port))
    client.send("4".encode('utf-8'))
    response = client.recv(4096)
    proc = client.recv(4096)
    arq = client.recv(4096)
    print("\n")
    print("Contando tempo das chamadas escalonadas no servidor: ", target_host, target_port)
    print(arq.decode("utf-8"))
    print("\n")
    print(proc.decode("utf-8"))
    print("\n")
    print(response.decode('utf-8'))
    print("\n")
    client.close()

def percentuais():
    target_host = socket.gethostname()
    target_port = 9999
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect((target_host, target_port))
    client.send("3".encode('utf-8'))
    cpu = client.recv(4096)
    memoria = client.recv(4096)
    disco = client.recv(4096)
    print("\n")
    print("Listando os percentuais da máquina: ", target_host, target_port)
    print(cpu.decode('utf-8'))
    print("\n")
    print(memoria.decode('utf-8'))
    print("\n")
    print(disco.decode('utf-8'))
    client.close()

def info_maquina():
    target_host = socket.gethostname()
    target_port = 9999
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect((target_host, target_port))
    client.send("5".encode('utf-8'))
    response = client.recv(4096)
    print("\n")
    print("Listando informações da máquina: ", target_host, target_port)
    print(response.decode('utf-8'))
    print("\n")
    client.close()

def redes():
    target_host = socket.gethostname()
    target_port = 9999
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    client.connect((target_host, target_port))
    client.send("6".encode('utf-8'))
    ip_string = input("Entre com o ip alvo: ")
    client.send(ip_string.encode('utf-8'))
    resposta = client.recv(4096)
    print("Listando informações da máquina: ", target_host, target_port)
    print(resposta.decode('utf-8'))
    print("\n")
    client.close()

def dados_redes():
    target_host = socket.gethostname()
    target_port = 9999
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect((target_host, target_port))
    client.send("7".encode('utf-8'))
    response = client.recv(4096)
    print("\n")
    print("Listando dados de rede por processos: ", target_host, target_port)
    print(response.decode('utf-8'))
    print("\n")
    client.close()

def dados_interface():
    target_host = socket.gethostname()
    target_port = 9999
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect((target_host, target_port))
    client.send("8".encode('utf-8'))
    response = client.recv(4096)
    print("\n")
    print("Listando dados de rede por interface: ", target_host, target_port)
    print(response.decode('utf-8'))
    print("\n")
    client.close()

def IP_gateway_mascara():
    target_host = socket.gethostname()
    target_port = 9999
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect((target_host, target_port))
    client.send("9".encode('utf-8'))
    response = client.recv(4096)
    print("\n")
    print("Listando IP, Gateway e máscara: ", target_host, target_port)
    print(response.decode('utf-8'))
    print("\n")
    client.close()

def menu():
    print("""
    1 - Executar Processos_do_Sistema
    2 - Listar Diretórios e arquivos
    3 - Informações sobre percentual de CPU, DISK e memoria
    4-  Chamadas escalonadas
    5-  Informações sobre a máquina
    6-  Informações sobre as portas dos diferentes IPs obtidos nessa sub-rede.(TP06)
    7-  Uso de dados de rede por processos.
    8-  Uso de dados de rede por interface.
    9-  Informação de rede:IP, gateway, máscara de subrede.
    0-  Sair
    """)

def main():
    menu()

    while True:

        try:
            choice = int(input("Escolha uma opção: "))
            if choice == 1:
                Processo_do_sistema()
            elif choice == 2:
                Diretorios_e_Arquivos()
            elif choice == 3:
                percentuais()
            elif choice == 4:
                Chamadas_escalonadas()
            elif choice == 5:
                info_maquina()
            elif choice == 6:
                redes()
            elif choice == 7:
                dados_redes()
            elif choice == 8:
                dados_interface()
            elif choice == 9:
                IP_gateway_mascara()
            elif choice == 0:
                sys.exit()
            else:
                print("Opção inválida")
        except ValueError:
            print("Opção inválida")


main()
if __name__ == "__main__":
    sys.exit(main())


