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

def Ice_Hockey(ano,cidade):
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


    print(F"Finlândia conseguiu em {ano} {cont_Fin_M_Speed_Gold} medalhas de {ouro}em {cidade} na modalidade masculina de {mod}.")
    print(F"Finlândia conseguiu em {ano} {cont_Fin_F_Speed_Gold} medalhas de {ouro}em {cidade} na modalidade feminina de {mod}.")
    print(F"Finlândia conseguiu em {ano} {cont_Fin_M_Speed_Silver} medalhas de {prata}em {cidade} na modalidade masculina de {mod}.")
    print(F"Finlândia conseguiu em {ano} {cont_Fin_F_Speed_Silver} medalhas de {prata}em {cidade} na modalidade feminina de {mod}.")
    print(F"Finlândia conseguiu em {ano} {cont_Fin_M_Speed_bronze} medalhas de {bronze}em {cidade} na modalidade masculina de {mod}.")
    print(F"Finlândia conseguiu em {ano} {cont_Fin_F_Speed_bronze} medalhas de {bronze}em {cidade} na modalidade feminina de {mod}.")
    print('-'*90)
    print(F"Noruega conseguiu em {ano} {cont_NOR_M_Speed_Gold} medalhas de {ouro} na modalidade masculina de {mod}.")
    print(F"Noruega conseguiu em {ano} {cont_NOR_F_Speed_Gold} medalhas de {ouro}em {cidade} na modalidade feminina de {mod}.")
    print(F"Noruega conseguiu em {ano} {cont_NOR_M_Speed_Silver} medalhas de {prata}em {cidade} na modalidade masculina de {mod}.")
    print(F"Noruega conseguiu em {ano} {cont_NOR_F_Speed_Silver} medalhas de {prata}em {cidade} na modalidade feminina de {mod}.")
    print(F"Noruega conseguiu em {ano} {cont_NOR_M_Speed_bronze} medalhas de {bronze}em {cidade} na modalidade masculina de {mod}.")
    print(F"Noruega conseguiu em {ano} {cont_NOR_F_Speed_bronze} medalhas de {bronze}em {cidade} na modalidade feminina de {mod}.")
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

datas=['1924','1928','','','','','','','','','','','','','','','','','','']
ano = str(input("Digite um ano da olimpíada a partir de 1924: "))

for l in range(1, len(linhas)):
    colunas = linhas[l].split(',')
    if colunas[0] == ano:
        cidade = colunas[1]

Ice_Hockey(ano,cidade)


