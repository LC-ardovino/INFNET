def gerar_nome_arquivo(ano):
    return f"consulta_cand_{ano}_RJ.csv"


def preparar_dados(ano):
    nome_arquivo = gerar_nome_arquivo(ano)
    arquivo = open(nome_arquivo, 'r', encoding='latin-1')
    dados_cruz = arquivo.read()
    linhas = dados_cruz.splitlines()
    dados_cruz_rotulos = linhas[0]
    lista_rotulos = dados_cruz_rotulos.split(';')
    dados_cruz_candidatos = linhas[1:]
    lista_candidatos = []
    for candidato in dados_cruz_candidatos:
        candidato = candidato.split(';')
        lista_candidatos.append(candidato)
    return lista_rotulos, lista_candidatos

def num_candidatos_genero(ano):
    rotulos, candidatos = preparar_dados(ano)
    genero = rotulos.index('GÊNERO')
    masc, fem, outros = 0,0,0
    for candidato in candidatos:
        if candidato[genero] == 'FEMININO':
            fem += 1
        elif candidato[genero] == 'MASCULINO':
            masc += 1
        else:
            outros += 1
        total = fem+masc+outros
    resultados = [total, masc, fem, outros]
    return resultados


from matplotlib import pyplot as plt

def exibir_graficos_multiplos(eixo_x, eixos_y, sub_rotulos_y, linhas, **rotulos):
    titulo = rotulos.get('titulo')
    rotulo_x = rotulos.get('rotulo_x')
    rotulo_y = rotulos.get('rotulo_y')

    fig, ax = plt.subplots()
    for i in range(len(eixos_y)):
        ax.plot(eixo_x, eixos_y[i], linhas[i], label=sub_rotulos_y[i])
    ax.legend()
    if titulo:
        plt.title(titulo)
    if rotulo_x:
        plt.xlabel(rotulo_x)
    if rotulo_y:
        plt.ylabel(rotulo_y)
plt.show()


#Programa Principal

