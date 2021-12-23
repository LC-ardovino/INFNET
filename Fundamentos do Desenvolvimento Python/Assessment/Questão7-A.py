#Dentre os seguintes países nórdicos: Suécia, Dinamarca e Noruega, verifique: No século XXI (a partir de 2001), qual foi o maior medalhista de ouro, considerando apenas as seguintes modalidades:
#Curling
#Patinação no gelo (skating)
#Esqui (skiing)
#Hóquei sobre o gelo (ice hockey)

import requests

url = "https://sites.google.com/site/dr2fundamentospython/arquivos/Winter_Olympics_Medals.csv"


requisicao = requests.get(url, timeout=5)
if requisicao.status_code != 200:
    requisicao.raise_for_status()
else:
    print("Conectado com sucesso!")


csv = requisicao.text


linhas = csv.splitlines()

curling = skating = skiing = Ice = 0

curling_nor = skating_nor =skiing_nor = Ice_nor = 0

curling_DEN = skating_DEN = skiing_DEN = Ice_DEN = 0

for l in range(1, len(linhas)):
  colunas = linhas[l].split(',')
  if colunas[0] >= '2001' and colunas[4] == 'SWE' and colunas[7] == 'Gold' and colunas[2] == "Curling":
     curling += 1
  elif colunas[0] >= '2001' and colunas[4] == 'SWE' and colunas[7] == 'Gold' and colunas[2] == "Skating":
      skating += 1
  elif colunas[0] >= '2001' and colunas[4] == 'SWE' and colunas[7] == 'Gold' and colunas[2] == "Skiing":
      skiing += 1
  elif colunas[0] >= '2001' and colunas[4] == 'SWE' and colunas[7] == 'Gold' and colunas[2] == "Ice Hockey":
      Ice += 1
  elif colunas[0] >= '2001' and colunas[4] == 'NOR' and colunas[7] == 'Gold' and colunas[2] == "Curling":
     curling_nor += 1
  elif colunas[0] >= '2001' and colunas[4] == 'NOR' and colunas[7] == 'Gold' and colunas[2] == "Skating":
      skating_nor += 1
  elif colunas[0] >= '2001' and colunas[4] == 'NOR' and colunas[7] == 'Gold' and colunas[2] == "Skiing":
      skiing_nor += 1
  elif colunas[0] >= '2001' and colunas[4] == 'NOR' and colunas[7] == 'Gold' and colunas[2] == "Ice Hockey":
      Ice_nor += 1
  elif colunas[0] >= '2001' and colunas[4] == 'DEN' and colunas[7] == 'Gold' and colunas[2] == "Curling":
     curling_DEN += 1
  elif colunas[0] >= '2001' and colunas[4] == 'DEN' and colunas[7] == 'Gold' and colunas[2] == "Skating":
      skating_DEN += 1
  elif colunas[0] >= '2001' and colunas[4] == 'DEN' and colunas[7] == 'Gold' and colunas[2] == "Skiing":
      skiing_DEN += 1
  elif colunas[0] >= '2001' and colunas[4] == 'DEN' and colunas[7] == 'Gold' and colunas[2] == "Ice Hockey":
      Ice_DEN += 1

soma_dinamarca = curling_DEN+skiing_DEN+skating_DEN+Ice_DEN
soma_suecia = curling+skiing+skating+Ice
soma_noruega = curling_nor+skiing_nor+skating_nor+Ice_nor
medalhistas = [soma_noruega,soma_suecia,soma_dinamarca]
if soma_suecia>soma_noruega and soma_suecia>soma_dinamarca:
  print(f"Suécia é o maior medalhista possuindo {soma_suecia} medalhas de ouro! ")
elif soma_noruega>soma_suecia and soma_noruega>soma_dinamarca:
  print(f"Noruega é o país medalhista possuindo {soma_noruega} medalhas de ouro!" )
else:
    print(f"Dinamarca é o país medalhista possuindo {soma_dinamarca} medalhas de ouro!")




