import os

#Identificando o nome do sistema
print(os.name)

#Identificando o usuário:
print(os.getlogin())

#Mapeador de caminhos

print(os.environ['HOMEPATH'])#Printa o caminho onde está a pasta do usuário

#Identificando o caminho em que o usuário se encontra:

print(os.getcwd())

#Identificando o número do processo atual:

print(os.getpid())

#Listando todos os usuários criados:

print(os.listdir("c:\\Users\\"))


