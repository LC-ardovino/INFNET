import psutil

disco = psutil.disk_usage('.')
print("------------B------------")
print(f"Total:{disco.total} B")
print(f"Em uso:{disco.used} B")
print(f"Livre:{disco.free} B")
print("------------GB------------")
print(f"Total:{round(disco.total/(1024*1024*1024))} GB")
print(f"Em uso:{round(disco.used/(1024*1024*1024))} GB")
print(f"Livre:{round(disco.free/(1024*1024*1024))} GB")

print(f"Percentual de Disco Usado:{disco.percent}%.")