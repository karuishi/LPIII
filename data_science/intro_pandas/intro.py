import requests
import pandas as pd
import matplotlib.pyplot as plt 


target_url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-elo/nbaallelo.csv"
filename = "nba_elo.csv"

response = requests.get(target_url)
response.raise_for_status() # Check that the request was succesful
with open(filename, "wb") as f:
    f.write(response.content)
print(f"Arquivo {filename} está disponível")

df = pd.read_csv(filename) # Leia o arquivo em um dataframe do Pandas

#print(df.head()) # Acessa a primeira linha do dataframe
df.head(5) 
#print(df.tail()) # Acessa a última linha do dataframe

# print(df.shape) # Retorna o número de linhas e colunas do dataframe
# print(df.info) # Retorna um resumo conciso do dataframe
# print(df.describe) # Retorna um resumo descritivo e estátistico de cada coluna do dataframe (count, mean, std, etc)

##################### PLOTTING #####################
df['pts'].plot.hist() # Plota um gráfico de histograma do dataframe
plt.xlabel("Points")
df.plot.scatter(x='year_id', y='seasongame') # Plota um gráfico de dispersão do dataframe
# plt.show()

##################### SUBSETTING #####################
# print(df['year_id']) # Retorna a coluna desejada

df_subset = df[['year_id', 'team_id']] # Pode ser uma ou mais colunas
# print(df_subset)

# Recuperando elementos
# print("LOC") # Recupera linhas (e/ou colunas) em labels específicas
# print(df_subset.loc[3]) 

# print("ILOC")  # Recupera linhas (e/ou colunas) em posições inteiras específicas
# print(df_subset.iloc[8:12])

"""
!!!!!!!!!!! IMPORTANTE !!!!!!!!!!!
O primeiro índice seleciona a linha, o segundo índice seleciona a coluna
"""

##################### SORTING #####################
df_sorted = df_subset.sort_values(by='team_id') # Ordena linhas de uma coluna por valor (menor para maior)
df_sorted[['year_id', 'team_id']]

df_sorted.loc[3]
df_sorted.iloc[3]

##################### VECTORIZATION #####################
"""
!!!!!!!!!!! EVITE !!!!!!!!!!!
for index, row in df.iterrows():
    df.loc[index, 'soma_pts'] = row['pts'] + row['opp_pts']

print(df['soma_pts'])

Ao utilizar o 'for' com o método iterrows(), estamos forçando o Pandas a processar os dados linha a linha.
Isso demanda muito processamento, caso a tabela tenha centenas de milhares de linhas.

O Pandas trabalha com operações vetorizadas. Isto significa que ele é capaz de aplicar uma operação matemática
a blocos inteiros de dados em simultâneo.
"""

df['soma_pts2'] = df['pts'] + df['opp_pts'] # Nestas duas colunas, some linha a linha de uma só vez. Muito mais rápido!!!
# print(df['soma_pts2'])

"""
!!!!!!!!!!! CUIDADO !!!!!!!!!!!
def quadrado(x):
  return x ** 2

df["teste"] = df[['soma_pts']].apply(quadrado, axis=1)
df["teste"] = df['soma_pts'].apply(lambda x: x ** 2)
df["teste"]

Utililzação de for (não vetorizado) ou 'apply' pode deixar o código muito mais lento. Utilize o código vetorizado sempre que possível.
"""

##################### TYPE #####################
x = df.iloc[3]
#print(type(x)) # Retorna o tipo Series, pois a linha no índice 3 é uma Series.
"""
!!!!!!!!!!! CUIDADO !!!!!!!!!!!
print(type(df[('soma_pts', 'team_id')])) 

Ao utilizar parênteses, o Python entende que desejamos criar uma tupla.
Quando passmos uma tupla dentro da seleção de colunas do Pandas, a biblioteca interpreta que estamos procurando por uma coluna com 
índice hierárquico (MultiIndex). Ou seja, o Pandas procurou por uma super-coluna chamada 'soma_pts' que tivesse uma sub-coluna 
chamada 'team_id'.
O correto é passar como uma lista de colunas, utilizando colchetes duplos:
print(type(df[['soma_pts', 'team_id']]))
"""

#print(df['team_id'].unique())
#print(type(df['team_id']))

# Retorna a linha (ou linhas) cujo label do índice seja exatamente 0, trazendo os valores de todas as colunas para essa(s) linha(s).
print(df.loc[0]) 