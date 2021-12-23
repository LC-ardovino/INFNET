import psutil as psutil

mem = psutil.virtual_memory()
print(mem.total)

#Segunda versão, convertendo pra GB

mem = psutil.virtual_memory()
capacidade = round(mem.total/(1024*1024*1024), 2)
print(f"A capacidade total de Memória Principal é {capacidade} GB")