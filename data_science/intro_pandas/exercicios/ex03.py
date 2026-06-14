import requests
import pandas as pd

target_url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-elo/nbaallelo.csv"
filename = "nba_elo.csv"

response = requests.get(target_url)
response.raise_for_status() # Check that the request was succesful
with open(filename, "wb") as f:
    f.write(response.content)
print(f"Arquivo {filename} está disponível")

df = pd.read_csv(filename)

df2 = df.where(df['game_id'] == '194611010TRH')
# Exercício 4
df3 = df.drop(columns=["notes"]).dropna(axis=1) # axis = {0 for index, 1 for column}
print(df2)
print(df3)

"""
1. Mantém o formato original: Ele não reduz o tamanho da tabela. O df3 continuará tendo exatamente 
o mesmo número de linhas e colunas do df original.

2. Preserva onde é Verdadeiro: Nas linhas onde o game_id for igual a '194611010TRH', ele mantém os valores originais intactos.

3. Substitui por NaN onde é Falso: Em todas as outras centenas de milhares de linhas onde o game_id for diferente, ele não apaga as linhas,
mas sim substitui todos os dados delas por NaN (valores nulos).
"""
