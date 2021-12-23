#Criar uma ou mais funções que retornem ou apresentem informações sobre diretórios e arquivos. Tais informações
# podem ser qualquer uma que você achar relevante disponível no módulo ‘os’ e ‘psutil’ de Python, como nome,
# tamanho, localização, data de criação, data de modificação, tipo, etc.



def mostra_dados_arquivos():
    import os
    import time
    # Obtém lista de arquivos e diretórios do diretório corrente:
    lista = os.listdir()
    dic = {}  # cria um dicionário
    lista_dir = []

    for i in lista:
        if os.path.isfile(i):
            # Cria uma lista para cada arquivo.Esta lista contém o tamanho, data de criação e data de modificação.
            dic[i] = []
            dic[i].append(os.stat(i).st_size)  # Tamanho
            dic[i].append(os.stat(i).st_atime)  # Tempo de criação
            dic[i].append(os.stat(i).st_mtime)  # Tempo de modificação
    for d in lista:
        if os.path.isdir(d):
            lista_dir.append(d)
    print(f'Diretórios: {lista_dir}')

    titulo = '{:11}'.format("Tamanho")  # 10 caracteres +1 de espaço
    # Concatenar com 25 caracteres +2 de espaço
    titulo = titulo + '{:27}'.format('Data de Modificação')
    # Concatenar com 25 caracteres +2 de espaço
    titulo = titulo + '{:27}'.format('Data de Criação')
    titulo = titulo + 'Nome'
    print(titulo)
    for i in dic:
        kb = dic[i][0] / 1024
        tamanho = '{:10}'.format(str('{:.2f}'.format(kb) + 'KB'))
        print(tamanho, time.ctime(dic[i][2]), "", time.ctime(dic[i][1]), "", i)




mostra_dados_arquivos()
