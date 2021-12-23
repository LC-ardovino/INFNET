import os
import time

nome_sistema_operacional = os.name
print(nome_sistema_operacional)

#Informações do sistema

nome_usuário = os.getlogin()
print(nome_usuário)

variaveis_ambiente = os.environ
print(variaveis_ambiente)

#Path do diretorio corrente

path_diretorio = os.getcwd()
print(path_diretorio)

#PID (identificador de processo) do próprio processo em execução.

PID_atual = os.getpid()
print(PID_atual)

#Manipular diretórios

#usando os.mkdir( "diretorio_exemplo") cria-se um diretório novo
#usando os.rename("diretorio_exemplo","diretorio_exemplo2") vc irá renomear o diretório
#Para remover um diretório, use a função os.rmdir("diretorio_exemplo2"). Ela só irá apagar um diretório se ele estiver vazio.
#Para listar arquivos e diretórios de um diretório específico use o comando  print(os.listdir('C:\\Users\\')) passando como parâmetro o nome do diretório.
#Para mudar de diretório para aquele especificado no parâmetro, use o comando os.chdir.

#Módulo os.path

#O módulo os apresenta um submódulo chamado path. Com ele, é possível manipular o nome e caminho (absoluto ou relativo) de um arquivo ou diretório.

#Verificando se um caminho de diretório existe...
p = 'diretorio_exemplo'
if os.path.exists(p):
    print(p, 'existe!')
else:
    print(p, 'não existe!')

#Verificando se p é um arquivo...
p = 'arq_texto.txt'
if os.path.isfile(p):
    print(p, 'é um arquivo!')
else:
    print(p, 'não é um arquivo!')

#Verificando se p é um diretório...
p = 'diretorio_exemplo'
if os.path.isfile(p):
    print(p, 'é um diretório!')
else:
    print(p, 'não é um diretório!')

#Verificando se p é um arquivo e se ele existe...
p = 'arq_texto.txt'
if os.path.isfile(p) is True:
    print(p, 'é um arquivo e ele existe!')
else:
    print(p, 'não existe!')

#Para obter o nome base de nome absoluto de um arquivo (isto é, obter apenas o nome do arquivo), use a função os.path.basename(path).
print(os.path.basename("C:\\Users\\Teste\\Desktop\\Exemplos\\arq_texto.txt"))

#Para obter o diretório, use os.path.dirname(path).
print(os.path.dirname("C:\\Users\\Teste\\Desktop\\Exemplos\\arq_texto.txt"))

#O comando os.path.abspath(file) retorna o caminho absoluto de um arquivo.
print(os.path.abspath('OS.py'))

#É possível também separar um caminho em partes usando a função os.path.split(path)
print(os.path.split("C:\\Users\\DESKTOP\\PycharmProjects\\Infnet\\Desenvolvimento Python para Redes e Sistemas Operacionais\\Etapa1\\OS.py"))

#Para gerar uma lista contendo todos os diretórios do caminho absoluto indicado acima:
p = os.path.abspath('OS.py')
t = os.path.split(p)  # separa em duas partes
p0 = t[0]  # parte 0
p1 = t[1]  # parte 1
lista_dir = []
while p1:  # fazer enquanto houver parte 1
    lista_dir.append(p1)  # adiciona à lista a parte 1
    t = os.path.split(p0)  # agora, separa p0
    p0 = t[0]
    p1 = t[1]
lista_dir.append(p0)  # Colocar último
lista_dir.reverse()  # Para reverter a lista, pois ela estava ao contrário
print(lista_dir)  # imprime a lista

#Para juntar diretórios e arquivos em um caminho, use os.path.join().
print(os.path.join("C:", "Users", "Teste", "arq_texto.txt"))
print(os.path.join(os.getcwd(), 'OS.py'))

#Obtendo status de arquivos
status = os.stat("C:\\Users\\DESKTOP\\PycharmProjects\\Infnet\\Desenvolvimento Python para Redes e Sistemas Operacionais\\Etapa1\\OS.py")
print(os.stat("C:\\Users\\DESKTOP\\PycharmProjects\\Infnet\\Desenvolvimento Python para Redes e Sistemas Operacionais\\Etapa1\\OS.py"))
print(status.st_size)
print(time.ctime(status.st_mtime))

#Gerenciamento de Processos

#os.abort(), aborta que o programa continue.

#Medindo tempo do processo
print(os.times())

# Parte do programa que queremos verificar o tempo
a = 0.1
for i in range(0, 10000000):
    a = a * 2.0
print(os.times())

#Executando e criando novos processos

executavel_com_path = os.environ['SYSTEMROOT'] + '\\System32\\calc.exe'
os.spawnl(os.P_NOWAIT, executavel_com_path, " ")

