#Escreva um programa usando o módulo ‘os’ de Python que imprima o PID do próprio processo.
import os


def pid():
    print(f"O PID do próprio processo é:{os.getpid()}")

pid()