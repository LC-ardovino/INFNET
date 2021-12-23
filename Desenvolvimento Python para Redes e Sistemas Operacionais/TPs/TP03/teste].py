import psutil
mem = psutil.virtual_memory()
mem_t = mem[0]
print(str(mem_t))