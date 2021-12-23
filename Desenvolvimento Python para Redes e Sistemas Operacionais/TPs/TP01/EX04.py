#Que função do módulo ‘os’ de Python é usada para obter o caminho absoluto de um diretório com caminho relativo? Dê um exemplo.
#C:\Users\DESKTOP\PycharmProjects\Infnet\Desenvolvimento Python para Redes e Sistemas Operacionais\TPs\TP01
import os

def obtendo_caminho():
    print("A função que é usada para se obter o caminho absoluto é o path.")
    print("Exemplo:")
    caminho = os.getcwd()
    print(f"O caminho absoluto do diretório atual é {os.path.dirname(caminho)}")
obtendo_caminho()
