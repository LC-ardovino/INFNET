#Utilizar o módulo ‘sched’ para chamar as funções criadas no TP4 que retornam as informações sobre diretórios e arquivos.
#Realizar um escalonamento das chamadas das funções com o módulo ‘sched’ e medir o tempo total utilizado por cada chamada com o módulo ‘time’. Você pode escolher com quais funções do seu projeto realizar o escalonamento, deixando indicado no relatório.
#Dentro do escalonamento realizado na questão anterior, realizar uma comparação dos tempos obtidos com a quantidade total de clocks utilizados pela CPU para a realização dessas mesmas chamadas.

import sched,os,time,subprocess,psutil

def arquivo():
    diretorio = r'C:\Users\DESKTOP\PycharmProjects\Infnet\Projeto_de_Bloco\TP5'
    os.chdir(diretorio)
    os.listdir(diretorio)
    for arquivo in os.listdir():
        print(f'''Tamanho:\t\tNome:\t\t\tData de criação:\t\t\t\tData de modificação:
{round(os.path.getsize(arquivo) / 1021, 2)} KB\t\t\t{os.path.basename(arquivo)}\t\t\
{time.ctime(os.path.getctime(arquivo))}\t\t{time.ctime(os.path.getmtime(arquivo))}''')


def processo():
    processo = 'python'
    pid = subprocess.Popen(processo).pid
    detalhe = psutil.Process(pid)
    uso_memoria = round(detalhe.memory_percent())
    print(f'''
Nome: {detalhe.name()}
Executável: {detalhe.exe()}
Data de criação: {time.ctime(detalhe.create_time())}
Uso de memória: {uso_memoria}%
Uso de CPU: {sum(detalhe.cpu_times()[:2])}%''')


scheduler = sched.scheduler(time.time, time.sleep)


def programa_principal():
    tempo_inicio = time.time()
    print('INICIO:', time.ctime())
    print(f'CHAMADAS ESCALONADAS DA FUNÇÃO: {time.ctime()}\n')
    scheduler.enter(2, 1, arquivo)
    scheduler.run()
    tempo_fim = time.time()
    print("\nEncerrando as chamadas escalonadas.")
    tempo_total = abs(tempo_fim - tempo_inicio)
    print(f"Tempo total: {tempo_total:.0f} segundos\n")

    tempo_inicio = time.time()
    scheduler.enter(3, 1, processo)
    print(f'CHAMADAS ESCALONADAS DA FUNÇÃO: {time.ctime()}\n')
    scheduler.run()
    tempo_fim = time.time()
    print("\nEncerrando as chamadas escalonadas.")
    tempo_total = abs(tempo_fim - tempo_inicio)
    print(f"Tempo total: {tempo_total:.0f} segundos")

programa_principal()




