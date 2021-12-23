#A função psutil.cpu_times() do módulo psutil retorna os tempos de CPU do computador classificados em 3 tipos:
#User: tempo executando no modo usuário.
#System: tempo executando no modo de sistema (usando funções do sistema operacional).
#Idle: tempo de inatividade.
import psutil, time
print(psutil.cpu_times())

#Exemplo de uso para obter os tempos por núcleo do processador:
print(psutil.cpu_times(percpu=True))

#É possível obter também a relação percentual destes tempos:
psutil.cpu_times_percent()
for i in range(10):
    time.sleep(0.1)
print(psutil.cpu_times_percent())

#Por núcleo de processador
print(psutil.cpu_times_percent(percpu=True))

#Diferentemente, é possível obter o tempo em um intervalo de tempo fixo usando o parâmetro ‘interval’:
print(psutil.cpu_times_percent(interval=1))

psutil.cpu_times_percent()
time.sleep(1)
print(psutil.cpu_times_percent())

#Obtendo o percentual de uso de CPU desde a última medida:

psutil.cpu_percent(percpu=True)
for i in range(3):
    time.sleep(0.1) # dorme por 0,1 segundos
    print(psutil.cpu_percent(percpu=True))