import psutil
import os
import time

def func_comparacao(l):
    return(l["cpu_percent"])

for i in range(11):
    lista = []
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','cpu_percent'])
            lista.append(pinfo)
        except psutil.NoSuchProcess:
            pass
        os.system('cls')
        if lista:
            titulo = '{:<6}'.format("PID")
            titulo = titulo + '{:<20.19}'.format("Nome")
            titulo = titulo + '{:<6}'.format("%CPU")
            print(titulo)
            lista_ordenada = sorted(lista,key = func_comparacao,reverse=True)
            for i in lista_ordenada[0:15]:
                texto = '{:<6}'.format(i["pid"])
                texto = texto + '{:<20.19}'.format(i["name"])
                texto = texto + '{:<6}'.format(i["cpu_percent"])
                print(texto)
        time.sleep(1)

