import os
import sched
import socket
import subprocess
import sys
import threading
import time
import psutil
import cpuinfo
import nmap
import platform


def processos(pid):
    try:
        p = psutil.Process(pid)
        texto = '{:6}'.format(pid)
        texto = texto + '{:11}'.format(p.num_threads())
        texto = texto + " " + time.ctime(p.create_time()) + " "
        texto = texto + '{:8.2f}'.format(p.cpu_times().user)
        texto = texto + '{:8.2f}'.format(p.cpu_times().system)
        texto = texto + '{:10.2f}'.format(p.memory_percent()) + " MB"
        rss = p.memory_info().rss / 1024 / 1024
        texto = texto + '{:10.2f}'.format(rss) + " MB"
        vms = p.memory_info().vms / 1024 / 1024
        texto = texto + '{:10.2f}'.format(vms) + " MB"
        texto = texto + " " + p.exe()
        return texto
    except:
        pass

def mostra_dados_arquivos():
    # Obtém lista de arquivos e diretórios do diretório corrente:
    lista = os.listdir()
    dic = {}  # cria um dicionário
    lista_dir = []
    Texto = []
    for i in lista:
        if os.path.isfile(i):
            # Cria uma lista para cada arquivo.Esta lista contém o tamanho, data de criação e data de modificação.
            dic[i] = []
            dic[i].append(os.stat(i).st_size)  # Tamanho
            dic[i].append(os.stat(i).st_atime)  # Tempo de criação
            dic[i].append(os.stat(i).st_mtime)  # Tempo de modificação
    for d in lista:
        if os.path.isdir(d):
            lista_dir.append(d)
    diretorio = f'Diretórios: {lista_dir}'

    titulo = '{:11}'.format("Tamanho")  # 10 caracteres +1 de espaço
    # Concatenar com 25 caracteres +2 de espaço
    titulo = titulo + '{:27}'.format('Data de Modificação')
    # Concatenar com 25 caracteres +2 de espaço
    titulo = titulo + '{:27}'.format('Data de Criação')
    titulo = titulo + 'Nome'
    titulo_final = titulo


    for i in dic:
        kb = dic[i][0] / 1024
        tamanho = '{:10}'.format(str('{:.2f}'.format(kb) + 'KB'))
        dados = tamanho + " " + time.ctime(dic[i][2]) + " " + time.ctime(dic[i][1]) + " " + i
        Texto.append(dados)

    return (diretorio + "\n" + titulo_final + "\n" + Texto[0] + "\n" + Texto[1])


def escalonamento_principal():

    start = time.time()
    print("Iniciando as chamadas escalonadas.")
    scheduler = sched.scheduler(time.time, time.sleep)
    scheduler.enter(1, 1, arquivo,)
    scheduler.enter(2, 1, processo)
    scheduler.run()
    end = time.time()
    total = abs(end - start)
    data = ("Finalizando as chamadas escalonadas..." + (f" Tempo total: {total:.0f} segundos"))
    return data


def arquivo():
    diretorio = r'C:\Users\DESKTOP\PycharmProjects\Infnet\Projeto_de_Bloco\TP8'
    os.chdir(diretorio)
    os.listdir(diretorio)
    for arquivo in os.listdir():
        return (f'''Tamanho:\t\tNome:\t\t\tData de criação:\t\t\t\tData de modificação:
{round(os.path.getsize(arquivo) / 1021, 2)} KB\t\t\t{os.path.basename(arquivo)}\t\t\
{time.ctime(os.path.getctime(arquivo))}\t\t{time.ctime(os.path.getmtime(arquivo))}''')


def processo():
    processo = 'python'
    pid = subprocess.Popen(processo).pid
    detalhe = psutil.Process(pid)
    uso_memoria = round(detalhe.memory_percent())
    return(f'''
Nome: {detalhe.name()}
Executável: {detalhe.exe()}
Data de criação: {time.ctime(detalhe.create_time())}
Uso de memória: {uso_memoria}%
Uso de CPU: {sum(detalhe.cpu_times()[:2])}%''')

def memoria():
    mem = psutil.virtual_memory()
    percent = mem[2]
    percent_texto = f"O percentual do uso de memória principal do computador do servidor é:{percent}%"
    return percent_texto

def CPU():
    info = cpuinfo.get_cpu_info()
    CPU_nome = info['brand_raw']
    CPU_percent_cores = psutil.cpu_percent(interval=1,percpu=True)
    CPU_text_cores = f"A porcentagem de uso do primeiro núcleo é:{CPU_percent_cores[0]}%\nA porcentagem de uso do segundo núcleo é:{CPU_percent_cores[1]}%\nA porcentagem de uso do terceiro núcleo é:{CPU_percent_cores[2]}%\nA porcentagem de uso do quarto núcleo é:{CPU_percent_cores[3]}%"

    CPU_percent = psutil.cpu_percent(interval=1)
    CPU_text = f"O percentual de uso da CPU é:{CPU_percent}%"
    return CPU_text +'\n'+ CPU_text_cores+'\n'+'Nome da CPU:'+CPU_nome

