from menu import exibir_menu
from contato import cadastrar_contato
from listagem import listar_contatos
from buscar import buscar_contato

arquivo_agenda = input("Informe o nome do arquivo:")
print("******************\n")
while True:
    exibir_menu()
    print("******************\n")
    opcao = int(input("Selecione a opção desejada (digite 9 para sair):"))
    print("******************\n")
    if opcao == 1:
        print("Cadastro de novo usuário.")
        nome = input("Nome:")
        telefone = input("Telefone:")
        email = input("Email:")
        cadastrar_contato(arquivo_agenda, nome, telefone, email)
        print(f"\nContato {nome} cadastrado com sucesso.")
        print("******************\n")
    elif opcao == 2:
        print("Listar todos os contatos.")
        listar_contatos(arquivo_agenda)
        print("**********************************\n")
    elif opcao == 3:
        print("Buscar contato.")
        busca = input("Informe o parâmetro de busca: ")
        buscar_contato(busca, arquivo_agenda)
        print("**********************************\n")
    elif opcao == 9:
        break
    else:
        print("Opção inválida.")
        print("**********************************\n")