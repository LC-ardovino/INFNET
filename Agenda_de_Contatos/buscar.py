def buscar_contato(busca, arquivo_agenda):
    agenda = open(arquivo_agenda, 'r')
    contatos = agenda.read()
    contatos = contatos.splitlines()
    agenda.close()
    resultados = 0
    for contato in contatos:
        contato = contato.split(';')
        nome, telefone, email = contato[0], contato[1], contato[2]
        if busca in nome or busca in telefone or busca in email:
            print(f"{nome:<30}\t{telefone:>20}\t{email:<30}")
            resultados += 1
        print(f"\n{resultados} resultado(s) encontado(s)")

