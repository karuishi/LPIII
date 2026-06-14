import requests
import pandas as pd

# Crie um dataframe apenas com as linhas onde soma_pts é maior que um certo valor

target_url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-elo/nbaallelo.csv"
filename = "nba_elo.csv"

response = requests.get(target_url)
response.raise_for_status() # Check that the request was succesful
with open(filename, "wb") as f:
    f.write(response.content)
print(f"Arquivo {filename} está disponível")

df = pd.read_csv(filename)

df['soma_pts'] = df['pts'] + df['opp_pts']

df2 = df[df['soma_pts'] > 200]
print(df2.head(5))