#Escreva um programa em Python, usando o módulo ‘psutil’, que imprima em GB, quanto de armazenamento disponível há na partição do sistema (onde o sistema está instalado).

import psutil

def partição_livre():
    partição_sistema = psutil.disk_usage('C:')
    disponível = partição_sistema[2] / (1024 * 1024 * 1024)
    print(round(disponível, 2), "GB")

partição_livre()








