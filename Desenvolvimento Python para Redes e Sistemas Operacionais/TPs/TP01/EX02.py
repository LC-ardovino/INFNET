#Sobre variáveis de ambiente, responda:
#A-O que são?
#B-Como elas podem ser obtidas pelo módulo ‘os’ de Python?
#C-Como pode ser obtido o caminho completo do diretório de usuário em Python, através das variáveis de ambiente?
import os

def letra_A():
    print("Letra A:")
    print("Variáveis de ambiente são variáveis às quais são atribuídos valores externamente ao programa Python, existindo para a flexibilidade do programa.Elas são definidas na linha de comando antes de invocar o executável Python. ")

def letra_B():
    print("Letra B:")
    print("As variáveis de ambiente são acessadas através do dicionário os.environ do pacote os.Portanto, para acessar um valor específico em python, basta passar o nome da variável de ambiente entre colchetes no os. environ['NOME-DA-VARIÁVEL-DE-AMBIENTE'].")
    print("Exemplo:")
    print(f"Obtendo o drive: {os.environ['HOMEDRIVE']}")

def letra_C():
    print("Letra C:")
    print(f"Obtendo o caminho completo do diretório de usuário atual: {os.environ['HOMEPATH']}")

letra_A()
letra_B()
letra_C()

