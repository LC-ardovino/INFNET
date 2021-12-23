import cpuinfo
import psutil
info = cpuinfo.get_cpu_info()

for i in info:
   print(i,':',info[i])#imprime todas as informações obtidas pela função
print("Dados específicos:")
print(info['arch'])#Imprime a arquitetura da CPU
print(info['brand_raw'])#Imprime o nome da CPU
print(info['bits'])#Imprime o número de bits
print(psutil.cpu_count())#Imprime o número de núcleos lógicos(cores)
print(psutil.cpu_count(logical=False))#Imprime o número de núcleos físicos
print(psutil.cpu_percent())#Imprime a frequência


