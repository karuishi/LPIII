import pandas as pd

filename = "titanic.csv"

df = pd.read_csv(filename)

df.head()
df.info()
df.isnull().sum()

df_clean = df.dropna(axis='index')
df_clean.info()

df_clean = df.dropna(axis='columns')
df_clean.info()

novel_df = df;
novel_df['Age']=novel_df['Age'].fillna(novel_df['Age'].mean())
novel_df.info()
df.isnull().sum()

novel_df = df;
novel_df['Cabin'] = novel_df['Cabin'].fillna('NOCABIN')