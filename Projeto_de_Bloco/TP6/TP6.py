#Criar uma ou mais funções que retornem ou apresentem informações sobre as máquinas pertencentes à sub-rede do IP específico.
#Usar a função em seu programa para mostrar o resultado. O resultado pode ser em texto formatado impresso na tela ou gráfico, usando o módulo ‘pygame’.
#Criar uma ou mais funções que retornem ou apresentem informações sobre as portas dos diferentes IPs obtidos nessa sub rede.
#Usar a função em seu programa para mostrar o resultado. O resultado pode ser em texto formatado impresso na tela ou gráfico, usando o ‘pygame’.

import os,subprocess,platform,nmap,psutil

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
                    text2 =('Porta: %s\t Estado: %s' % (port, nm[i][proto][port]['state']))
            print(f"{text}\n{text2}")

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
    print(f"O total de disco do sistema é: {round(disco_total / (1024 * 1024 * 1024), 2)}GB"+'\n'+f"O total de disco ocupado é {round(disco_ocupado / (1024 * 1024 * 1024), 2)}GB"+'\n'+f"O total de disco livre é {round(disco_livre / (1024 * 1024 * 1024), 2)}GB"+'\n'+f"Uso da memória: {round(uso_memoria[0] / (1024 * 1024 * 1024), 2)}GB"+'\n'+f"Uso de CPU total: {sum(psutil.cpu_times()[:2])} %")


def redes():
    dados_do_computador()
    ip_string = input("Entre com o ip alvo: ")
    ip_lista = ip_string.split('.')
    base_ip = ".".join(ip_lista[0:3]) + '.'
    host_validos = verifica_hosts(base_ip)
    print(f"O teste será feito na sub rede: {base_ip}  \n Os host válidos são: {host_validos} \n Iniciando nmapPortscanner \n {obter_hostnames(host_validos)}")

redes()
