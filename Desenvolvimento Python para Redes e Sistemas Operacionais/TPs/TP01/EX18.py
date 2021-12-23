#Escreva um programa em Python, usando o módulo ‘psutil’, que imprima em GB, quanto de memória principal e quanto de memória de paginação (swap) existem no computador.
import psutil

def memória_física():
    analise_fisica = psutil.virtual_memory()
    tot_fis = analise_fisica[0]/(1024*1024*1024)
    print(round(tot_fis,2),"GB")

def memória_swap():
    analise_swap = psutil.swap_memory()
    tot_swap = analise_swap[0]/(1024*1024*1024)
    print(round(tot_swap,2),"GB")

memória_física()
memória_swap()