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

df['soma_pts'] = df['pts'] + df['opp_pts']
predicado = (df['soma_pts'] >= 100) & (df['soma_pts'] < 300)

df2 = df[predicado]
print(df2)