def disk():
    DISK= psutil.disk_usage("/")
    DISK_percent = DISK[3]
    DISK_text =  f"O percentual de uso do disco do servidor é:{DISK_percent}%"
    return DISK_text

def info_maquina():
    info = cpuinfo.get_cpu_info()
    arch = info['arch']
    palavra_proc_bits = info['bits']
    nucleos_logicos = psutil.cpu_count()
    nucleos_fisicos = psutil.cpu_count(logical=False)
    IP = socket.gethostbyname(socket.gethostname())
    return(f"A arquitetura da máquina é {arch}" + '\n' + f"O IP do computador é {IP}"+'\n'+ f"A palavra chave é {palavra_proc_bits}" + '\n' + f"O numero de núcleos lágicos é:{nucleos_logicos}" + '\n' + f"O numero de núcleos fisicos é:{nucleos_fisicos}")

"-------------------------------------------------------------------------------------------------"


def retorna_codigo_ping(hostname):
    plataforma = platform.system()
    args = []
    print(hostname)
    if plataforma == "Windows":
        args = ["ping", "-n", "1", "-l", "1", "-w", "100", hostname]

    else:
        args = ['ping', '-c', '1', '-W', '1', hostname]

    ret_cod = subprocess.call(args,
                              stdout=open(os.devnull, 'w'),
                              stderr=open(os.devnull, 'w'))
    return ret_cod


def verifica_hosts(base_ip):
    """Verifica todos os host com a base_ip entre 1 e 255 retorna uma lista com todos os host que tiveram resposta 0 (ativo)"""
    print("Mapeando\r")
    host_validos = []
    return_codes = dict()
    for i in range(1, 255):
        return_codes[base_ip + '{0}'.format(i)] = retorna_codigo_ping(base_ip + '{0}'.format(i))
        if i % 20 == 0:
            print(".", end="")
        if return_codes[base_ip + '{0}'.format(i)] == 0:
            host_validos.append(base_ip + '{0}'.format(i))
    print("\nMapping ready...")

    return host_validos


def obter_hostnames(host_validos):
    nm = nmap.PortScanner()
    for i in host_validos:
        try:
            nm.scan(i)
            for proto in nm[i].all_protocols():
                text = (f"O IP possui o nome: {nm[i].hostname()} \n ---------- \n Protocolo : {proto}'")

                lport = nm[i][proto].keys()
                # lport.sort()
                for port in lport:
                    text2 = ('Porta: %s\t Estado: %s' % (port, nm[i][proto][port]['state']))
            return(f"{text}\n{text2}")

        except:
            print("Erro no processamento.")
            pass

    # Chamadas


def dados_do_computador():
    uso_memoria = psutil.virtual_memory()
    disco = psutil.disk_usage('/')
    disco_total = disco[0]
    disco_ocupado = disco[1]
    disco_livre = disco[2]
    return(f"O total de disco do sistema é: {round(disco_total / (1024 * 1024 * 1024), 2)}GB" + '\n' + f"O total de disco ocupado é {round(disco_ocupado / (1024 * 1024 * 1024), 2)}GB" + '\n' + f"O total de disco livre é {round(disco_livre / (1024 * 1024 * 1024), 2)}GB" + '\n' + f"Uso da memória: {round(uso_memoria[0] / (1024 * 1024 * 1024), 2)}GB" + '\n' + f"Uso de CPU total: {sum(psutil.cpu_times()[:2])} %")


def redes(ip_string):
    dados_do_computador()
    ip_lista = ip_string.split('.')
    base_ip = ".".join(ip_lista[0:3]) + '.'
    host_validos = verifica_hosts(base_ip)
    return(f"{ip_string}\nO teste será feito na sub rede: {base_ip}  \n Os host válidos são: {host_validos} \n Iniciando nmapPortscanner \n {obter_hostnames(host_validos)}")




"--------------------------------------------------------------------------------------------------"

def processos_rede():
    a = psutil.net_io_counters().bytes_sent
    b = psutil.net_io_counters().bytes_recv
    c = psutil.net_io_counters().packets_sent
    d = psutil.net_io_counters().packets_recv

    time.sleep(1)

    vazao_s = psutil.net_io_counters().bytes_sent - a
    vazao_r = psutil.net_io_counters().bytes_recv - b

    a = a/1024/1024/1024
    b = b/1024/1024/1024
    text = (f"Informações do uso e dados por processos na Rede:\nGbytes enviados:{a}\nGbytes recebidos:{b}\nPacotes enviados: {c}\nPacotes recebidos: {d}\nVazão de bytes enviados: {vazao_s}\nVazão de bytes recebidos: {vazao_r}")
    return text

