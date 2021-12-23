import os

p_dir = input("Entre com o diretório: ")
if os.path.isdir(p_dir):
    somador = 0
    lista = os.listdir(p_dir)
    for i in lista:
        p = os.path.join(p_dir, i)
        if os.path.isfile(p):
            somador = somador + os.stat(p).st_size
    print("Tamanho: ", somador/1000,"KB")
else:
    print(f"O diretório {p_dir} não existe.")