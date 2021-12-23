#Para cada esporte, considere todas as modalidades, tanto no masculino quanto no feminino. Sua resposta deve imprimir um relatório mostrando o total de medalhas de cada um dos países e em que esporte, ano, cidade e gênero (masculino ou feminino) cada medalha foi obtida.


import requests

url = "https://sites.google.com/site/dr2fundamentospython/arquivos/Winter_Olympics_Medals.csv"

# Usando requests e checando conexao
requisicao = requests.get(url, timeout=5)
if requisicao.status_code != 200:
    requisicao.raise_for_status()
else:
    print("Conectado com sucesso!")

# Obtendo o CSV:
csv = requisicao.text

# Separa as linhas em uma lista
linhas = csv.splitlines()



ouro = 'Ouro'
prata = 'Prata'
bronze = 'Bronze'
def dados_1924_Skating_Speed(ano):
    mod = 'Speed Skating'
    cont_Fin_M_Speed_Gold =cont_Fin_F_Speed_Gold=cont_Fin_M_Speed_Silver=cont_Fin_F_Speed_Silver=cont_Fin_M_Speed_bronze=cont_Fin_F_Speed_bronze= 0
    cont_NOR_M_Speed_Gold =cont_NOR_F_Speed_Gold=cont_NOR_M_Speed_Silver=cont_NOR_F_Speed_Silver=cont_NOR_M_Speed_bronze=cont_NOR_F_Speed_bronze= 0
    cont_USA_M_Speed_Gold =cont_USA_F_Speed_Gold=cont_USA_M_Speed_Silver=cont_USA_F_Speed_Silver=cont_USA_M_Speed_bronze=cont_USA_F_Speed_bronze= 0
    cont_AUT_M_Speed_Gold =cont_AUT_F_Speed_Gold=cont_AUT_M_Speed_Silver=cont_AUT_F_Speed_Silver=cont_AUT_M_Speed_bronze=cont_AUT_F_Speed_bronze= 0
    cont_BEL_M_Speed_Gold =cont_BEL_F_Speed_Gold=cont_BEL_M_Speed_Silver=cont_BEL_F_Speed_Silver=cont_BEL_M_Speed_bronze=cont_BEL_F_Speed_bronze= 0
    cont_FRAN_M_Speed_Gold =cont_FRAN_F_Speed_Gold=cont_FRAN_M_Speed_Silver=cont_FRAN_F_Speed_Silver=cont_FRAN_M_Speed_bronze=cont_FRAN_F_Speed_bronze= 0
    cont_GBR_M_Speed_Gold =cont_GBR_F_Speed_Gold=cont_GBR_M_Speed_Silver=cont_GBR_F_Speed_Silver=cont_GBR_M_Speed_bronze=cont_GBR_F_Speed_bronze= 0
    cont_SWE_M_Speed_Gold =cont_SWE_F_Speed_Gold=cont_SWE_M_Speed_Silver=cont_SWE_F_Speed_Silver=cont_SWE_M_Speed_bronze=cont_SWE_F_Speed_bronze= 0
    for l in range(1, len(linhas)):
        colunas = linhas[l].split(',')

        if colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Speed skating' and colunas[4] == 'FIN' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_Fin_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Speed skating' and colunas[4] == 'FIN' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_Fin_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Speed skating' and colunas[4] == 'FIN' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_Fin_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Speed skating' and colunas[4] == 'FIN' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_Fin_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Speed skating' and colunas[4] == 'FIN' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_Fin_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Speed skating' and colunas[4] == 'FIN' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_Fin_F_Speed_bronze += 1

        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Speed skating' and colunas[4] == 'NOR' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_NOR_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Speed skating' and colunas[4] == 'NOR' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_NOR_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Speed skating' and colunas[4] == 'NOR' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_NOR_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Speed skating' and colunas[4] == 'NOR' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_NOR_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Speed skating' and colunas[4] == 'NOR' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_NOR_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Speed skating' and colunas[4] == 'NOR' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_NOR_F_Speed_bronze += 1

        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Speed skating' and colunas[4] == 'USA' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_USA_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Speed skating' and colunas[4] == 'USA' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_USA_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Speed skating' and colunas[4] == 'USA' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_USA_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Speed skating' and colunas[4] == 'USA' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_USA_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Speed skating' and colunas[4] == 'USA' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_USA_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Speed skating' and colunas[4] == 'USA' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_USA_F_Speed_bronze += 1

        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Speed skating' and colunas[4] == 'AUT' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_AUT_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Speed skating' and colunas[4] == 'AUT' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_AUT_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Speed skating' and colunas[4] == 'AUT' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_AUT_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Speed skating' and colunas[4] == 'AUT' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_AUT_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Speed skating' and colunas[4] == 'AUT' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_AUT_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Speed skating' and colunas[4] == 'AUT' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_AUT_F_Speed_bronze += 1

        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Speed skating' and colunas[4] == 'BEL' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_BEL_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Speed skating' and colunas[4] == 'BEL' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_BEL_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Speed skating' and colunas[4] == 'BEL' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_BEL_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Speed skating' and colunas[4] == 'BEL' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_BEL_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Speed skating' and colunas[4] == 'BEL' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_BEL_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Speed skating' and colunas[4] == 'BEL' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_BEL_F_Speed_bronze += 1

        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Speed skating' and colunas[4] == 'FRAN' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_FRAN_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Speed skating' and colunas[4] == 'FRAN' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_FRAN_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Speed skating' and colunas[4] == 'FRAN' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_FRAN_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Speed skating' and colunas[4] == 'FRAN' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_FRAN_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Speed skating' and colunas[4] == 'FRAN' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_FRAN_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Speed skating' and colunas[4] == 'FRAN' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_FRAN_F_Speed_bronze += 1


        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Speed skating' and colunas[4] == 'GBR' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_GBR_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Speed skating' and colunas[4] == 'GBR' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_GBR_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Speed skating' and colunas[4] == 'GBR' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_GBR_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Speed skating' and colunas[4] == 'GBR' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_GBR_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Speed skating' and colunas[4] == 'GBR' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_GBR_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Speed skating' and colunas[4] == 'GBR' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_GBR_F_Speed_bronze += 1

        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Speed skating' and colunas[4] == 'GBR' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_SWE_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Speed skating' and colunas[4] == 'GBR' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_SWE_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Speed skating' and colunas[4] == 'GBR' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_SWE_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Speed skating' and colunas[4] == 'GBR' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_SWE_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Speed skating' and colunas[4] == 'GBR' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_SWE_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Speed skating' and colunas[4] == 'GBR' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_SWE_F_Speed_bronze += 1

    print(F"Finlândia conseguiu em {ano} {cont_Fin_M_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade masculina de {mod}.")
    print(F"Finlândia conseguiu em {ano} {cont_Fin_F_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade feminina de {mod}.")
    print(F"Finlândia conseguiu em {ano} {cont_Fin_M_Speed_Silver} medalhas de {prata} em {cidade} na modalidade masculina de {mod}.")
    print(F"Finlândia conseguiu em {ano} {cont_Fin_F_Speed_Silver} medalhas de {prata} em {cidade} na modalidade feminina de {mod}.")
    print(F"Finlândia conseguiu em {ano} {cont_Fin_M_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade masculina de {mod}.")
    print(F"Finlândia conseguiu em {ano} {cont_Fin_F_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)
    print(F"Noruega conseguiu em {ano} {cont_NOR_M_Speed_Gold} medalhas de {ouro} na modalidade masculina de {mod}.")
    print(F"Noruega conseguiu em {ano} {cont_NOR_F_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade feminina de {mod}.")
    print(F"Noruega conseguiu em {ano} {cont_NOR_M_Speed_Silver} medalhas de {prata} em {cidade} na modalidade masculina de {mod}.")
    print(F"Noruega conseguiu em {ano} {cont_NOR_F_Speed_Silver} medalhas de {prata} em {cidade} na modalidade feminina de {mod}.")
    print(F"Noruega conseguiu em {ano} {cont_NOR_M_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade masculina de {mod}.")
    print(F"Noruega conseguiu em {ano} {cont_NOR_F_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)
    print(F"Estados Unidos conseguiu em {ano} {cont_USA_M_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade masculina de {mod}.")
    print(F"Estados Unidos conseguiu em {ano} {cont_USA_F_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade feminina de {mod}.")
    print(F"Estados Unidos conseguiu em {ano} {cont_USA_M_Speed_Silver} medalhas de {prata} em {cidade} na modalidade masculina de {mod}.")
    print(F"Estados Unidos conseguiu em {ano} {cont_USA_F_Speed_Silver} medalhas de {prata} em {cidade} na modalidade feminina de {mod}.")
    print(F"Estados Unidos conseguiu em {ano} {cont_USA_M_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade masculina de {mod}.")
    print(F"Estados Unidos em conseguiu em {ano} {cont_USA_F_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)
    print(F"Austria conseguiu em {ano} {cont_AUT_M_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade masculina de {mod}.")
    print(F"Austria conseguiu em {ano} {cont_AUT_F_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade feminina de {mod}.")
    print(F"Austria conseguiu em {ano} {cont_AUT_M_Speed_Silver} medalhas de {prata} em {cidade} na modalidade masculina de {mod}.")
    print(F"Austria conseguiu em {ano} {cont_AUT_F_Speed_Silver} medalhas de {prata} em {cidade} na modalidade feminina de {mod}.")
    print(F"Austria conseguiu em {ano} {cont_AUT_M_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade masculina de {mod}.")
    print(F"Austria conseguiu em {ano} {cont_AUT_F_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)
    print(F"Bélgica conseguiu em {ano} {cont_BEL_M_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade masculina de {mod}.")
    print(F"Bélgica conseguiu em {ano} {cont_BEL_F_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade feminina de {mod}.")
    print(F"Bélgica conseguiu em {ano} {cont_BEL_F_Speed_Silver} medalhas de {prata} em {cidade} na modalidade feminina de {mod}.")
    print(F"Bélgica conseguiu em {ano} {cont_BEL_M_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade masculina de {mod}.")
    print(F"Bélgica conseguiu em {ano} {cont_BEL_F_Speed_bronze} medalhas de {bronze}  em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)
    print(F"França conseguiu em {ano} {cont_FRAN_M_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade masculina de {mod}.")
    print(F"França conseguiu em {ano} {cont_FRAN_F_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade feminina de {mod}.")
    print(F"França conseguiu em {ano} {cont_FRAN_M_Speed_Silver} medalhas de {prata} em {cidade} na modalidade masculina de {mod}.")
    print(F"França conseguiu em {ano} {cont_FRAN_F_Speed_Silver} medalhas de {prata} em {cidade} na modalidade feminina de {mod}.")
    print(F"França conseguiu em {ano} {cont_FRAN_M_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade masculina de {mod}.")
    print(F"França conseguiu em {ano} {cont_FRAN_F_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)
    print(F"Reino Unido conseguiu em {ano} {cont_GBR_M_Speed_Gold} medalhas de {ouro}  em {cidade} na modalidade masculina de {mod}.")
    print(F"Reino Unido conseguiu em {ano} {cont_GBR_F_Speed_Gold} medalhas de {ouro}  em {cidade} na modalidade feminina de {mod}.")
    print(F"Reino Unido conseguiu em {ano} {cont_GBR_M_Speed_Silver} medalhas de {prata}  em {cidade} na modalidade masculina de {mod}.")
    print(F"Reino Unido conseguiu em {ano} {cont_GBR_F_Speed_Silver} medalhas de {prata}  em {cidade} na modalidade feminina de {mod}.")
    print(F"Reino Unido conseguiu em {ano} {cont_GBR_M_Speed_bronze} medalhas de {bronze}  em {cidade} na modalidade masculina de {mod}.")
    print(F"Reino Unido conseguiu em {ano} {cont_GBR_F_Speed_bronze} medalhas de {bronze}  em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)
    print(F"Suécia conseguiu em {ano} {cont_SWE_M_Speed_Gold} medalhas de {ouro}  em {cidade} na modalidade masculina de {mod}.")
    print(F"Suécia conseguiu em {ano} {cont_SWE_F_Speed_Gold} medalhas de {ouro}  em {cidade} na modalidade feminina de {mod}.")
    print(F"Suécia conseguiu em {ano} {cont_SWE_M_Speed_Silver} medalhas de {prata}  em {cidade} na modalidade masculina de {mod}.")
    print(F"Suécia conseguiu em {ano} {cont_SWE_F_Speed_Silver} medalhas de {prata}  em {cidade} na modalidade feminina de {mod}.")
    print(F"Suécia conseguiu em {ano} {cont_SWE_M_Speed_bronze} medalhas de {bronze}  em {cidade} na modalidade masculina de {mod}.")
    print(F"Suécia conseguiu em {ano} {cont_SWE_F_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)

def dados_1924_Skating_figure(ano):
    mod = 'Figure Skating'
    cont_Fin_M_Speed_Gold =cont_Fin_F_Speed_Gold=cont_Fin_M_Speed_Silver=cont_Fin_F_Speed_Silver=cont_Fin_M_Speed_bronze=cont_Fin_F_Speed_bronze= 0
    cont_NOR_M_Speed_Gold =cont_NOR_F_Speed_Gold=cont_NOR_M_Speed_Silver=cont_NOR_F_Speed_Silver=cont_NOR_M_Speed_bronze=cont_NOR_F_Speed_bronze= 0
    cont_USA_M_Speed_Gold =cont_USA_F_Speed_Gold=cont_USA_M_Speed_Silver=cont_USA_F_Speed_Silver=cont_USA_M_Speed_bronze=cont_USA_F_Speed_bronze= 0
    cont_AUT_M_Speed_Gold =cont_AUT_F_Speed_Gold=cont_AUT_M_Speed_Silver=cont_AUT_F_Speed_Silver=cont_AUT_M_Speed_bronze=cont_AUT_F_Speed_bronze= 0
    cont_BEL_M_Speed_Gold =cont_BEL_F_Speed_Gold=cont_BEL_M_Speed_Silver=cont_BEL_F_Speed_Silver=cont_BEL_M_Speed_bronze=cont_BEL_F_Speed_bronze= 0
    cont_FRAN_M_Speed_Gold =cont_FRAN_F_Speed_Gold=cont_FRAN_M_Speed_Silver=cont_FRAN_F_Speed_Silver=cont_FRAN_M_Speed_bronze=cont_FRAN_F_Speed_bronze= 0
    cont_GBR_M_Speed_Gold =cont_GBR_F_Speed_Gold=cont_GBR_M_Speed_Silver=cont_GBR_F_Speed_Silver=cont_GBR_M_Speed_bronze=cont_GBR_F_Speed_bronze= 0
    cont_SWE_M_Speed_Gold =cont_SWE_F_Speed_Gold=cont_SWE_M_Speed_Silver=cont_SWE_F_Speed_Silver=cont_SWE_M_Speed_bronze=cont_SWE_F_Speed_bronze= 0
    for l in range(1, len(linhas)):
        colunas = linhas[l].split(',')

        if colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Figure skating' and colunas[4] == 'FIN' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_Fin_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Figure skating' and colunas[4] == 'FIN' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_Fin_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Figure skating' and colunas[4] == 'FIN' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_Fin_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Figure skating' and colunas[4] == 'FIN' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_Fin_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Figure skating' and colunas[4] == 'FIN' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_Fin_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Figure skating' and colunas[4] == 'FIN' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_Fin_F_Speed_bronze += 1

        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Figure skating' and colunas[4] == 'NOR' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_NOR_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Figure skating' and colunas[4] == 'NOR' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_NOR_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Figure skating' and colunas[4] == 'NOR' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_NOR_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Figure skating' and colunas[4] == 'NOR' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_NOR_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Figure skating' and colunas[4] == 'NOR' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_NOR_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Figure skating' and colunas[4] == 'NOR' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_NOR_F_Speed_bronze += 1

        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Figure skating' and colunas[4] == 'USA' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_USA_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Figure skating' and colunas[4] == 'USA' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_USA_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Figure skating' and colunas[4] == 'USA' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_USA_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Figure skating' and colunas[4] == 'USA' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_USA_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Figure skating' and colunas[4] == 'USA' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_USA_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Figure skating' and colunas[4] == 'USA' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_USA_F_Speed_bronze += 1

        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Figure skating' and colunas[4] == 'AUT' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_AUT_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Figure skating' and colunas[4] == 'AUT' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_AUT_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Figure skating' and colunas[4] == 'AUT' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_AUT_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Figure skating' and colunas[4] == 'AUT' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_AUT_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Figure skating' and colunas[4] == 'AUT' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_AUT_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Figure skating' and colunas[4] == 'AUT' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_AUT_F_Speed_bronze += 1

        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Figure skating' and colunas[4] == 'BEL' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_BEL_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Figure skating' and colunas[4] == 'BEL' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_BEL_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Figure skating' and colunas[4] == 'BEL' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_BEL_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Figure skating' and colunas[4] == 'BEL' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_BEL_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Figure skating' and colunas[4] == 'BEL' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_BEL_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Figure skating' and colunas[4] == 'BEL' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_BEL_F_Speed_bronze += 1

        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Figure skating' and colunas[4] == 'FRAN' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_FRAN_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Figure skating' and colunas[4] == 'FRAN' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_FRAN_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Figure skating' and colunas[4] == 'FRAN' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_FRAN_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Figure skating' and colunas[4] == 'FRAN' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_FRAN_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Figure skating' and colunas[4] == 'FRAN' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_FRAN_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Figure skating' and colunas[4] == 'FRAN' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_FRAN_F_Speed_bronze += 1


        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Figure skating' and colunas[4] == 'GBR' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_GBR_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Figure skating' and colunas[4] == 'GBR' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_GBR_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Figure skating' and colunas[4] == 'GBR' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_GBR_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Figure skating' and colunas[4] == 'GBR' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_GBR_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Figure skating' and colunas[4] == 'GBR' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_GBR_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Figure skating' and colunas[4] == 'GBR' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_GBR_F_Speed_bronze += 1

        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Figure skating' and colunas[4] == 'GBR' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_SWE_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Figure skating' and colunas[4] == 'GBR' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_SWE_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Figure skating' and colunas[4] == 'GBR' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_SWE_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Figure skating' and colunas[4] == 'GBR' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_SWE_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Figure skating' and colunas[4] == 'GBR' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_SWE_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Skating' and colunas[3] == 'Figure skating' and colunas[4] == 'GBR' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_SWE_F_Speed_bronze += 1

    print(F"Finlândia conseguiu em {ano} {cont_Fin_M_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade masculina de {mod}.")
    print(F"Finlândia conseguiu em {ano} {cont_Fin_F_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade feminina de {mod}.")
    print(F"Finlândia conseguiu em {ano} {cont_Fin_M_Speed_Silver} medalhas de {prata} em {cidade} na modalidade masculina de {mod}.")
    print(F"Finlândia conseguiu em {ano} {cont_Fin_F_Speed_Silver} medalhas de {prata} em {cidade} na modalidade feminina de {mod}.")
    print(F"Finlândia conseguiu em {ano} {cont_Fin_M_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade masculina de {mod}.")
    print(F"Finlândia conseguiu em {ano} {cont_Fin_F_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)
    print(F"Noruega conseguiu em {ano} {cont_NOR_M_Speed_Gold} medalhas de {ouro} na modalidade masculina de {mod}.")
    print(F"Noruega conseguiu em {ano} {cont_NOR_F_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade feminina de {mod}.")
    print(F"Noruega conseguiu em {ano} {cont_NOR_M_Speed_Silver} medalhas de {prata} em {cidade} na modalidade masculina de {mod}.")
    print(F"Noruega conseguiu em {ano} {cont_NOR_F_Speed_Silver} medalhas de {prata} em {cidade} na modalidade feminina de {mod}.")
    print(F"Noruega conseguiu em {ano} {cont_NOR_M_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade masculina de {mod}.")
    print(F"Noruega conseguiu em {ano} {cont_NOR_F_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)
    print(F"Estados Unidos conseguiu em {ano} {cont_USA_M_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade masculina de {mod}.")
    print(F"Estados Unidos conseguiu em {ano} {cont_USA_F_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade feminina de {mod}.")
    print(F"Estados Unidos conseguiu em {ano} {cont_USA_M_Speed_Silver} medalhas de {prata} em {cidade} na modalidade masculina de {mod}.")
    print(F"Estados Unidos conseguiu em {ano} {cont_USA_F_Speed_Silver} medalhas de {prata} em {cidade} na modalidade feminina de {mod}.")
    print(F"Estados Unidos conseguiu em {ano} {cont_USA_M_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade masculina de {mod}.")
    print(F"Estados Unidos em conseguiu em {ano} {cont_USA_F_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)
    print(F"Austria conseguiu em {ano} {cont_AUT_M_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade masculina de {mod}.")
    print(F"Austria conseguiu em {ano} {cont_AUT_F_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade feminina de {mod}.")
    print(F"Austria conseguiu em {ano} {cont_AUT_M_Speed_Silver} medalhas de {prata} em {cidade} na modalidade masculina de {mod}.")
    print(F"Austria conseguiu em {ano} {cont_AUT_F_Speed_Silver} medalhas de {prata} em {cidade} na modalidade feminina de {mod}.")
    print(F"Austria conseguiu em {ano} {cont_AUT_M_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade masculina de {mod}.")
    print(F"Austria conseguiu em {ano} {cont_AUT_F_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)
    print(F"Bélgica conseguiu em {ano} {cont_BEL_M_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade masculina de {mod}.")
    print(F"Bélgica conseguiu em {ano} {cont_BEL_F_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade feminina de {mod}.")
    print(F"Bélgica conseguiu em {ano} {cont_BEL_F_Speed_Silver} medalhas de {prata} em {cidade} na modalidade feminina de {mod}.")
    print(F"Bélgica conseguiu em {ano} {cont_BEL_M_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade masculina de {mod}.")
    print(F"Bélgica conseguiu em {ano} {cont_BEL_F_Speed_bronze} medalhas de {bronze}  em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)
    print(F"França conseguiu em {ano} {cont_FRAN_M_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade masculina de {mod}.")
    print(F"França conseguiu em {ano} {cont_FRAN_F_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade feminina de {mod}.")
    print(F"França conseguiu em {ano} {cont_FRAN_M_Speed_Silver} medalhas de {prata} em {cidade} na modalidade masculina de {mod}.")
    print(F"França conseguiu em {ano} {cont_FRAN_F_Speed_Silver} medalhas de {prata} em {cidade} na modalidade feminina de {mod}.")
    print(F"França conseguiu em {ano} {cont_FRAN_M_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade masculina de {mod}.")
    print(F"França conseguiu em {ano} {cont_FRAN_F_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)
    print(F"Reino Unido conseguiu em {ano} {cont_GBR_M_Speed_Gold} medalhas de {ouro}  em {cidade} na modalidade masculina de {mod}.")
    print(F"Reino Unido conseguiu em {ano} {cont_GBR_F_Speed_Gold} medalhas de {ouro}  em {cidade} na modalidade feminina de {mod}.")
    print(F"Reino Unido conseguiu em {ano} {cont_GBR_M_Speed_Silver} medalhas de {prata}  em {cidade} na modalidade masculina de {mod}.")
    print(F"Reino Unido conseguiu em {ano} {cont_GBR_F_Speed_Silver} medalhas de {prata}  em {cidade} na modalidade feminina de {mod}.")
    print(F"Reino Unido conseguiu em {ano} {cont_GBR_M_Speed_bronze} medalhas de {bronze}  em {cidade} na modalidade masculina de {mod}.")
    print(F"Reino Unido conseguiu em {ano} {cont_GBR_F_Speed_bronze} medalhas de {bronze}  em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)
    print(F"Suécia conseguiu em {ano} {cont_SWE_M_Speed_Gold} medalhas de {ouro}  em {cidade} na modalidade masculina de {mod}.")
    print(F"Suécia conseguiu em {ano} {cont_SWE_F_Speed_Gold} medalhas de {ouro}  em {cidade} na modalidade feminina de {mod}.")
    print(F"Suécia conseguiu em {ano} {cont_SWE_M_Speed_Silver} medalhas de {prata}  em {cidade} na modalidade masculina de {mod}.")
    print(F"Suécia conseguiu em {ano} {cont_SWE_F_Speed_Silver} medalhas de {prata}  em {cidade} na modalidade feminina de {mod}.")
    print(F"Suécia conseguiu em {ano} {cont_SWE_M_Speed_bronze} medalhas de {bronze}  em {cidade} na modalidade masculina de {mod}.")
    print(F"Suécia conseguiu em {ano} {cont_SWE_F_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)


def curling_1924(ano):
    mod = 'Curling'
    cont_Fin_M_Speed_Gold = cont_Fin_F_Speed_Gold = cont_Fin_M_Speed_Silver = cont_Fin_F_Speed_Silver = cont_Fin_M_Speed_bronze = cont_Fin_F_Speed_bronze = 0
    cont_NOR_M_Speed_Gold = cont_NOR_F_Speed_Gold = cont_NOR_M_Speed_Silver = cont_NOR_F_Speed_Silver = cont_NOR_M_Speed_bronze = cont_NOR_F_Speed_bronze = 0
    cont_USA_M_Speed_Gold = cont_USA_F_Speed_Gold = cont_USA_M_Speed_Silver = cont_USA_F_Speed_Silver = cont_USA_M_Speed_bronze = cont_USA_F_Speed_bronze = 0
    cont_AUT_M_Speed_Gold = cont_AUT_F_Speed_Gold = cont_AUT_M_Speed_Silver = cont_AUT_F_Speed_Silver = cont_AUT_M_Speed_bronze = cont_AUT_F_Speed_bronze = 0
    cont_BEL_M_Speed_Gold = cont_BEL_F_Speed_Gold = cont_BEL_M_Speed_Silver = cont_BEL_F_Speed_Silver = cont_BEL_M_Speed_bronze = cont_BEL_F_Speed_bronze = 0
    cont_FRAN_M_Speed_Gold = cont_FRAN_F_Speed_Gold = cont_FRAN_M_Speed_Silver = cont_FRAN_F_Speed_Silver = cont_FRAN_M_Speed_bronze = cont_FRAN_F_Speed_bronze = 0
    cont_GBR_M_Speed_Gold = cont_GBR_F_Speed_Gold = cont_GBR_M_Speed_Silver = cont_GBR_F_Speed_Silver = cont_GBR_M_Speed_bronze = cont_GBR_F_Speed_bronze = 0
    cont_SWE_M_Speed_Gold = cont_SWE_F_Speed_Gold = cont_SWE_M_Speed_Silver = cont_SWE_F_Speed_Silver = cont_SWE_M_Speed_bronze = cont_SWE_F_Speed_bronze = 0
    for l in range(1, len(linhas)):
        colunas = linhas[l].split(',')
        if colunas[0] == ano and colunas[2] == 'Curling' and colunas[3] == 'Curling' and colunas[4] == 'FIN' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_Fin_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Curling' and colunas[3] == 'Curling' and colunas[4] == 'FIN' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_Fin_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Curling' and colunas[3] == 'Curling' and colunas[4] == 'FIN' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_Fin_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Curling' and colunas[3] == 'Curling' and colunas[4] == 'FIN' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_Fin_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Curling' and colunas[3] == 'Curling' and colunas[4] == 'FIN' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_Fin_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Curling' and colunas[3] == 'Curling' and colunas[4] == 'FIN' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_Fin_F_Speed_bronze += 1

        elif colunas[0] == ano and colunas[2] == 'Curling' and colunas[3] == 'Curling' and colunas[4] == 'NOR' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_NOR_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Curling' and colunas[3] == 'Curling' and colunas[4] == 'NOR' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_NOR_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Curling' and colunas[3] == 'Curling' and colunas[4] == 'NOR' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_NOR_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Curling' and colunas[3] == 'Curling' and colunas[4] == 'NOR' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_NOR_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Curling' and colunas[3] == 'Curling' and colunas[4] == 'NOR' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_NOR_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Curling' and colunas[3] == 'Curling' and colunas[4] == 'NOR' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_NOR_F_Speed_bronze += 1

        elif colunas[0] == ano and colunas[2] == 'Curling' and colunas[3] == 'Curling' and colunas[4] == 'USA' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_USA_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Curling' and colunas[3] == 'Curling' and colunas[4] == 'USA' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_USA_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Curling' and colunas[3] == 'Curling' and colunas[4] == 'USA' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_USA_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Curling' and colunas[3] == 'Curling' and colunas[4] == 'USA' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_USA_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Curling' and colunas[3] == 'Curling' and colunas[4] == 'USA' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_USA_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Curling' and colunas[3] == 'Curling' and colunas[4] == 'USA' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_USA_F_Speed_bronze += 1

        elif colunas[0] == ano and colunas[2] == 'Curling' and colunas[3] == 'Curling' and colunas[4] == 'AUT' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_AUT_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Curling' and colunas[3] == 'Curling' and colunas[4] == 'AUT' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_AUT_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Curling' and colunas[3] == 'Curling' and colunas[4] == 'AUT' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_AUT_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Curling' and colunas[3] == 'Curling' and colunas[4] == 'AUT' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_AUT_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Curling' and colunas[3] == 'Curling' and colunas[4] == 'AUT' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_AUT_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Curling' and colunas[3] == 'Curling' and colunas[4] == 'AUT' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_AUT_F_Speed_bronze += 1

        elif colunas[0] == ano and colunas[2] == 'Curling' and colunas[3] == 'Curling' and colunas[4] == 'BEL' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_BEL_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Curling' and colunas[3] == 'Curling' and colunas[4] == 'BEL' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_BEL_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Curling' and colunas[3] == 'Curling' and colunas[4] == 'BEL' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_BEL_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Curling' and colunas[3] == 'Curling' and colunas[4] == 'BEL' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_BEL_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Curling' and colunas[3] == 'Curling' and colunas[4] == 'BEL' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_BEL_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Curling' and colunas[3] == 'Curling' and colunas[4] == 'BEL' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_BEL_F_Speed_bronze += 1

        elif colunas[0] == ano and colunas[2] == 'Curling' and colunas[3] == 'Curling' and colunas[4] == 'FRAN' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_FRAN_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Curling' and colunas[3] == 'Curling' and colunas[4] == 'FRAN' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_FRAN_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Curling' and colunas[3] == 'Curling' and colunas[4] == 'FRAN' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_FRAN_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Curling' and colunas[3] == 'Curling' and colunas[4] == 'FRAN' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_FRAN_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Curling' and colunas[3] == 'Curling' and colunas[4] == 'FRAN' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_FRAN_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Curling' and colunas[3] == 'Curling' and colunas[4] == 'FRAN' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_FRAN_F_Speed_bronze += 1


        elif colunas[0] == ano and colunas[2] == 'Curling' and colunas[3] == 'Curling' and colunas[4] == 'GBR' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_GBR_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Curling' and colunas[3] == 'Curling' and colunas[4] == 'GBR' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_GBR_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Curling' and colunas[3] == 'Curling' and colunas[4] == 'GBR' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_GBR_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Curling' and colunas[3] == 'Curling' and colunas[4] == 'GBR' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_GBR_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Curling' and colunas[3] == 'Curling' and colunas[4] == 'GBR' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_GBR_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Curling' and colunas[3] == 'Curling' and colunas[4] == 'GBR' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_GBR_F_Speed_bronze += 1

        elif colunas[0] == ano and colunas[2] == 'Curling' and colunas[3] == 'Curling' and colunas[4] == 'GBR' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_SWE_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Curling' and colunas[3] == 'Curling' and colunas[4] == 'GBR' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_SWE_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Curling' and colunas[3] == 'Curling' and colunas[4] == 'GBR' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_SWE_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Curling' and colunas[3] == 'Curling' and colunas[4] == 'GBR' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_SWE_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Curling' and colunas[3] == 'Curling' and colunas[4] == 'GBR' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_SWE_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Curling' and colunas[3] == 'Curling' and colunas[4] == 'GBR' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_SWE_F_Speed_bronze += 1

    print(F"Finlândia conseguiu em {ano} {cont_Fin_M_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade masculina de {mod}.")
    print(F"Finlândia conseguiu em {ano} {cont_Fin_F_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade feminina de {mod}.")
    print(F"Finlândia conseguiu em {ano} {cont_Fin_M_Speed_Silver} medalhas de {prata} em {cidade} na modalidade masculina de {mod}.")
    print(F"Finlândia conseguiu em {ano} {cont_Fin_F_Speed_Silver} medalhas de {prata} em {cidade} na modalidade feminina de {mod}.")
    print(F"Finlândia conseguiu em {ano} {cont_Fin_M_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade masculina de {mod}.")
    print(F"Finlândia conseguiu em {ano} {cont_Fin_F_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)
    print(F"Noruega conseguiu em {ano} {cont_NOR_M_Speed_Gold} medalhas de {ouro} na modalidade masculina de {mod}.")
    print(F"Noruega conseguiu em {ano} {cont_NOR_F_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade feminina de {mod}.")
    print(F"Noruega conseguiu em {ano} {cont_NOR_M_Speed_Silver} medalhas de {prata} em {cidade} na modalidade masculina de {mod}.")
    print(F"Noruega conseguiu em {ano} {cont_NOR_F_Speed_Silver} medalhas de {prata} em {cidade} na modalidade feminina de {mod}.")
    print(F"Noruega conseguiu em {ano} {cont_NOR_M_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade masculina de {mod}.")
    print(F"Noruega conseguiu em {ano} {cont_NOR_F_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)
    print(F"Estados Unidos conseguiu em {ano} {cont_USA_M_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade masculina de {mod}.")
    print(F"Estados Unidos conseguiu em {ano} {cont_USA_F_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade feminina de {mod}.")
    print(F"Estados Unidos conseguiu em {ano} {cont_USA_M_Speed_Silver} medalhas de {prata} em {cidade} na modalidade masculina de {mod}.")
    print(F"Estados Unidos conseguiu em {ano} {cont_USA_F_Speed_Silver} medalhas de {prata} em {cidade} na modalidade feminina de {mod}.")
    print(F"Estados Unidos conseguiu em {ano} {cont_USA_M_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade masculina de {mod}.")
    print(F"Estados Unidos em conseguiu em {ano} {cont_USA_F_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)
    print(F"Austria conseguiu em {ano} {cont_AUT_M_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade masculina de {mod}.")
    print(F"Austria conseguiu em {ano} {cont_AUT_F_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade feminina de {mod}.")
    print(F"Austria conseguiu em {ano} {cont_AUT_M_Speed_Silver} medalhas de {prata} em {cidade} na modalidade masculina de {mod}.")
    print(F"Austria conseguiu em {ano} {cont_AUT_F_Speed_Silver} medalhas de {prata} em {cidade} na modalidade feminina de {mod}.")
    print(F"Austria conseguiu em {ano} {cont_AUT_M_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade masculina de {mod}.")
    print(F"Austria conseguiu em {ano} {cont_AUT_F_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)
    print(F"Bélgica conseguiu em {ano} {cont_BEL_M_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade masculina de {mod}.")
    print(F"Bélgica conseguiu em {ano} {cont_BEL_F_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade feminina de {mod}.")
    print(F"Bélgica conseguiu em {ano} {cont_BEL_F_Speed_Silver} medalhas de {prata} em {cidade} na modalidade feminina de {mod}.")
    print(F"Bélgica conseguiu em {ano} {cont_BEL_M_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade masculina de {mod}.")
    print(F"Bélgica conseguiu em {ano} {cont_BEL_F_Speed_bronze} medalhas de {bronze}  em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)
    print(F"França conseguiu em {ano} {cont_FRAN_M_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade masculina de {mod}.")
    print(F"França conseguiu em {ano} {cont_FRAN_F_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade feminina de {mod}.")
    print(F"França conseguiu em {ano} {cont_FRAN_M_Speed_Silver} medalhas de {prata} em {cidade} na modalidade masculina de {mod}.")
    print(F"França conseguiu em {ano} {cont_FRAN_F_Speed_Silver} medalhas de {prata} em {cidade} na modalidade feminina de {mod}.")
    print(F"França conseguiu em {ano} {cont_FRAN_M_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade masculina de {mod}.")
    print(F"França conseguiu em {ano} {cont_FRAN_F_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)
    print(F"Reino Unido conseguiu em {ano} {cont_GBR_M_Speed_Gold} medalhas de {ouro}  em {cidade} na modalidade masculina de {mod}.")
    print(F"Reino Unido conseguiu em {ano} {cont_GBR_F_Speed_Gold} medalhas de {ouro}  em {cidade} na modalidade feminina de {mod}.")
    print(F"Reino Unido conseguiu em {ano} {cont_GBR_M_Speed_Silver} medalhas de {prata}  em {cidade} na modalidade masculina de {mod}.")
    print(F"Reino Unido conseguiu em {ano} {cont_GBR_F_Speed_Silver} medalhas de {prata}  em {cidade} na modalidade feminina de {mod}.")
    print(F"Reino Unido conseguiu em {ano} {cont_GBR_M_Speed_bronze} medalhas de {bronze}  em {cidade} na modalidade masculina de {mod}.")
    print(F"Reino Unido conseguiu em {ano} {cont_GBR_F_Speed_bronze} medalhas de {bronze}  em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)
    print(F"Suécia conseguiu em {ano} {cont_SWE_M_Speed_Gold} medalhas de {ouro}  em {cidade} na modalidade masculina de {mod}.")
    print(F"Suécia conseguiu em {ano} {cont_SWE_F_Speed_Gold} medalhas de {ouro}  em {cidade} na modalidade feminina de {mod}.")
    print(F"Suécia conseguiu em {ano} {cont_SWE_M_Speed_Silver} medalhas de {prata}  em {cidade} na modalidade masculina de {mod}.")
    print(F"Suécia conseguiu em {ano} {cont_SWE_F_Speed_Silver} medalhas de {prata}  em {cidade} na modalidade feminina de {mod}.")
    print(F"Suécia conseguiu em {ano} {cont_SWE_M_Speed_bronze} medalhas de {bronze}  em {cidade} na modalidade masculina de {mod}.")
    print(F"Suécia conseguiu em {ano} {cont_SWE_F_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)


def skiing_1924(ano):
    mod = 'Skiing-Cross Country'
    cont_Fin_M_Speed_Gold = cont_Fin_F_Speed_Gold = cont_Fin_M_Speed_Silver = cont_Fin_F_Speed_Silver = cont_Fin_M_Speed_bronze = cont_Fin_F_Speed_bronze = 0
    cont_NOR_M_Speed_Gold = cont_NOR_F_Speed_Gold = cont_NOR_M_Speed_Silver = cont_NOR_F_Speed_Silver = cont_NOR_M_Speed_bronze = cont_NOR_F_Speed_bronze = 0
    cont_USA_M_Speed_Gold = cont_USA_F_Speed_Gold = cont_USA_M_Speed_Silver = cont_USA_F_Speed_Silver = cont_USA_M_Speed_bronze = cont_USA_F_Speed_bronze = 0
    cont_AUT_M_Speed_Gold = cont_AUT_F_Speed_Gold = cont_AUT_M_Speed_Silver = cont_AUT_F_Speed_Silver = cont_AUT_M_Speed_bronze = cont_AUT_F_Speed_bronze = 0
    cont_BEL_M_Speed_Gold = cont_BEL_F_Speed_Gold = cont_BEL_M_Speed_Silver = cont_BEL_F_Speed_Silver = cont_BEL_M_Speed_bronze = cont_BEL_F_Speed_bronze = 0
    cont_FRAN_M_Speed_Gold = cont_FRAN_F_Speed_Gold = cont_FRAN_M_Speed_Silver = cont_FRAN_F_Speed_Silver = cont_FRAN_M_Speed_bronze = cont_FRAN_F_Speed_bronze = 0
    cont_GBR_M_Speed_Gold = cont_GBR_F_Speed_Gold = cont_GBR_M_Speed_Silver = cont_GBR_F_Speed_Silver = cont_GBR_M_Speed_bronze = cont_GBR_F_Speed_bronze = 0
    cont_SWE_M_Speed_Gold = cont_SWE_F_Speed_Gold = cont_SWE_M_Speed_Silver = cont_SWE_F_Speed_Silver = cont_SWE_M_Speed_bronze = cont_SWE_F_Speed_bronze = 0
    for l in range(1, len(linhas)):
        colunas = linhas[l].split(',')

        if colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Cross Country S' and colunas[4] == 'FIN' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_Fin_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Cross Country S' and colunas[4] == 'FIN' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_Fin_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Cross Country S' and colunas[4] == 'FIN' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_Fin_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Cross Country S' and colunas[4] == 'FIN' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_Fin_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Cross Country S' and colunas[4] == 'FIN' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_Fin_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Cross Country S' and colunas[4] == 'FIN' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_Fin_F_Speed_bronze += 1

        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Cross Country S' and colunas[4] == 'NOR' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_NOR_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Cross Country S' and colunas[4] == 'NOR' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_NOR_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Cross Country S' and colunas[4] == 'NOR' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_NOR_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Cross Country S' and colunas[4] == 'NOR' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_NOR_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Cross Country S' and colunas[4] == 'NOR' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_NOR_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Cross Country S' and colunas[4] == 'NOR' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_NOR_F_Speed_bronze += 1


        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Cross Country S' and colunas[4] == 'USA' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_USA_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Cross Country S' and colunas[4] == 'USA' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_USA_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Cross Country S' and colunas[4] == 'USA' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_USA_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Cross Country S' and colunas[4] == 'USA' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_USA_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Cross Country S' and colunas[4] == 'USA' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_USA_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Cross Country S' and colunas[4] == 'USA' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_USA_F_Speed_bronze += 1

        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Cross Country S' and colunas[4] == 'AUT' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_AUT_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Cross Country S' and colunas[4] == 'AUT' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_AUT_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Cross Country S' and colunas[4] == 'AUT' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_AUT_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Cross Country S' and colunas[4] == 'AUT' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_AUT_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Cross Country S' and colunas[4] == 'AUT' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_AUT_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Cross Country S' and colunas[4] == 'AUT' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_AUT_F_Speed_bronze += 1

        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Cross Country S' and colunas[4] == 'BEL' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_BEL_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Cross Country S' and colunas[4] == 'BEL' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_BEL_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Cross Country S' and colunas[4] == 'BEL' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_BEL_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Cross Country S' and colunas[4] == 'BEL' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_BEL_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Cross Country S' and colunas[4] == 'BEL' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_BEL_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Cross Country S' and colunas[4] == 'BEL' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_BEL_F_Speed_bronze += 1

        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Cross Country S' and colunas[4] == 'FRAN' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_FRAN_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Cross Country S' and colunas[4] == 'FRAN' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_FRAN_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Cross Country S' and colunas[4] == 'FRAN' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_FRAN_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Cross Country S' and colunas[4] == 'FRAN' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_FRAN_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Cross Country S' and colunas[4] == 'FRAN' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_FRAN_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Cross Country S' and colunas[4] == 'FRAN' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_FRAN_F_Speed_bronze += 1


        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Cross Country S' and colunas[4] == 'GBR' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_GBR_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Cross Country S' and colunas[4] == 'GBR' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_GBR_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Cross Country S' and colunas[4] == 'GBR' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_GBR_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Cross Country S' and colunas[4] == 'GBR' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_GBR_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Cross Country S' and colunas[4] == 'GBR' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_GBR_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Cross Country S' and colunas[4] == 'GBR' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_GBR_F_Speed_bronze += 1

        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Cross Country S' and colunas[4] == 'GBR' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_SWE_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Cross Country S' and colunas[4] == 'GBR' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_SWE_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Cross Country S' and colunas[4] == 'GBR' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_SWE_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Cross Country S' and colunas[4] == 'GBR' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_SWE_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Cross Country S' and colunas[4] == 'GBR' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_SWE_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Cross Country S' and colunas[4] == 'GBR' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_SWE_F_Speed_bronze += 1

    print(F"Finlândia conseguiu em {ano} {cont_Fin_M_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade masculina de {mod}.")
    print(F"Finlândia conseguiu em {ano} {cont_Fin_F_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade feminina de {mod}.")
    print(F"Finlândia conseguiu em {ano} {cont_Fin_M_Speed_Silver} medalhas de {prata} em {cidade} na modalidade masculina de {mod}.")
    print(F"Finlândia conseguiu em {ano} {cont_Fin_F_Speed_Silver} medalhas de {prata} em {cidade} na modalidade feminina de {mod}.")
    print(F"Finlândia conseguiu em {ano} {cont_Fin_M_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade masculina de {mod}.")
    print(F"Finlândia conseguiu em {ano} {cont_Fin_F_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)
    print(F"Noruega conseguiu em {ano} {cont_NOR_M_Speed_Gold} medalhas de {ouro} na modalidade masculina de {mod}.")
    print(F"Noruega conseguiu em {ano} {cont_NOR_F_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade feminina de {mod}.")
    print(F"Noruega conseguiu em {ano} {cont_NOR_M_Speed_Silver} medalhas de {prata} em {cidade} na modalidade masculina de {mod}.")
    print(F"Noruega conseguiu em {ano} {cont_NOR_F_Speed_Silver} medalhas de {prata} em {cidade} na modalidade feminina de {mod}.")
    print(F"Noruega conseguiu em {ano} {cont_NOR_M_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade masculina de {mod}.")
    print(F"Noruega conseguiu em {ano} {cont_NOR_F_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)
    print(F"Estados Unidos conseguiu em {ano} {cont_USA_M_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade masculina de {mod}.")
    print(F"Estados Unidos conseguiu em {ano} {cont_USA_F_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade feminina de {mod}.")
    print(F"Estados Unidos conseguiu em {ano} {cont_USA_M_Speed_Silver} medalhas de {prata} em {cidade} na modalidade masculina de {mod}.")
    print(F"Estados Unidos conseguiu em {ano} {cont_USA_F_Speed_Silver} medalhas de {prata} em {cidade} na modalidade feminina de {mod}.")
    print(F"Estados Unidos conseguiu em {ano} {cont_USA_M_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade masculina de {mod}.")
    print(F"Estados Unidos em conseguiu em {ano} {cont_USA_F_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)
    print(F"Austria conseguiu em {ano} {cont_AUT_M_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade masculina de {mod}.")
    print(F"Austria conseguiu em {ano} {cont_AUT_F_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade feminina de {mod}.")
    print(F"Austria conseguiu em {ano} {cont_AUT_M_Speed_Silver} medalhas de {prata} em {cidade} na modalidade masculina de {mod}.")
    print(F"Austria conseguiu em {ano} {cont_AUT_F_Speed_Silver} medalhas de {prata} em {cidade} na modalidade feminina de {mod}.")
    print(F"Austria conseguiu em {ano} {cont_AUT_M_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade masculina de {mod}.")
    print(F"Austria conseguiu em {ano} {cont_AUT_F_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)
    print(F"Bélgica conseguiu em {ano} {cont_BEL_M_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade masculina de {mod}.")
    print(F"Bélgica conseguiu em {ano} {cont_BEL_F_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade feminina de {mod}.")
    print(F"Bélgica conseguiu em {ano} {cont_BEL_F_Speed_Silver} medalhas de {prata} em {cidade} na modalidade feminina de {mod}.")
    print(F"Bélgica conseguiu em {ano} {cont_BEL_M_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade masculina de {mod}.")
    print(F"Bélgica conseguiu em {ano} {cont_BEL_F_Speed_bronze} medalhas de {bronze}  em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)
    print(F"França conseguiu em {ano} {cont_FRAN_M_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade masculina de {mod}.")
    print(F"França conseguiu em {ano} {cont_FRAN_F_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade feminina de {mod}.")
    print(F"França conseguiu em {ano} {cont_FRAN_M_Speed_Silver} medalhas de {prata} em {cidade} na modalidade masculina de {mod}.")
    print(F"França conseguiu em {ano} {cont_FRAN_F_Speed_Silver} medalhas de {prata} em {cidade} na modalidade feminina de {mod}.")
    print(F"França conseguiu em {ano} {cont_FRAN_M_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade masculina de {mod}.")
    print(F"França conseguiu em {ano} {cont_FRAN_F_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)
    print(F"Reino Unido conseguiu em {ano} {cont_GBR_M_Speed_Gold} medalhas de {ouro}  em {cidade} na modalidade masculina de {mod}.")
    print(F"Reino Unido conseguiu em {ano} {cont_GBR_F_Speed_Gold} medalhas de {ouro}  em {cidade} na modalidade feminina de {mod}.")
    print(F"Reino Unido conseguiu em {ano} {cont_GBR_M_Speed_Silver} medalhas de {prata}  em {cidade} na modalidade masculina de {mod}.")
    print(F"Reino Unido conseguiu em {ano} {cont_GBR_F_Speed_Silver} medalhas de {prata}  em {cidade} na modalidade feminina de {mod}.")
    print(F"Reino Unido conseguiu em {ano} {cont_GBR_M_Speed_bronze} medalhas de {bronze}  em {cidade} na modalidade masculina de {mod}.")
    print(F"Reino Unido conseguiu em {ano} {cont_GBR_F_Speed_bronze} medalhas de {bronze}  em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)
    print(F"Suécia conseguiu em {ano} {cont_SWE_M_Speed_Gold} medalhas de {ouro}  em {cidade} na modalidade masculina de {mod}.")
    print(F"Suécia conseguiu em {ano} {cont_SWE_F_Speed_Gold} medalhas de {ouro}  em {cidade} na modalidade feminina de {mod}.")
    print(F"Suécia conseguiu em {ano} {cont_SWE_M_Speed_Silver} medalhas de {prata}  em {cidade} na modalidade masculina de {mod}.")
    print(F"Suécia conseguiu em {ano} {cont_SWE_F_Speed_Silver} medalhas de {prata}  em {cidade} na modalidade feminina de {mod}.")
    print(F"Suécia conseguiu em {ano} {cont_SWE_M_Speed_bronze} medalhas de {bronze}  em {cidade} na modalidade masculina de {mod}.")
    print(F"Suécia conseguiu em {ano} {cont_SWE_F_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)



def skiing_Nordic_1924(ano):
    mod = 'Skiing-Nordic Combined'
    cont_Fin_M_Speed_Gold = cont_Fin_F_Speed_Gold = cont_Fin_M_Speed_Silver = cont_Fin_F_Speed_Silver = cont_Fin_M_Speed_bronze = cont_Fin_F_Speed_bronze = 0
    cont_NOR_M_Speed_Gold = cont_NOR_F_Speed_Gold = cont_NOR_M_Speed_Silver = cont_NOR_F_Speed_Silver = cont_NOR_M_Speed_bronze = cont_NOR_F_Speed_bronze = 0
    cont_USA_M_Speed_Gold = cont_USA_F_Speed_Gold = cont_USA_M_Speed_Silver = cont_USA_F_Speed_Silver = cont_USA_M_Speed_bronze = cont_USA_F_Speed_bronze = 0
    cont_AUT_M_Speed_Gold = cont_AUT_F_Speed_Gold = cont_AUT_M_Speed_Silver = cont_AUT_F_Speed_Silver = cont_AUT_M_Speed_bronze = cont_AUT_F_Speed_bronze = 0
    cont_BEL_M_Speed_Gold = cont_BEL_F_Speed_Gold = cont_BEL_M_Speed_Silver = cont_BEL_F_Speed_Silver = cont_BEL_M_Speed_bronze = cont_BEL_F_Speed_bronze = 0
    cont_FRAN_M_Speed_Gold = cont_FRAN_F_Speed_Gold = cont_FRAN_M_Speed_Silver = cont_FRAN_F_Speed_Silver = cont_FRAN_M_Speed_bronze = cont_FRAN_F_Speed_bronze = 0
    cont_GBR_M_Speed_Gold = cont_GBR_F_Speed_Gold = cont_GBR_M_Speed_Silver = cont_GBR_F_Speed_Silver = cont_GBR_M_Speed_bronze = cont_GBR_F_Speed_bronze = 0
    cont_SWE_M_Speed_Gold = cont_SWE_F_Speed_Gold = cont_SWE_M_Speed_Silver = cont_SWE_F_Speed_Silver = cont_SWE_M_Speed_bronze = cont_SWE_F_Speed_bronze = 0
    for l in range(1, len(linhas)):
        colunas = linhas[l].split(',')

        if colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Nordic Combined' and colunas[4] == 'FIN' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_Fin_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Nordic Combined' and colunas[4] == 'FIN' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_Fin_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Nordic Combined' and colunas[4] == 'FIN' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_Fin_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Nordic Combined' and colunas[4] == 'FIN' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_Fin_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Nordic Combined' and colunas[4] == 'FIN' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_Fin_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Nordic Combined' and colunas[4] == 'FIN' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_Fin_F_Speed_bronze += 1

        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Nordic Combined' and colunas[4] == 'NOR' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_NOR_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Nordic Combined' and colunas[4] == 'NOR' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_NOR_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Nordic Combined' and colunas[4] == 'NOR' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_NOR_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Nordic Combined' and colunas[4] == 'NOR' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_NOR_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Nordic Combined' and colunas[4] == 'NOR' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_NOR_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Nordic Combined' and colunas[4] == 'NOR' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_NOR_F_Speed_bronze += 1


        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Nordic Combined' and colunas[4] == 'USA' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_USA_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Nordic Combined' and colunas[4] == 'USA' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_USA_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Nordic Combined' and colunas[4] == 'USA' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_USA_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Nordic Combined' and colunas[4] == 'USA' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_USA_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Nordic Combined' and colunas[4] == 'USA' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_USA_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Nordic Combined' and colunas[4] == 'USA' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_USA_F_Speed_bronze += 1

        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Nordic Combined' and colunas[4] == 'AUT' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_AUT_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Nordic Combined' and colunas[4] == 'AUT' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_AUT_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Nordic Combined' and colunas[4] == 'AUT' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_AUT_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Nordic Combined' and colunas[4] == 'AUT' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_AUT_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Nordic Combined' and colunas[4] == 'AUT' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_AUT_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Nordic Combined' and colunas[4] == 'AUT' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_AUT_F_Speed_bronze += 1

        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Nordic Combined' and colunas[4] == 'BEL' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_BEL_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Nordic Combined' and colunas[4] == 'BEL' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_BEL_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Nordic Combined' and colunas[4] == 'BEL' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_BEL_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Nordic Combined' and colunas[4] == 'BEL' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_BEL_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Nordic Combined' and colunas[4] == 'BEL' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_BEL_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Nordic Combined' and colunas[4] == 'BEL' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_BEL_F_Speed_bronze += 1

        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Nordic Combined' and colunas[4] == 'FRAN' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_FRAN_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Nordic Combined' and colunas[4] == 'FRAN' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_FRAN_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Nordic Combined' and colunas[4] == 'FRAN' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_FRAN_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Nordic Combined' and colunas[4] == 'FRAN' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_FRAN_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Nordic Combined' and colunas[4] == 'FRAN' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_FRAN_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Nordic Combined' and colunas[4] == 'FRAN' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_FRAN_F_Speed_bronze += 1


        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Nordic Combined' and colunas[4] == 'GBR' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_GBR_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Nordic Combined' and colunas[4] == 'GBR' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_GBR_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Nordic Combined' and colunas[4] == 'GBR' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_GBR_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Nordic Combined' and colunas[4] == 'GBR' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_GBR_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Nordic Combined' and colunas[4] == 'GBR' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_GBR_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Nordic Combined' and colunas[4] == 'GBR' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_GBR_F_Speed_bronze += 1

        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Nordic Combined' and colunas[4] == 'GBR' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_SWE_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Nordic Combined' and colunas[4] == 'GBR' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_SWE_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Nordic Combined' and colunas[4] == 'GBR' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_SWE_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Nordic Combined' and colunas[4] == 'GBR' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_SWE_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Nordic Combined' and colunas[4] == 'GBR' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_SWE_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Nordic Combined' and colunas[4] == 'GBR' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_SWE_F_Speed_bronze += 1

    print(F"Finlândia conseguiu em {ano} {cont_Fin_M_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade masculina de {mod}.")
    print(F"Finlândia conseguiu em {ano} {cont_Fin_F_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade feminina de {mod}.")
    print(F"Finlândia conseguiu em {ano} {cont_Fin_M_Speed_Silver} medalhas de {prata} em {cidade} na modalidade masculina de {mod}.")
    print(F"Finlândia conseguiu em {ano} {cont_Fin_F_Speed_Silver} medalhas de {prata} em {cidade} na modalidade feminina de {mod}.")
    print(F"Finlândia conseguiu em {ano} {cont_Fin_M_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade masculina de {mod}.")
    print(F"Finlândia conseguiu em {ano} {cont_Fin_F_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)
    print(F"Noruega conseguiu em {ano} {cont_NOR_M_Speed_Gold} medalhas de {ouro} na modalidade masculina de {mod}.")
    print(F"Noruega conseguiu em {ano} {cont_NOR_F_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade feminina de {mod}.")
    print(F"Noruega conseguiu em {ano} {cont_NOR_M_Speed_Silver} medalhas de {prata} em {cidade} na modalidade masculina de {mod}.")
    print(F"Noruega conseguiu em {ano} {cont_NOR_F_Speed_Silver} medalhas de {prata} em {cidade} na modalidade feminina de {mod}.")
    print(F"Noruega conseguiu em {ano} {cont_NOR_M_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade masculina de {mod}.")
    print(F"Noruega conseguiu em {ano} {cont_NOR_F_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)
    print(F"Estados Unidos conseguiu em {ano} {cont_USA_M_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade masculina de {mod}.")
    print(F"Estados Unidos conseguiu em {ano} {cont_USA_F_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade feminina de {mod}.")
    print(F"Estados Unidos conseguiu em {ano} {cont_USA_M_Speed_Silver} medalhas de {prata} em {cidade} na modalidade masculina de {mod}.")
    print(F"Estados Unidos conseguiu em {ano} {cont_USA_F_Speed_Silver} medalhas de {prata} em {cidade} na modalidade feminina de {mod}.")
    print(F"Estados Unidos conseguiu em {ano} {cont_USA_M_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade masculina de {mod}.")
    print(F"Estados Unidos em conseguiu em {ano} {cont_USA_F_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)
    print(F"Austria conseguiu em {ano} {cont_AUT_M_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade masculina de {mod}.")
    print(F"Austria conseguiu em {ano} {cont_AUT_F_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade feminina de {mod}.")
    print(F"Austria conseguiu em {ano} {cont_AUT_M_Speed_Silver} medalhas de {prata} em {cidade} na modalidade masculina de {mod}.")
    print(F"Austria conseguiu em {ano} {cont_AUT_F_Speed_Silver} medalhas de {prata} em {cidade} na modalidade feminina de {mod}.")
    print(F"Austria conseguiu em {ano} {cont_AUT_M_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade masculina de {mod}.")
    print(F"Austria conseguiu em {ano} {cont_AUT_F_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)
    print(F"Bélgica conseguiu em {ano} {cont_BEL_M_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade masculina de {mod}.")
    print(F"Bélgica conseguiu em {ano} {cont_BEL_F_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade feminina de {mod}.")
    print(F"Bélgica conseguiu em {ano} {cont_BEL_F_Speed_Silver} medalhas de {prata} em {cidade} na modalidade feminina de {mod}.")
    print(F"Bélgica conseguiu em {ano} {cont_BEL_M_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade masculina de {mod}.")
    print(F"Bélgica conseguiu em {ano} {cont_BEL_F_Speed_bronze} medalhas de {bronze}  em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)
    print(F"França conseguiu em {ano} {cont_FRAN_M_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade masculina de {mod}.")
    print(F"França conseguiu em {ano} {cont_FRAN_F_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade feminina de {mod}.")
    print(F"França conseguiu em {ano} {cont_FRAN_M_Speed_Silver} medalhas de {prata} em {cidade} na modalidade masculina de {mod}.")
    print(F"França conseguiu em {ano} {cont_FRAN_F_Speed_Silver} medalhas de {prata} em {cidade} na modalidade feminina de {mod}.")
    print(F"França conseguiu em {ano} {cont_FRAN_M_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade masculina de {mod}.")
    print(F"França conseguiu em {ano} {cont_FRAN_F_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)
    print(F"Reino Unido conseguiu em {ano} {cont_GBR_M_Speed_Gold} medalhas de {ouro}  em {cidade} na modalidade masculina de {mod}.")
    print(F"Reino Unido conseguiu em {ano} {cont_GBR_F_Speed_Gold} medalhas de {ouro}  em {cidade} na modalidade feminina de {mod}.")
    print(F"Reino Unido conseguiu em {ano} {cont_GBR_M_Speed_Silver} medalhas de {prata}  em {cidade} na modalidade masculina de {mod}.")
    print(F"Reino Unido conseguiu em {ano} {cont_GBR_F_Speed_Silver} medalhas de {prata}  em {cidade} na modalidade feminina de {mod}.")
    print(F"Reino Unido conseguiu em {ano} {cont_GBR_M_Speed_bronze} medalhas de {bronze}  em {cidade} na modalidade masculina de {mod}.")
    print(F"Reino Unido conseguiu em {ano} {cont_GBR_F_Speed_bronze} medalhas de {bronze}  em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)
    print(F"Suécia conseguiu em {ano} {cont_SWE_M_Speed_Gold} medalhas de {ouro}  em {cidade} na modalidade masculina de {mod}.")
    print(F"Suécia conseguiu em {ano} {cont_SWE_F_Speed_Gold} medalhas de {ouro}  em {cidade} na modalidade feminina de {mod}.")
    print(F"Suécia conseguiu em {ano} {cont_SWE_M_Speed_Silver} medalhas de {prata}  em {cidade} na modalidade masculina de {mod}.")
    print(F"Suécia conseguiu em {ano} {cont_SWE_F_Speed_Silver} medalhas de {prata}  em {cidade} na modalidade feminina de {mod}.")
    print(F"Suécia conseguiu em {ano} {cont_SWE_M_Speed_bronze} medalhas de {bronze}  em {cidade} na modalidade masculina de {mod}.")
    print(F"Suécia conseguiu em {ano} {cont_SWE_F_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)

def skiing_Sky_1924(ano):
    mod = 'Skiing-Sky Jump'
    cont_Fin_M_Speed_Gold = cont_Fin_F_Speed_Gold = cont_Fin_M_Speed_Silver = cont_Fin_F_Speed_Silver = cont_Fin_M_Speed_bronze = cont_Fin_F_Speed_bronze = 0
    cont_NOR_M_Speed_Gold = cont_NOR_F_Speed_Gold = cont_NOR_M_Speed_Silver = cont_NOR_F_Speed_Silver = cont_NOR_M_Speed_bronze = cont_NOR_F_Speed_bronze = 0
    cont_USA_M_Speed_Gold = cont_USA_F_Speed_Gold = cont_USA_M_Speed_Silver = cont_USA_F_Speed_Silver = cont_USA_M_Speed_bronze = cont_USA_F_Speed_bronze = 0
    cont_AUT_M_Speed_Gold = cont_AUT_F_Speed_Gold = cont_AUT_M_Speed_Silver = cont_AUT_F_Speed_Silver = cont_AUT_M_Speed_bronze = cont_AUT_F_Speed_bronze = 0
    cont_BEL_M_Speed_Gold = cont_BEL_F_Speed_Gold = cont_BEL_M_Speed_Silver = cont_BEL_F_Speed_Silver = cont_BEL_M_Speed_bronze = cont_BEL_F_Speed_bronze = 0
    cont_FRAN_M_Speed_Gold = cont_FRAN_F_Speed_Gold = cont_FRAN_M_Speed_Silver = cont_FRAN_F_Speed_Silver = cont_FRAN_M_Speed_bronze = cont_FRAN_F_Speed_bronze = 0
    cont_GBR_M_Speed_Gold = cont_GBR_F_Speed_Gold = cont_GBR_M_Speed_Silver = cont_GBR_F_Speed_Silver = cont_GBR_M_Speed_bronze = cont_GBR_F_Speed_bronze = 0
    cont_SWE_M_Speed_Gold = cont_SWE_F_Speed_Gold = cont_SWE_M_Speed_Silver = cont_SWE_F_Speed_Silver = cont_SWE_M_Speed_bronze = cont_SWE_F_Speed_bronze = 0
    for l in range(1, len(linhas)):
        colunas = linhas[l].split(',')

        if colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Ski Jumping' and colunas[4] == 'FIN' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_Fin_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Ski Jumping' and colunas[4] == 'FIN' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_Fin_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Ski Jumping' and colunas[4] == 'FIN' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_Fin_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Ski Jumping' and colunas[4] == 'FIN' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_Fin_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Ski Jumping' and colunas[4] == 'FIN' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_Fin_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Ski Jumping' and colunas[4] == 'FIN' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_Fin_F_Speed_bronze += 1

        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Ski Jumping' and colunas[4] == 'NOR' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_NOR_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Ski Jumping' and colunas[4] == 'NOR' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_NOR_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Ski Jumping' and colunas[4] == 'NOR' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_NOR_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Ski Jumping' and colunas[4] == 'NOR' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_NOR_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Ski Jumping' and colunas[4] == 'NOR' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_NOR_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Ski Jumping' and colunas[4] == 'NOR' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_NOR_F_Speed_bronze += 1


        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Ski Jumping' and colunas[4] == 'USA' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_USA_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Ski Jumping' and colunas[4] == 'USA' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_USA_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Ski Jumping' and colunas[4] == 'USA' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_USA_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Ski Jumping' and colunas[4] == 'USA' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_USA_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Ski Jumping' and colunas[4] == 'USA' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_USA_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Ski Jumping' and colunas[4] == 'USA' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_USA_F_Speed_bronze += 1

        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Ski Jumping' and colunas[4] == 'AUT' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_AUT_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Ski Jumping' and colunas[4] == 'AUT' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_AUT_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Ski Jumping' and colunas[4] == 'AUT' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_AUT_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Ski Jumping' and colunas[4] == 'AUT' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_AUT_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Ski Jumping' and colunas[4] == 'AUT' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_AUT_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Ski Jumping' and colunas[4] == 'AUT' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_AUT_F_Speed_bronze += 1

        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Ski Jumping' and colunas[4] == 'BEL' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_BEL_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Ski Jumping' and colunas[4] == 'BEL' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_BEL_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Ski Jumping' and colunas[4] == 'BEL' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_BEL_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Ski Jumping' and colunas[4] == 'BEL' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_BEL_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Ski Jumping' and colunas[4] == 'BEL' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_BEL_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Ski Jumping' and colunas[4] == 'BEL' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_BEL_F_Speed_bronze += 1

        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Ski Jumping' and colunas[4] == 'FRAN' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_FRAN_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Ski Jumping' and colunas[4] == 'FRAN' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_FRAN_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Ski Jumping' and colunas[4] == 'FRAN' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_FRAN_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Ski Jumping' and colunas[4] == 'FRAN' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_FRAN_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Ski Jumping' and colunas[4] == 'FRAN' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_FRAN_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Ski Jumping' and colunas[4] == 'FRAN' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_FRAN_F_Speed_bronze += 1


        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Ski Jumping' and colunas[4] == 'GBR' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_GBR_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Ski Jumping' and colunas[4] == 'GBR' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_GBR_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Ski Jumping' and colunas[4] == 'GBR' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_GBR_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Ski Jumping' and colunas[4] == 'GBR' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_GBR_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Ski Jumping' and colunas[4] == 'GBR' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_GBR_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Ski Jumping' and colunas[4] == 'GBR' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_GBR_F_Speed_bronze += 1

        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Ski Jumping' and colunas[4] == 'GBR' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_SWE_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Ski Jumping' and colunas[4] == 'GBR' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_SWE_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Ski Jumping' and colunas[4] == 'GBR' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_SWE_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Ski Jumping' and colunas[4] == 'GBR' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_SWE_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Ski Jumping' and colunas[4] == 'GBR' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_SWE_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Skiing' and colunas[3] == 'Ski Jumping' and colunas[4] == 'GBR' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_SWE_F_Speed_bronze += 1

    print(F"Finlândia conseguiu em {ano} {cont_Fin_M_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade masculina de {mod}.")
    print(F"Finlândia conseguiu em {ano} {cont_Fin_F_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade feminina de {mod}.")
    print(F"Finlândia conseguiu em {ano} {cont_Fin_M_Speed_Silver} medalhas de {prata} em {cidade} na modalidade masculina de {mod}.")
    print(F"Finlândia conseguiu em {ano} {cont_Fin_F_Speed_Silver} medalhas de {prata} em {cidade} na modalidade feminina de {mod}.")
    print(F"Finlândia conseguiu em {ano} {cont_Fin_M_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade masculina de {mod}.")
    print(F"Finlândia conseguiu em {ano} {cont_Fin_F_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)
    print(F"Noruega conseguiu em {ano} {cont_NOR_M_Speed_Gold} medalhas de {ouro} na modalidade masculina de {mod}.")
    print(F"Noruega conseguiu em {ano} {cont_NOR_F_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade feminina de {mod}.")
    print(F"Noruega conseguiu em {ano} {cont_NOR_M_Speed_Silver} medalhas de {prata} em {cidade} na modalidade masculina de {mod}.")
    print(F"Noruega conseguiu em {ano} {cont_NOR_F_Speed_Silver} medalhas de {prata} em {cidade} na modalidade feminina de {mod}.")
    print(F"Noruega conseguiu em {ano} {cont_NOR_M_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade masculina de {mod}.")
    print(F"Noruega conseguiu em {ano} {cont_NOR_F_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)
    print(F"Estados Unidos conseguiu em {ano} {cont_USA_M_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade masculina de {mod}.")
    print(F"Estados Unidos conseguiu em {ano} {cont_USA_F_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade feminina de {mod}.")
    print(F"Estados Unidos conseguiu em {ano} {cont_USA_M_Speed_Silver} medalhas de {prata} em {cidade} na modalidade masculina de {mod}.")
    print(F"Estados Unidos conseguiu em {ano} {cont_USA_F_Speed_Silver} medalhas de {prata} em {cidade} na modalidade feminina de {mod}.")
    print(F"Estados Unidos conseguiu em {ano} {cont_USA_M_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade masculina de {mod}.")
    print(F"Estados Unidos em conseguiu em {ano} {cont_USA_F_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)
    print(F"Austria conseguiu em {ano} {cont_AUT_M_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade masculina de {mod}.")
    print(F"Austria conseguiu em {ano} {cont_AUT_F_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade feminina de {mod}.")
    print(F"Austria conseguiu em {ano} {cont_AUT_M_Speed_Silver} medalhas de {prata} em {cidade} na modalidade masculina de {mod}.")
    print(F"Austria conseguiu em {ano} {cont_AUT_F_Speed_Silver} medalhas de {prata} em {cidade} na modalidade feminina de {mod}.")
    print(F"Austria conseguiu em {ano} {cont_AUT_M_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade masculina de {mod}.")
    print(F"Austria conseguiu em {ano} {cont_AUT_F_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)
    print(F"Bélgica conseguiu em {ano} {cont_BEL_M_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade masculina de {mod}.")
    print(F"Bélgica conseguiu em {ano} {cont_BEL_F_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade feminina de {mod}.")
    print(F"Bélgica conseguiu em {ano} {cont_BEL_F_Speed_Silver} medalhas de {prata} em {cidade} na modalidade feminina de {mod}.")
    print(F"Bélgica conseguiu em {ano} {cont_BEL_M_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade masculina de {mod}.")
    print(F"Bélgica conseguiu em {ano} {cont_BEL_F_Speed_bronze} medalhas de {bronze}  em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)
    print(F"França conseguiu em {ano} {cont_FRAN_M_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade masculina de {mod}.")
    print(F"França conseguiu em {ano} {cont_FRAN_F_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade feminina de {mod}.")
    print(F"França conseguiu em {ano} {cont_FRAN_M_Speed_Silver} medalhas de {prata} em {cidade} na modalidade masculina de {mod}.")
    print(F"França conseguiu em {ano} {cont_FRAN_F_Speed_Silver} medalhas de {prata} em {cidade} na modalidade feminina de {mod}.")
    print(F"França conseguiu em {ano} {cont_FRAN_M_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade masculina de {mod}.")
    print(F"França conseguiu em {ano} {cont_FRAN_F_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)
    print(F"Reino Unido conseguiu em {ano} {cont_GBR_M_Speed_Gold} medalhas de {ouro}  em {cidade} na modalidade masculina de {mod}.")
    print(F"Reino Unido conseguiu em {ano} {cont_GBR_F_Speed_Gold} medalhas de {ouro}  em {cidade} na modalidade feminina de {mod}.")
    print(F"Reino Unido conseguiu em {ano} {cont_GBR_M_Speed_Silver} medalhas de {prata}  em {cidade} na modalidade masculina de {mod}.")
    print(F"Reino Unido conseguiu em {ano} {cont_GBR_F_Speed_Silver} medalhas de {prata}  em {cidade} na modalidade feminina de {mod}.")
    print(F"Reino Unido conseguiu em {ano} {cont_GBR_M_Speed_bronze} medalhas de {bronze}  em {cidade} na modalidade masculina de {mod}.")
    print(F"Reino Unido conseguiu em {ano} {cont_GBR_F_Speed_bronze} medalhas de {bronze}  em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)
    print(F"Suécia conseguiu em {ano} {cont_SWE_M_Speed_Gold} medalhas de {ouro}  em {cidade} na modalidade masculina de {mod}.")
    print(F"Suécia conseguiu em {ano} {cont_SWE_F_Speed_Gold} medalhas de {ouro}  em {cidade} na modalidade feminina de {mod}.")
    print(F"Suécia conseguiu em {ano} {cont_SWE_M_Speed_Silver} medalhas de {prata}  em {cidade} na modalidade masculina de {mod}.")
    print(F"Suécia conseguiu em {ano} {cont_SWE_F_Speed_Silver} medalhas de {prata}  em {cidade} na modalidade feminina de {mod}.")
    print(F"Suécia conseguiu em {ano} {cont_SWE_M_Speed_bronze} medalhas de {bronze}  em {cidade} na modalidade masculina de {mod}.")
    print(F"Suécia conseguiu em {ano} {cont_SWE_F_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)


def Bobsleight(ano):
    mod = 'Bobsleight'
    cont_Fin_M_Speed_Gold = cont_Fin_F_Speed_Gold = cont_Fin_M_Speed_Silver = cont_Fin_F_Speed_Silver = cont_Fin_M_Speed_bronze = cont_Fin_F_Speed_bronze = 0
    cont_NOR_M_Speed_Gold = cont_NOR_F_Speed_Gold = cont_NOR_M_Speed_Silver = cont_NOR_F_Speed_Silver = cont_NOR_M_Speed_bronze = cont_NOR_F_Speed_bronze = 0
    cont_USA_M_Speed_Gold = cont_USA_F_Speed_Gold = cont_USA_M_Speed_Silver = cont_USA_F_Speed_Silver = cont_USA_M_Speed_bronze = cont_USA_F_Speed_bronze = 0
    cont_AUT_M_Speed_Gold = cont_AUT_F_Speed_Gold = cont_AUT_M_Speed_Silver = cont_AUT_F_Speed_Silver = cont_AUT_M_Speed_bronze = cont_AUT_F_Speed_bronze = 0
    cont_BEL_M_Speed_Gold = cont_BEL_F_Speed_Gold = cont_BEL_M_Speed_Silver = cont_BEL_F_Speed_Silver = cont_BEL_M_Speed_bronze = cont_BEL_F_Speed_bronze = 0
    cont_FRAN_M_Speed_Gold = cont_FRAN_F_Speed_Gold = cont_FRAN_M_Speed_Silver = cont_FRAN_F_Speed_Silver = cont_FRAN_M_Speed_bronze = cont_FRAN_F_Speed_bronze = 0
    cont_GBR_M_Speed_Gold = cont_GBR_F_Speed_Gold = cont_GBR_M_Speed_Silver = cont_GBR_F_Speed_Silver = cont_GBR_M_Speed_bronze = cont_GBR_F_Speed_bronze = 0
    cont_SWE_M_Speed_Gold = cont_SWE_F_Speed_Gold = cont_SWE_M_Speed_Silver = cont_SWE_F_Speed_Silver = cont_SWE_M_Speed_bronze = cont_SWE_F_Speed_bronze = 0
    for l in range(1, len(linhas)):
        colunas = linhas[l].split(',')

        if colunas[0] == ano and colunas[2] == 'Bobsleigh' and colunas[3] == 'Bobsleigh' and colunas[4] == 'FIN' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_Fin_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Bobsleigh' and colunas[3] == 'Bobsleigh' and colunas[4] == 'FIN' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_Fin_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Bobsleigh' and colunas[3] == 'Bobsleigh' and colunas[4] == 'FIN' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_Fin_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Bobsleigh' and colunas[3] == 'Bobsleigh' and colunas[4] == 'FIN' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_Fin_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Bobsleigh' and colunas[3] == 'Bobsleigh' and colunas[4] == 'FIN' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_Fin_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Bobsleigh' and colunas[3] == 'Bobsleigh' and colunas[4] == 'FIN' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_Fin_F_Speed_bronze += 1

        elif colunas[0] == ano and colunas[2] == 'Bobsleigh' and colunas[3] == 'Bobsleigh' and colunas[4] == 'NOR' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_NOR_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Bobsleigh' and colunas[3] == 'Bobsleigh' and colunas[4] == 'NOR' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_NOR_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Bobsleigh' and colunas[3] == 'Bobsleigh' and colunas[4] == 'NOR' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_NOR_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Bobsleigh' and colunas[3] == 'Bobsleigh' and colunas[4] == 'NOR' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_NOR_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Bobsleigh' and colunas[3] == 'Bobsleigh' and colunas[4] == 'NOR' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_NOR_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Bobsleigh' and colunas[3] == 'Bobsleigh' and colunas[4] == 'NOR' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_NOR_F_Speed_bronze += 1


        elif colunas[0] == ano and colunas[2] == 'Bobsleigh' and colunas[3] == 'Bobsleigh' and colunas[4] == 'USA' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_USA_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Bobsleigh' and colunas[3] == 'Bobsleigh' and colunas[4] == 'USA' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_USA_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Bobsleigh' and colunas[3] == 'Bobsleigh' and colunas[4] == 'USA' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_USA_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Bobsleigh' and colunas[3] == 'Bobsleigh' and colunas[4] == 'USA' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_USA_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Bobsleigh' and colunas[3] == 'Bobsleigh' and colunas[4] == 'USA' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_USA_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Bobsleigh' and colunas[3] == 'Bobsleigh' and colunas[4] == 'USA' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_USA_F_Speed_bronze += 1

        elif colunas[0] == ano and colunas[2] == 'Bobsleigh' and colunas[3] == 'Bobsleigh' and colunas[4] == 'AUT' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_AUT_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Bobsleigh' and colunas[3] == 'Bobsleigh' and colunas[4] == 'AUT' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_AUT_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Bobsleigh' and colunas[3] == 'Bobsleigh' and colunas[4] == 'AUT' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_AUT_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Bobsleigh' and colunas[3] == 'Bobsleigh' and colunas[4] == 'AUT' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_AUT_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Bobsleigh' and colunas[3] == 'Bobsleigh' and colunas[4] == 'AUT' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_AUT_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Bobsleigh' and colunas[3] == 'Bobsleigh' and colunas[4] == 'AUT' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_AUT_F_Speed_bronze += 1

        elif colunas[0] == ano and colunas[2] == 'Bobsleigh' and colunas[3] == 'Bobsleigh' and colunas[4] == 'BEL' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_BEL_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Bobsleigh' and colunas[3] == 'Bobsleigh' and colunas[4] == 'BEL' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_BEL_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Bobsleigh' and colunas[3] == 'Bobsleigh' and colunas[4] == 'BEL' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_BEL_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Bobsleigh' and colunas[3] == 'Bobsleigh' and colunas[4] == 'BEL' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_BEL_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Bobsleigh' and colunas[3] == 'Bobsleigh' and colunas[4] == 'BEL' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_BEL_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Bobsleigh' and colunas[3] == 'Bobsleigh' and colunas[4] == 'BEL' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_BEL_F_Speed_bronze += 1

        elif colunas[0] == ano and colunas[2] == 'Bobsleigh' and colunas[3] == 'Bobsleigh' and colunas[4] == 'FRAN' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_FRAN_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Bobsleigh' and colunas[3] == 'Bobsleigh' and colunas[4] == 'FRAN' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_FRAN_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Bobsleigh' and colunas[3] == 'Bobsleigh' and colunas[4] == 'FRAN' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_FRAN_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Bobsleigh' and colunas[3] == 'Bobsleigh' and colunas[4] == 'FRAN' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_FRAN_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Bobsleigh' and colunas[3] == 'Bobsleigh' and colunas[4] == 'FRAN' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_FRAN_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Bobsleigh' and colunas[3] == 'Bobsleigh' and colunas[4] == 'FRAN' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_FRAN_F_Speed_bronze += 1

        elif colunas[0] == ano and colunas[2] == 'Bobsleigh' and colunas[3] == 'Bobsleigh' and colunas[4] == 'GBR' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_GBR_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Bobsleigh' and colunas[3] == 'Bobsleigh' and colunas[4] == 'GBR' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_GBR_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Bobsleigh' and colunas[3] == 'Bobsleigh' and colunas[4] == 'GBR' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_GBR_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Bobsleigh' and colunas[3] == 'Bobsleigh' and colunas[4] == 'GBR' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_GBR_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Bobsleigh' and colunas[3] == 'Bobsleigh' and colunas[4] == 'GBR' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_GBR_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Bobsleigh' and colunas[3] == 'Bobsleigh' and colunas[4] == 'GBR' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_GBR_F_Speed_bronze += 1

        elif colunas[0] == ano and colunas[2] == 'Bobsleigh' and colunas[3] == 'Bobsleigh' and colunas[4] == 'GBR' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_SWE_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Bobsleigh' and colunas[3] == 'Bobsleigh' and colunas[4] == 'GBR' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_SWE_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Bobsleigh' and colunas[3] == 'Bobsleigh' and colunas[4] == 'GBR' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_SWE_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Bobsleigh' and colunas[3] == 'Bobsleigh' and colunas[4] == 'GBR' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_SWE_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Bobsleigh' and colunas[3] == 'Bobsleigh' and colunas[4] == 'GBR' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_SWE_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Bobsleigh' and colunas[3] == 'Bobsleigh' and colunas[4] == 'GBR' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_SWE_F_Speed_bronze += 1

    print(F"Finlândia conseguiu em {ano} {cont_Fin_M_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade masculina de {mod}.")
    print(F"Finlândia conseguiu em {ano} {cont_Fin_F_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade feminina de {mod}.")
    print(F"Finlândia conseguiu em {ano} {cont_Fin_M_Speed_Silver} medalhas de {prata} em {cidade} na modalidade masculina de {mod}.")
    print(F"Finlândia conseguiu em {ano} {cont_Fin_F_Speed_Silver} medalhas de {prata} em {cidade} na modalidade feminina de {mod}.")
    print(F"Finlândia conseguiu em {ano} {cont_Fin_M_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade masculina de {mod}.")
    print(F"Finlândia conseguiu em {ano} {cont_Fin_F_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)
    print(F"Noruega conseguiu em {ano} {cont_NOR_M_Speed_Gold} medalhas de {ouro} na modalidade masculina de {mod}.")
    print(F"Noruega conseguiu em {ano} {cont_NOR_F_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade feminina de {mod}.")
    print(F"Noruega conseguiu em {ano} {cont_NOR_M_Speed_Silver} medalhas de {prata} em {cidade} na modalidade masculina de {mod}.")
    print(F"Noruega conseguiu em {ano} {cont_NOR_F_Speed_Silver} medalhas de {prata} em {cidade} na modalidade feminina de {mod}.")
    print(F"Noruega conseguiu em {ano} {cont_NOR_M_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade masculina de {mod}.")
    print(F"Noruega conseguiu em {ano} {cont_NOR_F_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)
    print(F"Estados Unidos conseguiu em {ano} {cont_USA_M_Speed_Gold} medalhas de {ouro}em {cidade} na modalidade masculina de {mod}.")
    print(F"Estados Unidos conseguiu em {ano} {cont_USA_F_Speed_Gold} medalhas de {ouro}em {cidade} na modalidade feminina de {mod}.")
    print(F"Estados Unidos conseguiu em {ano} {cont_USA_M_Speed_Silver} medalhas de {prata}em {cidade} na modalidade masculina de {mod}.")
    print(F"Estados Unidos conseguiu em {ano} {cont_USA_F_Speed_Silver} medalhas de {prata}em {cidade} na modalidade feminina de {mod}.")
    print(F"Estados Unidos conseguiu em {ano} {cont_USA_M_Speed_bronze} medalhas de {bronze}em {cidade} na modalidade masculina de {mod}.")
    print(F"Estados Unidos em conseguiu em {ano} {cont_USA_F_Speed_bronze} medalhas de {bronze}em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)
    print(F"Austria conseguiu em {ano} {cont_AUT_M_Speed_Gold} medalhas de {ouro}em {cidade} na modalidade masculina de {mod}.")
    print(F"Austria conseguiu em {ano} {cont_AUT_F_Speed_Gold} medalhas de {ouro}em {cidade} na modalidade feminina de {mod}.")
    print(F"Austria conseguiu em {ano} {cont_AUT_M_Speed_Silver} medalhas de {prata}em {cidade} na modalidade masculina de {mod}.")
    print(F"Austria conseguiu em {ano} {cont_AUT_F_Speed_Silver} medalhas de {prata}em {cidade} na modalidade feminina de {mod}.")
    print(F"Austria conseguiu em {ano} {cont_AUT_M_Speed_bronze} medalhas de {bronze}em {cidade} na modalidade masculina de {mod}.")
    print(F"Austria conseguiu em {ano} {cont_AUT_F_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)
    print(F"Bélgica conseguiu em {ano} {cont_BEL_M_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade masculina de {mod}.")
    print(F"Bélgica conseguiu em {ano} {cont_BEL_F_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade feminina de {mod}.")
    print(F"Bélgica conseguiu em {ano} {cont_BEL_F_Speed_Silver} medalhas de {prata} em {cidade} na modalidade feminina de {mod}.")
    print(F"Bélgica conseguiu em {ano} {cont_BEL_M_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade masculina de {mod}.")
    print(F"Bélgica conseguiu em {ano} {cont_BEL_F_Speed_bronze} medalhas de {bronze}  em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)
    print(F"França conseguiu em {ano} {cont_FRAN_M_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade masculina de {mod}.")
    print(F"França conseguiu em {ano} {cont_FRAN_F_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade feminina de {mod}.")
    print(F"França conseguiu em {ano} {cont_FRAN_M_Speed_Silver} medalhas de {prata} em {cidade} na modalidade masculina de {mod}.")
    print(F"França conseguiu em {ano} {cont_FRAN_F_Speed_Silver} medalhas de {prata} em {cidade} na modalidade feminina de {mod}.")
    print(F"França conseguiu em {ano} {cont_FRAN_M_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade masculina de {mod}.")
    print(F"França conseguiu em {ano} {cont_FRAN_F_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)
    print(F"Reino Unido conseguiu em {ano} {cont_GBR_M_Speed_Gold} medalhas de {ouro}  em {cidade} na modalidade masculina de {mod}.")
    print(F"Reino Unido conseguiu em {ano} {cont_GBR_F_Speed_Gold} medalhas de {ouro}  em {cidade} na modalidade feminina de {mod}.")
    print(F"Reino Unido conseguiu em {ano} {cont_GBR_M_Speed_Silver} medalhas de {prata}  em {cidade} na modalidade masculina de {mod}.")
    print(F"Reino Unido conseguiu em {ano} {cont_GBR_F_Speed_Silver} medalhas de {prata}  em {cidade} na modalidade feminina de {mod}.")
    print(F"Reino Unido conseguiu em {ano} {cont_GBR_M_Speed_bronze} medalhas de {bronze}  em {cidade} na modalidade masculina de {mod}.")
    print(F"Reino Unido conseguiu em {ano} {cont_GBR_F_Speed_bronze} medalhas de {bronze}  em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)
    print(F"Suécia conseguiu em {ano} {cont_SWE_M_Speed_Gold} medalhas de {ouro}  em {cidade} na modalidade masculina de {mod}.")
    print(F"Suécia conseguiu em {ano} {cont_SWE_F_Speed_Gold} medalhas de {ouro}  em {cidade} na modalidade feminina de {mod}.")
    print(F"Suécia conseguiu em {ano} {cont_SWE_M_Speed_Silver} medalhas de {prata}  em {cidade} na modalidade masculina de {mod}.")
    print(F"Suécia conseguiu em {ano} {cont_SWE_F_Speed_Silver} medalhas de {prata}  em {cidade} na modalidade feminina de {mod}.")
    print(F"Suécia conseguiu em {ano} {cont_SWE_M_Speed_bronze} medalhas de {bronze}  em {cidade} na modalidade masculina de {mod}.")
    print(F"Suécia conseguiu em {ano} {cont_SWE_F_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)


def Ice_Hockey(ano):
    mod = 'Ice Hockey'
    cont_Fin_M_Speed_Gold = cont_Fin_F_Speed_Gold = cont_Fin_M_Speed_Silver = cont_Fin_F_Speed_Silver = cont_Fin_M_Speed_bronze = cont_Fin_F_Speed_bronze = 0
    cont_NOR_M_Speed_Gold = cont_NOR_F_Speed_Gold = cont_NOR_M_Speed_Silver = cont_NOR_F_Speed_Silver = cont_NOR_M_Speed_bronze = cont_NOR_F_Speed_bronze = 0
    cont_USA_M_Speed_Gold = cont_USA_F_Speed_Gold = cont_USA_M_Speed_Silver = cont_USA_F_Speed_Silver = cont_USA_M_Speed_bronze = cont_USA_F_Speed_bronze = 0
    cont_AUT_M_Speed_Gold = cont_AUT_F_Speed_Gold = cont_AUT_M_Speed_Silver = cont_AUT_F_Speed_Silver = cont_AUT_M_Speed_bronze = cont_AUT_F_Speed_bronze = 0
    cont_BEL_M_Speed_Gold = cont_BEL_F_Speed_Gold = cont_BEL_M_Speed_Silver = cont_BEL_F_Speed_Silver = cont_BEL_M_Speed_bronze = cont_BEL_F_Speed_bronze = 0
    cont_FRAN_M_Speed_Gold = cont_FRAN_F_Speed_Gold = cont_FRAN_M_Speed_Silver = cont_FRAN_F_Speed_Silver = cont_FRAN_M_Speed_bronze = cont_FRAN_F_Speed_bronze = 0
    cont_GBR_M_Speed_Gold = cont_GBR_F_Speed_Gold = cont_GBR_M_Speed_Silver = cont_GBR_F_Speed_Silver = cont_GBR_M_Speed_bronze = cont_GBR_F_Speed_bronze = 0
    cont_SWE_M_Speed_Gold = cont_SWE_F_Speed_Gold = cont_SWE_M_Speed_Silver = cont_SWE_F_Speed_Silver = cont_SWE_M_Speed_bronze = cont_SWE_F_Speed_bronze = 0
    for l in range(1, len(linhas)):
        colunas = linhas[l].split(',')

        if colunas[0] == ano and colunas[2] == 'Ice Hockey' and colunas[3] == 'Ice Hockey' and colunas[4] == 'FIN' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_Fin_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Ice Hockey' and colunas[3] == 'Ice Hockey' and colunas[4] == 'FIN' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_Fin_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Ice Hockey' and colunas[3] == 'Ice Hockey' and colunas[4] == 'FIN' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_Fin_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Ice Hockey' and colunas[3] == 'Ice Hockey' and colunas[4] == 'FIN' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_Fin_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Ice Hockey' and colunas[3] == 'Ice Hockey' and colunas[4] == 'FIN' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_Fin_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Ice Hockey' and colunas[3] == 'Ice Hockey' and colunas[4] == 'FIN' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_Fin_F_Speed_bronze += 1

        elif colunas[0] == ano and colunas[2] == 'Ice Hockey' and colunas[3] == 'Ice Hockey' and colunas[4] == 'NOR' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_NOR_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Ice Hockey' and colunas[3] == 'Ice Hockey' and colunas[4] == 'NOR' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_NOR_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Ice Hockey' and colunas[3] == 'Ice Hockey' and colunas[4] == 'NOR' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_NOR_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Ice Hockey' and colunas[3] == 'Ice Hockey' and colunas[4] == 'NOR' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_NOR_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Ice Hockey' and colunas[3] == 'Ice Hockey' and colunas[4] == 'NOR' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_NOR_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Ice Hockey' and colunas[3] == 'Ice Hockey' and colunas[4] == 'NOR' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_NOR_F_Speed_bronze += 1


        elif colunas[0] == ano and colunas[2] == 'Ice Hockey' and colunas[3] == 'Ice Hockey' and colunas[4] == 'USA' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_USA_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Ice Hockey' and colunas[3] == 'Ice Hockey' and colunas[4] == 'USA' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_USA_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Ice Hockey' and colunas[3] == 'Ice Hockey' and colunas[4] == 'USA' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_USA_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Ice Hockey' and colunas[3] == 'Ice Hockey' and colunas[4] == 'USA' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_USA_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Ice Hockey' and colunas[3] == 'Ice Hockey' and colunas[4] == 'USA' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_USA_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Ice Hockey' and colunas[3] == 'Ice Hockey' and colunas[4] == 'USA' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_USA_F_Speed_bronze += 1

        elif colunas[0] == ano and colunas[2] == 'Ice Hockey' and colunas[3] == 'Ice Hockey' and colunas[4] == 'AUT' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_AUT_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Ice Hockey' and colunas[3] == 'Ice Hockey' and colunas[4] == 'AUT' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_AUT_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Ice Hockey' and colunas[3] == 'Ice Hockey' and colunas[4] == 'AUT' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_AUT_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Ice Hockey' and colunas[3] == 'Ice Hockey' and colunas[4] == 'AUT' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_AUT_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Ice Hockey' and colunas[3] == 'Ice Hockey' and colunas[4] == 'AUT' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_AUT_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Ice Hockey' and colunas[3] == 'Ice Hockey' and colunas[4] == 'AUT' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_AUT_F_Speed_bronze += 1

        elif colunas[0] == ano and colunas[2] == 'Ice Hockey' and colunas[3] == 'Ice Hockey' and colunas[4] == 'BEL' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_BEL_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Ice Hockey' and colunas[3] == 'Ice Hockey' and colunas[4] == 'BEL' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_BEL_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Ice Hockey' and colunas[3] == 'Ice Hockey' and colunas[4] == 'BEL' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_BEL_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Ice Hockey' and colunas[3] == 'Ice Hockey' and colunas[4] == 'BEL' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_BEL_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Ice Hockey' and colunas[3] == 'Ice Hockey' and colunas[4] == 'BEL' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_BEL_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Ice Hockey' and colunas[3] == 'Ice Hockey' and colunas[4] == 'BEL' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_BEL_F_Speed_bronze += 1

        elif colunas[0] == ano and colunas[2] == 'Ice Hockey' and colunas[3] == 'Ice Hockey' and colunas[4] == 'FRAN' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_FRAN_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Ice Hockey' and colunas[3] == 'Ice Hockey' and colunas[4] == 'FRAN' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_FRAN_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Ice Hockey' and colunas[3] == 'Ice Hockey' and colunas[4] == 'FRAN' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_FRAN_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Ice Hockey' and colunas[3] == 'Ice Hockey' and colunas[4] == 'FRAN' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_FRAN_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Ice Hockey' and colunas[3] == 'Ice Hockey' and colunas[4] == 'FRAN' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_FRAN_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Ice Hockey' and colunas[3] == 'Ice Hockey' and colunas[4] == 'FRAN' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_FRAN_F_Speed_bronze += 1

        elif colunas[0] == ano and colunas[2] == 'Ice Hockey' and colunas[3] == 'Ice Hockey' and colunas[4] == 'GBR' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_GBR_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Ice Hockey' and colunas[3] == 'Ice Hockey' and colunas[4] == 'GBR' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_GBR_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Ice Hockey' and colunas[3] == 'Ice Hockey' and colunas[4] == 'GBR' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_GBR_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Ice Hockey' and colunas[3] == 'Ice Hockey' and colunas[4] == 'GBR' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_GBR_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Ice Hockey' and colunas[3] == 'Ice Hockey' and colunas[4] == 'GBR' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_GBR_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Ice Hockey' and colunas[3] == 'Ice Hockey' and colunas[4] == 'GBR' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_GBR_F_Speed_bronze += 1

        elif colunas[0] == ano and colunas[2] == 'Ice Hockey' and colunas[3] == 'Ice Hockey' and colunas[4] == 'GBR' and colunas[6] == 'M' and colunas[7] =='Gold':
            cont_SWE_M_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Ice Hockey' and colunas[3] == 'Ice Hockey' and colunas[4] == 'GBR' and colunas[6] == 'W' and colunas[7] =='Gold':
            cont_SWE_F_Speed_Gold += 1
        elif colunas[0] == ano and colunas[2] == 'Ice Hockey' and colunas[3] == 'Ice Hockey' and colunas[4] == 'GBR' and colunas[6] == 'M' and colunas[7] =='Silver':
            cont_SWE_M_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Ice Hockey' and colunas[3] == 'Ice Hockey' and colunas[4] == 'GBR' and colunas[6] == 'W' and colunas[7] =='Silver':
            cont_SWE_F_Speed_Silver += 1
        elif colunas[0] == ano and colunas[2] == 'Ice Hockey' and colunas[3] == 'Ice Hockey' and colunas[4] == 'GBR' and colunas[6] == 'M' and colunas[7] =='Bronze':
            cont_SWE_M_Speed_bronze += 1
        elif colunas[0] == ano and colunas[2] == 'Ice Hockey' and colunas[3] == 'Ice Hockey' and colunas[4] == 'GBR' and colunas[6] == 'W' and colunas[7] =='Bronze':
            cont_SWE_F_Speed_bronze += 1


    print(F"Finlândia conseguiu em {ano} {cont_Fin_M_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade masculina de {mod}.")
    print(F"Finlândia conseguiu em {ano} {cont_Fin_F_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade feminina de {mod}.")
    print(F"Finlândia conseguiu em {ano} {cont_Fin_M_Speed_Silver} medalhas de {prata} em {cidade} na modalidade masculina de {mod}.")
    print(F"Finlândia conseguiu em {ano} {cont_Fin_F_Speed_Silver} medalhas de {prata} em {cidade} na modalidade feminina de {mod}.")
    print(F"Finlândia conseguiu em {ano} {cont_Fin_M_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade masculina de {mod}.")
    print(F"Finlândia conseguiu em {ano} {cont_Fin_F_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)
    print(F"Noruega conseguiu em {ano} {cont_NOR_M_Speed_Gold} medalhas de {ouro} na modalidade masculina de {mod}.")
    print(F"Noruega conseguiu em {ano} {cont_NOR_F_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade feminina de {mod}.")
    print(F"Noruega conseguiu em {ano} {cont_NOR_M_Speed_Silver} medalhas de {prata} em {cidade} na modalidade masculina de {mod}.")
    print(F"Noruega conseguiu em {ano} {cont_NOR_F_Speed_Silver} medalhas de {prata} em {cidade} na modalidade feminina de {mod}.")
    print(F"Noruega conseguiu em {ano} {cont_NOR_M_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade masculina de {mod}.")
    print(F"Noruega conseguiu em {ano} {cont_NOR_F_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)
    print(F"Estados Unidos conseguiu em {ano} {cont_USA_M_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade masculina de {mod}.")
    print(F"Estados Unidos conseguiu em {ano} {cont_USA_F_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade feminina de {mod}.")
    print(F"Estados Unidos conseguiu em {ano} {cont_USA_M_Speed_Silver} medalhas de {prata} em {cidade} na modalidade masculina de {mod}.")
    print(F"Estados Unidos conseguiu em {ano} {cont_USA_F_Speed_Silver} medalhas de {prata} em {cidade} na modalidade feminina de {mod}.")
    print(F"Estados Unidos conseguiu em {ano} {cont_USA_M_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade masculina de {mod}.")
    print(F"Estados Unidos em conseguiu em {ano} {cont_USA_F_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)
    print(F"Austria conseguiu em {ano} {cont_AUT_M_Speed_Gold} medalhas de {ouro}em {cidade} na modalidade masculina de {mod}.")
    print(F"Austria conseguiu em {ano} {cont_AUT_F_Speed_Gold} medalhas de {ouro}em {cidade} na modalidade feminina de {mod}.")
    print(F"Austria conseguiu em {ano} {cont_AUT_M_Speed_Silver} medalhas de {prata}em {cidade} na modalidade masculina de {mod}.")
    print(F"Austria conseguiu em {ano} {cont_AUT_F_Speed_Silver} medalhas de {prata}em {cidade} na modalidade feminina de {mod}.")
    print(F"Austria conseguiu em {ano} {cont_AUT_M_Speed_bronze} medalhas de {bronze}em {cidade} na modalidade masculina de {mod}.")
    print(F"Austria conseguiu em {ano} {cont_AUT_F_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)
    print(F"Bélgica conseguiu em {ano} {cont_BEL_M_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade masculina de {mod}.")
    print(F"Bélgica conseguiu em {ano} {cont_BEL_F_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade feminina de {mod}.")
    print(F"Bélgica conseguiu em {ano} {cont_BEL_F_Speed_Silver} medalhas de {prata} em {cidade} na modalidade feminina de {mod}.")
    print(F"Bélgica conseguiu em {ano} {cont_BEL_M_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade masculina de {mod}.")
    print(F"Bélgica conseguiu em {ano} {cont_BEL_F_Speed_bronze} medalhas de {bronze}  em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)
    print(F"França conseguiu em {ano} {cont_FRAN_M_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade masculina de {mod}.")
    print(F"França conseguiu em {ano} {cont_FRAN_F_Speed_Gold} medalhas de {ouro} em {cidade} na modalidade feminina de {mod}.")
    print(F"França conseguiu em {ano} {cont_FRAN_M_Speed_Silver} medalhas de {prata} em {cidade} na modalidade masculina de {mod}.")
    print(F"França conseguiu em {ano} {cont_FRAN_F_Speed_Silver} medalhas de {prata} em {cidade} na modalidade feminina de {mod}.")
    print(F"França conseguiu em {ano} {cont_FRAN_M_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade masculina de {mod}.")
    print(F"França conseguiu em {ano} {cont_FRAN_F_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)
    print(F"Reino Unido conseguiu em {ano} {cont_GBR_M_Speed_Gold} medalhas de {ouro}  em {cidade} na modalidade masculina de {mod}.")
    print(F"Reino Unido conseguiu em {ano} {cont_GBR_F_Speed_Gold} medalhas de {ouro}  em {cidade} na modalidade feminina de {mod}.")
    print(F"Reino Unido conseguiu em {ano} {cont_GBR_M_Speed_Silver} medalhas de {prata}  em {cidade} na modalidade masculina de {mod}.")
    print(F"Reino Unido conseguiu em {ano} {cont_GBR_F_Speed_Silver} medalhas de {prata}  em {cidade} na modalidade feminina de {mod}.")
    print(F"Reino Unido conseguiu em {ano} {cont_GBR_M_Speed_bronze} medalhas de {bronze}  em {cidade} na modalidade masculina de {mod}.")
    print(F"Reino Unido conseguiu em {ano} {cont_GBR_F_Speed_bronze} medalhas de {bronze}  em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)
    print(F"Suécia conseguiu em {ano} {cont_SWE_M_Speed_Gold} medalhas de {ouro}  em {cidade} na modalidade masculina de {mod}.")
    print(F"Suécia conseguiu em {ano} {cont_SWE_F_Speed_Gold} medalhas de {ouro}  em {cidade} na modalidade feminina de {mod}.")
    print(F"Suécia conseguiu em {ano} {cont_SWE_M_Speed_Silver} medalhas de {prata}  em {cidade} na modalidade masculina de {mod}.")
    print(F"Suécia conseguiu em {ano} {cont_SWE_F_Speed_Silver} medalhas de {prata}  em {cidade} na modalidade feminina de {mod}.")
    print(F"Suécia conseguiu em {ano} {cont_SWE_M_Speed_bronze} medalhas de {bronze}  em {cidade} na modalidade masculina de {mod}.")
    print(F"Suécia conseguiu em {ano} {cont_SWE_F_Speed_bronze} medalhas de {bronze} em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)



def ano_1924(ano):
    dados_1924_Skating_Speed(ano)
    dados_1924_Skating_figure(ano)
    curling_1924(ano)
    skiing_1924(ano)
    skiing_Nordic_1924(ano)
    skiing_Sky_1924(ano)
    Bobsleight(ano)
    Ice_Hockey(ano)
ano = str(input("Digite um ano da olimpíada a partir de 1924: "))

for l in range(1, len(linhas)):
    colunas = linhas[l].split(',')
    if colunas[0] == ano:
        cidade = colunas[1]
ano_1924(ano)