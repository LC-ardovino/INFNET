
def cadastrar_contato(arquivo_agenda, nome, telefone, email):
    """
    Solicita um nome, telefone, email, um arquivo e cadastra um novo contato
    :return:
    """

    #Abre o arquivo em modo append para escrever ao seu final
    agenda = open(arquivo_agenda, "a")
    #Escrevemos, na agenda, os dados do contato e damos um retorno
    agenda.write(f"{nome}; {telefone}; {email}\r")
    #Fecha o arquivo
    agenda.close()





