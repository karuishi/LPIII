import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

try:
    conn = sqlite3.connect('Car_Database.db')
    print("Conexão com o banco de dados estabelecida com sucesso.")
except sqlite3.Error as e:
    print(f"Erro ao conectar ao banco de dados: {e}")
    conn = None

cursor = conn.cursor()

query_tables = "SELECT name FROM sqlite_master WHERE type='table';"
cursor.execute(query_tables)
tables = cursor.fetchall()
print("\nTabelas na base de dados:")
for table in tables:
    print(f"- {table[0]}")

# Customers.customer_id        -> Customer_Ownership.customer_id  (ID comum nº 1)
# Customer_Ownership.dealer_id -> Dealers.dealer_id               (ID comum nº 2)
# Assim juntamos "cliente" + "compra" + "concessionária" em uma única tabela.
query_join = """
SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    c.gender,
    c.household_income,
    c.birthdate,
    co.purchase_date,
    co.purchase_price,
    d.dealer_name
FROM Customers c
INNER JOIN Customer_Ownership co ON c.customer_id = co.customer_id
INNER JOIN Dealers d ON co.dealer_id = d.dealer_id;
"""

df_sql = pd.read_sql_query(query_join, conn)

csv_path = 'customers_purchases.csv'
df_sql.to_csv(csv_path, index=False)
print(f"\nArquivo CSV gerado com sucesso: {csv_path}")
print(f"Total de linhas exportadas: {len(df_sql)}")

conn.close()

df = pd.read_csv(csv_path)

print("\n Primeiras linhas do dataset ")
print(df.head())

print("\n Informações gerais (tipos de dados, valores nulos) ")
print(df.info())

print("\nValores nulos por coluna:")
print(df.isnull().sum())

df = df.drop_duplicates()

# Converte datas de texto para datetime
df['birthdate'] = pd.to_datetime(df['birthdate'])
df['purchase_date'] = pd.to_datetime(df['purchase_date'])

# Cria uma coluna nova: idade do cliente NO MOMENTO da compra
df['idade_na_compra'] = (
    (df['purchase_date'] - df['birthdate']).dt.days // 365
)

# Cria uma coluna com o nome completo
df['nome_completo'] = df['first_name'] + ' ' + df['last_name']

# Estatísticas descritivas 
print("\n Estatísticas descritivas do preço pago ")
print(df['purchase_price'].describe())

print("\n Renda média e preço médio pago, por gênero ")
# por_genero = df.groupby('gender')[['household_income', 'purchase_price']].mean()
# print(por_genero)
por_genero = df.groupby('gender').agg(
    renda_media=('household_income', 'mean'),
    renda_desvio_padrao=('household_income', 'std'),
    preco_medio=('purchase_price', 'mean'),
    preco_desvio_padrao=('purchase_price', 'std'),
    qtd_clientes=('purchase_price', 'count'),
)
print(por_genero)

print("\n Idade média dos clientes no momento da compra ")
print(f"Média: {df['idade_na_compra'].mean():.1f} anos")
print(f"Desvio padrão: {df['idade_na_compra'].std():.1f} anos")

print("\n Preço médio pago por concessionária ")
stats_dealer = df.groupby('dealer_name')['purchase_price'].agg(
    media='mean', desvio_padrao='std', qtd_compras='count'
).sort_values('media', ascending=False)
print(stats_dealer.fillna('-'))
por_dealer = stats_dealer['media']

print("\n Correlação entre renda familiar e preço pago pelo carro ")
correlacao = df[['household_income', 'purchase_price', 'idade_na_compra']].corr()
print(correlacao)

# Proporção do preço do carro em relação à renda anual 
df['percentual_da_renda'] = (df['purchase_price'] / df['household_income']) * 100
print("\n Percentual da renda anual gasto no carro, por cliente ")
print(df[['nome_completo', 'household_income', 'purchase_price', 'percentual_da_renda']])

sns.set_style("whitegrid")
# 1) Renda familiar x Preço pago
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='household_income', y='purchase_price', hue='gender', s=150)
plt.title('Renda Familiar x Preço Pago pelo Carro')
plt.xlabel('Renda Familiar Anual (USD)')
plt.ylabel('Preço Pago pelo Carro (USD)')
plt.tight_layout()
plt.savefig('grafico_renda_vs_preco.png', dpi=150)
plt.close()

# 2) Preço médio pago por concessionária
plt.figure(figsize=(8, 5))
plt.bar(
    stats_dealer.index,
    stats_dealer['media'],
    yerr=stats_dealer['desvio_padrao'],
    capsize=5,
    color='mediumseagreen',
)
plt.title('Preço Médio Pago por Concessionária')
plt.xlabel('Concessionária')
plt.ylabel('Preço Médio (USD)')
plt.xticks(rotation=30, ha='right')
plt.tight_layout()
plt.savefig('grafico_preco_por_concessionaria.png', dpi=150)
plt.close()

# 3) Percentual da renda gasto no carro, por cliente
plt.figure(figsize=(8, 5))
df_sorted = df.sort_values('percentual_da_renda', ascending=True)
plt.barh(df_sorted['nome_completo'], df_sorted['percentual_da_renda'], color='coral')
plt.title('Percentual da Renda Anual Gasto no Carro')
plt.xlabel('% da Renda Anual')
plt.ylabel('Cliente')
plt.tight_layout()
plt.savefig('grafico_percentual_renda.png', dpi=150)
plt.close()

# 4) Preço pago x Idade na compra
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='idade_na_compra', y='purchase_price', hue='gender', s=150)
plt.title('Idade do Cliente na Compra x Preço Pago')
plt.xlabel('Idade na Compra (anos)')
plt.ylabel('Preço Pago (USD)')
plt.tight_layout()
plt.savefig('grafico_idade_vs_preco.png', dpi=150)
plt.close()
