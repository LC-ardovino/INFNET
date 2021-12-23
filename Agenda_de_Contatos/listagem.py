
def listar_contatos(arquivo_agenda):
  ''' Lista nome, telefone e e-mail de cada contato na agenda definida pelo caminho arquivo_agenda '''
  # Abre a agenda para leitura dos dados:
  agenda = open(arquivo_agenda, 'r')
  # Lê todo o conteúdo da agenda
  contatos = agenda.read() # contatos é uma string contendo todos os dados da agenda
  # Cria uma lista onde cada elemento da lista é uma das linhas da agenda
  contatos = contatos.splitlines() # contatos é uma lista onde cada elemento é um dos contatos.
  # Fecha a agenda
  agenda.close()
  # Percorre a lista de contatos
  print(f"{'Contato':<30}\t{'Telefone':>20}\t{'E-mail':<30}")
  for contato in contatos:
    # Queremos imprimir nome, telefone e e-mail com alguma formatação
    # Para isso, nós vamos quebrar a linha que contém esses dados, usando a vírgula como separador
    # Isto transformará o contato em uma lista contendo 3 elementos: nome, telefone e-mail.
    contato = contato.split(';') # contato é uma lista contendo 3 elementos: nome, telefone, e-mail
    # contato[0] é o nome. contato[1] é o telefone. contato[2] é o e-mail.
    nome = contato[0]
    telefone = contato[1]
    email = contato[2]
    print(f"{nome:<30}\t{telefone:>20}\t{email:<30}")




