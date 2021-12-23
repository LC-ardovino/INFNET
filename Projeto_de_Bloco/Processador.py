import platform
import psutil
import time
print(platform.processor())
print(platform.node())
print(platform.platform())
print(platform.system())

print("Informações relacionadas ao processamento do processador:")
for i in range(1,100):
    print(psutil.cpu_percent())
    time.sleep(1)