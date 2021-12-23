#Escreva um programa em Python que:
#gere uma estrutura que armazena o nome dos arquivos em um determinado diretório e a quantidade de bytes que eles ocupam em disco. Obtenha o nome do diretório do usuário.
#Ordene decrescentemente esta estrutura pelo valor da quantidade de bytes ocupada em disco (pode usar as funções sort ou sorted);
#gere um arquivo texto com os valores desta estrutura ordenados.

import os
# Obtém lista de arquivos e diretórios do diretório corrente:
# caminho atual = C:\\Users\\DESKTOP\\PycharmProjects\\Infnet\\Desenvolvimento Python para Redes e Sistemas Operacionais\\Assessment
caminho = input("Digite um caminho:")
lista = os.listdir(caminho)
ordenado = sorted(lista)
dic = {}  # cria um dicionário
lista_dir = []

for i in ordenado:
    if os.path.isfile(i):
        # Cria uma lista para cada arquivo.Esta lista contém o tamanho, data de criação e data de modificação.
        dic[i] = []
        tam = os.stat(i).st_size
        dic[i].append(tam)  # Tamanho

for d in ordenado:
    if os.path.isdir(d):
        lista_dir.append(d)
print(f'Diretórios: {lista_dir}')

titulo = '{:11}'.format("Tamanho")
titulo = titulo + 'Nome'
print(titulo)

lista_tamanho = []
ordenado = []
new_dic = {}
for nome, dados in dic.items():
    kb = dados[0] / 1024
    tamanho = '{:10}'.format(str('{:.2f}'.format(kb) + 'KB'))
    ordenado.append(tamanho)
    dado = tamanho
    new_dic[nome] = dado
    print(new_dic[nome],nome)








