import random
import pandas as pd

filename = "titanic.csv"

df = pd.read_csv(filename)

column_set = [c for c in df.columns if c not in ['PassengerId']]
print(f"Sua coluna será: {df.columns[random.randint(0, len(df.columns))]}")
"""
-> Survived
R: Em caso de dados faltantes, preencheria como falso (ou 0), pois, dentro do contexto é improvável
que, em caso de não confirmação de sobrevivência ou morte, a pessoa tenha sobrevivido.
"""