def processos_rede_interface():
    io_status = psutil.net_io_counters(pernic=True)
    nomes = []
    Texto = []
    Texto2 = []
    for i in io_status:
        nomes.append(str(i))
    for j in nomes:
        J = j
        text = ("\t" + str(io_status[j]))

        Texto.append(J)
        Texto.append(text)
    for i in range(4):
        time.sleep(1)
        io_status = psutil.net_io_counters(pernic=True)
    for j in nomes:
        J2 = j
        text2 = ("\t" + str(io_status[j]))

        Texto2.append(J2)
        Texto2.append(text2)
    cliente1 = (Texto[0] + "\n" + Texto[1] + "\n" + Texto[2] + "\n" + Texto[3] + "\n" + Texto[4] + "\n" + Texto[5] + Texto[6] + "\n" + Texto[7] + "\n" + Texto[8] + "\n" + Texto[9] + "\n" + Texto[10] + "\n" + Texto[11])
    cliente2 = (Texto2[0] + "\n" + Texto2[1] + "\n" + Texto2[2] + "\n" + Texto2[3] + "\n" + Texto2[4] + "\n" + Texto2[5] + Texto2[6] + "\n" + Texto2[7] + "\n" + Texto2[8] + "\n" + Texto2[9] + "\n" + Texto2[10] + "\n" + Texto2[11])
    cliente_final = cliente1+"\n"+cliente2
    return(cliente_final)

def ip_gateway_mascara():
    interfaces = psutil.net_if_addrs()
    nomes = []
    Texto = []
    # Obtém os nomes das interfaces primeiro
    for i in interfaces:
        nomes.append(str(i))
    status = psutil.net_if_stats()
    # Depois, imprimir os valores:
    for i in nomes:
        t = (i+":")
        sni = (str(status[i]))
        Texto.append(t)
        Texto.append(sni)
        for j in interfaces[i]:
            dados = ("\t"+str(j))
            Texto.append(dados)
    cliente = (Texto[0] + "\n" + Texto[1] + "\n" + Texto[2] + "\n" + Texto[3] + "\n" + Texto[4]+ "\n" + Texto[5]+ "\n" +Texto[6] + "\n" + Texto[7] + "\n" + Texto[8] + "\n" + Texto[9] + "\n" + Texto[10]+ "\n" + Texto[11]+ "\n" +Texto[12] + "\n" + Texto[13] + "\n" + Texto[14] + "\n" + Texto[15] + "\n" + Texto[16]+ "\n" + Texto[17]+ "\n" +Texto[18] + "\n" + Texto[19] + "\n" + Texto[20] + "\n" + Texto[21] + "\n" + Texto[22]+ "\n" + Texto[23]+ "\n" +Texto[24] + "\n" + Texto[25] + "\n" + Texto[26] + "\n" + Texto[27] + "\n" + Texto[28])
    return cliente


def handle_client(client_socket):
    request = client_socket.recv(1024)
    print("[*] Recebido: %s" % request)
    request_data = request.decode('utf-8')
    data = request_data.split(",")
    print(data)
    if data[0] == "1":
        pid = os.getpid()
        p = processos(pid)
        client_socket.send(p.encode('utf-8'))  # Envia mensagem

    elif data[0] == "2":
        interfaces = mostra_dados_arquivos()
        client_socket.send(interfaces.encode('utf-8'))

    elif data[0] == '3':
        cpu = CPU()
        disco = disk()
        memória = memoria()
        client_socket.send(cpu.encode('utf-8'))
        client_socket.send(memória.encode("utf-8"))
        client_socket.send(disco.encode("utf-8"))

    elif data[0] == "4":
        data = escalonamento_principal()
        proc = processo()
        arquiv = arquivo()
        client_socket.send(bytes(data, 'utf-8'))
        client_socket.send(bytes(arquiv, 'utf-8'))
        client_socket.send(bytes(proc, 'utf-8'))
        sys.exit()

    elif data[0] == '5':
        info = info_maquina()
        client_socket.send(info.encode('utf-8'))

    elif data[0] == '6':
        request_2 = client_socket.recv(1024)
        ip = request_2.decode("utf-8")
        ip_final = ip.split(",")
        ip_send = ip_final[0]
        info = redes(ip_send)
        client_socket.send(info.encode('utf-8'))
    elif data[0] == '7':
        info = processos_rede()
        client_socket.send(info.encode('utf-8'))
    elif data[0] == '8':
        info = processos_rede_interface()
        client_socket.send(info.encode('utf-8'))
    elif data[0] == '9':
        info = ip_gateway_mascara()
        client_socket.send(info.encode('utf-8'))

    print(client_socket.getpeername())
    client_socket.close()
#-----------------------------------------------------------------------------------------------
bind_ip = socket.gethostname()
bind_port = 9999
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def start_server():
    server.bind((bind_ip, bind_port))
    server.listen(5)
    print("[*] Escutando no endereço: %s:%d" % (bind_ip, bind_port))

def main():
    start_server()
    while True:
        client, addr = server.accept()
        print("[*] Nova conexão realizada pelo cliente %s:%d" % (addr[0], addr[1]))
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()
main()
if __name__ == "__main__":
    sys.exit(main())



