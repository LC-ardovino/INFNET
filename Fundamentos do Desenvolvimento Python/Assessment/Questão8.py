#Boa tarde professor, fiquei sabendo hoje atravéz de um amigo que o senhor pediu para não fazer com o pandas, acabou que
#não consegui resolver essa questão com o que foi aprendido em sala, mas mesmo assim preferi não deixá-la em branco.Acabei
# pesquisando por conta própria sobre a biblioteca pandas e consegui resolver, irei entender se o senhor não aceitar a questão.

import pandas #Importa a biblioteca pandas para resolver a questão

url = 'https://sites.google.com/site/dr2fundamentospython/arquivos/Video_Games_Sales_as_at_22_Dec_2016.csv'
dataframe = pandas.read_csv(url,sep=',')#Um DataFrame é simplesmente um conjunto de Series. Trata-se de uma estrutura de dados de 2 dimensões — colunas e linhas — que transforma os dados em uma bela tabela.

jogo_genero = dataframe[(dataframe['Genre'] == 'Action') | (dataframe['Genre'] == 'Shooter') | (dataframe['Genre'] == 'Platform')]#Crio uma tabela de 2 dimensões com os tipos de jogos. (A)
venda_Global = dataframe.groupby(['Publisher'])['Global_Sales'].sum().sort_values(ascending=False)#Crio uma tabela de 2 dimensões onde agrupo em ordem descendente o número de vendas globais e a publisher. (B)
ação = dataframe[(dataframe['Year_of_Release']>=2011) & (dataframe['Genre'] == 'Action')]#Crio uma tabela de 2 dimensões onde agrupo os jogos de ação que vieram depois de 2010
Tiro = dataframe[(dataframe['Year_of_Release']>=2011) & (dataframe['Genre'] == 'Shooter')]#Crio uma tabela de 2 dimensões onde agrupo os jogos de tiro que vieram depois de 2010
Plataforma = dataframe[(dataframe['Year_of_Release'] >= 2010) & (dataframe['Genre'] == 'Platform')]#Crio uma tabela de 2 dimensões onde agrupo os jogos de  que vieram depois de 2010
japa_ação = dataframe[(dataframe['Year_of_Release']>=2011) & (dataframe['Genre'] == 'Action')]#Crio uma tabela de 2 dimensões onde agrupo os jogos de ação que vieram depois de 2010, mas para o japão
japa_Tiro = dataframe[(dataframe['Year_of_Release']>=2011) & (dataframe['Genre'] == 'Shooter')]#Crio uma tabela de 2 dimensões onde agrupo os jogos de tiro que vieram depois de 2010,mas para o japão
japa_Plataforma = dataframe[(dataframe['Year_of_Release'] >= 2010) & (dataframe['Genre'] == 'Platform')]#Crio uma tabela de 2 dimensões onde agrupo os jogos de  que vieram depois de 2010, mas para o japão



os_3_mais_publicados = jogo_genero.groupby(['Publisher'])['Publisher'].count().sort_values(ascending=False).head(3)#Ordena em ordem descendente as 3 publishers com mais jogos publicados, com os 3 gêneros publicados.(A)
as_3_publishers = venda_Global.head(3)# ordena as 3 publishers com maior lucro global
maior_ação = ação.groupby(['Publisher'])['Publisher'].count().sort_values(ascending=False).head(1)#Ordena em uma tabela a maior marca e a quantidade de jogos de ação lançados
maior_Tiro = Tiro.groupby(['Publisher'])['Publisher'].count().sort_values(ascending=False).head(1)#Ordena em uma tabela a maior marca e a quantidade de jogos de tiro lançados
maior_Plataforma = Plataforma.groupby(['Publisher'])['Publisher'].count().sort_values(ascending=False).head(1)#Ordena em uma tabela a maior marca e a quantidade de jogos de plataforma lançados
japa_maior_ação = ação.groupby(['Publisher'])['JP_Sales'].count().sort_values(ascending=False).head(1)#Ordena em uma tabela a maior marca e a quantidade de jogos de ação lançados no Japão
japa_maior_Tiro = Tiro.groupby(['Publisher'])['JP_Sales'].count().sort_values(ascending=False).head(1)#Ordena em uma tabela a maior marca e a quantidade de jogos de tiro lançados no Japão
japa_maior_Plataforma = Plataforma.groupby(['Publisher'])['JP_Sales'].count().sort_values(ascending=False).head(1)#Ordena em uma tabela a maior marca e a quantidade de jogos de plataforma lançados no Japão

#Agora irei printar as informações pedidas.

print("As 3 marcas que mais publicaram jogos:")
print(os_3_mais_publicados)
print("-"*30)
print("Os 3 maiores vendedores de jogos:")
print(as_3_publishers)
print('-'*30)
print('Marca com mais publicações no gênero action:')
print(maior_ação)
print('-'*30)
print('Marca com mais publicações no gênero Shooter:')
print(maior_Tiro)
print('-'*30)
print('Marca com mais publicações no gênero Plataforma:')
print(maior_Plataforma)
print('-'*30)
print('Marca com mais publicações no gênero action no Japão:')
print(japa_maior_ação)
print('-'*30)
print('Marca com mais publicações no gênero Shooter no Japão:')
print(japa_maior_Tiro)
print('-'*30)
print('Marca com mais publicações no gênero Plataforma no Japão:')
print(japa_maior_Plataforma)