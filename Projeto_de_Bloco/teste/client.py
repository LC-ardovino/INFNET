import socket
import sys

target_host = socket.gethostname()
target_port = 9991
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def server_staggered_scheeduling():
    client.connect((target_host, target_port))
    client.send("1".encode('utf-8'))
    response = client.recv(4096)
    print("\n")
    print("Listando chamadas escalonadas no servidor: ", target_host, target_port)
    print(response.decode('utf-8'))
    print("\n")
    client.close()

def get_network_interfaces():
    client.connect((target_host, target_port))
    client.send("2".encode('utf-8'))
    response = client.recv(4096)
    print("\n")
    print("Listando as interfaces de rede disponíveis no servidor: " , target_host, target_port)
    print(response.decode('utf-8'))
    print("\n")
    client.close()

def menu():
    print("""
    1 - Executar chamadas escalonadas
    2 - Listar interfaces de rede disponíveis
    3 - Sair
    """)

def main():
    menu()
    while True:
        try:
            choice = int(input("Escolha uma opção: "))
            if choice == 1:
                server_staggered_scheeduling()
            elif choice == 2:
                get_network_interfaces()
            elif choice == 3:
                sys.exit()
            else:
                print("Opção inválida")
        except ValueError:
            print("Opção inválida")


main()
if __name__ == "__main__":
    sys.exit(main())
