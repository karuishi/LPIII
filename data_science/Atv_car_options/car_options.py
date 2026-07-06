import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

# Car_Options.model_id  ->  Models.model_id  (ID comum nº 1)
# Models.brand_id       ->  Brands.brand_id  (ID comum nº 2)
# Assim juntamos "opções de carro" + "modelo" + "marca" em uma única tabela.
query_join = """
SELECT
    co.option_set_id,
    b.brand_name,
    m.model_name,
    m.model_base_price,
    co.color,
    co.option_set_price,
    (m.model_base_price + co.option_set_price) AS total_price
FROM Car_Options co
INNER JOIN Models m ON co.model_id = m.model_id
INNER JOIN Brands b ON m.brand_id = b.brand_id;
"""

df_sql = pd.read_sql_query(query_join, conn)

csv_path = 'car_options_models.csv'
df_sql.to_csv(csv_path, index=False)
print(f"\nArquivo CSV gerado com sucesso: {csv_path}")
print(f"Total de linhas exportadas: {len(df_sql)}")

conn.close()

df = pd.read_csv(csv_path)

print("\n Primeiras linhas do dataset ")
print(df.head())

print("\n Informações gerais (tipos de dados, valores nulos) ")
print(df.info())

# Verifica valores ausentes
print("\nValores nulos por coluna:")
print(df.isnull().sum())

# Remove linhas duplicadas
df = df.drop_duplicates()

# Garante que colunas numéricas estão no tipo correto
df['model_base_price'] = pd.to_numeric(df['model_base_price'], errors='coerce')
df['option_set_price'] = pd.to_numeric(df['option_set_price'], errors='coerce')
df['total_price'] = pd.to_numeric(df['total_price'], errors='coerce')

# Estatísticas descritivas 
print("\n Estatísticas descritivas do preço total ")
print(df['total_price'].describe())

print("\n Preço médio total por marca ")
# media_por_marca = df.groupby('brand_name')['total_price'].mean().sort_values(ascending=False)
# print(media_por_marca)
media_por_marca = df.groupby('brand_name')['total_price'].agg(
    media='mean', 
    desvio_padrao='std', 
    qtd_carros='count'
    ).sort_values('media', ascending=False)
print(media_por_marca.fillna('-'))

print("\n Preço médio das opções por cor ")
# media_por_cor = df.groupby('color')['option_set_price'].mean().sort_values(ascending=False)
# print(media_por_cor)
media_por_cor = df.groupby('color')['option_set_price'].agg(
    media='mean', 
    desvio_padrao='std', 
    qtd_carros='count'
    ).sort_values('media', ascending=False)
print(media_por_cor.fillna('-'))

print("\n Correlação entre preço base do modelo e preço das opções ")
correlacao = df[['model_base_price', 'option_set_price', 'total_price']].corr()
print(correlacao)

sns.set_style("whitegrid")
# 1) Preço total médio por marca
plt.figure(figsize=(9, 5))
plt.bar(media_por_marca.index,
    media_por_marca['media'],
    yerr=media_por_marca['desvio_padrao'],
    capsize=5,
    color='steelblue',
    )
plt.title('Preço Total Médio por Marca')
plt.ylabel('Preço Total Médio (USD)')
plt.xlabel('Marca')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('grafico_preco_medio_por_marca.png', dpi=150)
plt.close()

# 2) Distribuição do preço das opções
plt.figure(figsize=(8, 5))
sns.histplot(df['option_set_price'], bins=8, kde=True, color='darkorange')
plt.title('Distribuição do Preço das Opções')
plt.xlabel('Preço das Opções (USD)')
plt.ylabel('Frequência')
plt.tight_layout()
plt.savefig('grafico_distribuicao_preco_opcoes.png', dpi=150)
plt.close()

# 3) Preço das opções por cor 
plt.figure(figsize=(9, 5))
sns.boxplot(data=df, x='color', y='option_set_price', hue='color', palette='Set2', legend=False)
plt.title('Preço das Opções por Cor do Carro')
plt.xlabel('Cor')
plt.ylabel('Preço das Opções (USD)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('grafico_preco_por_cor.png', dpi=150)
plt.close()

# 4) Relação entre preço base do modelo e preço das opções
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='model_base_price', y='option_set_price', hue='brand_name', s=100)
plt.title('Preço Base do Modelo x Preço das Opções')
plt.xlabel('Preço Base do Modelo (USD)')
plt.ylabel('Preço das Opções (USD)')
plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', fontsize=8)
plt.tight_layout()
plt.savefig('grafico_dispersao_preco_base_vs_opcoes.png', dpi=150)
plt.close()