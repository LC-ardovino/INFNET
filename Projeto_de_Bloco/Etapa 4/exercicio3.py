import os

lista = os.listdir()

lista_arq = []# lista para guardar os arquivos
lista_dir = []# lista para guardar os diretórios
for i in lista:
    if os.path.isfile(i):
        lista_arq.append(i)
    else:
        lista_dir.append(i)

if len(lista_arq) > 0:#Checa se tem arquivos na lista
    print("Arquivos:")
    for i in lista_arq:
        print("\t"+i)#Insere uma tabulação no início
    print("")#Quebra de linha

if len(lista_dir) > 0:#Checa se tem diretórios na lista
    print("Diretório:")
    for i in lista_dir:
        print("\t"+i)#Insere uma tabulação no início
    print("")#Quebra de linha