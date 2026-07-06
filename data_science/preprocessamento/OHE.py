import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Criando um DataFrame fictício
dados = {'Cor': ['Vermelho', 'Azul', 'Verde', 'Azul', 'Vermelho']}
df = pd.DataFrame(dados)

print("--- Dados Originais ---")
print(df)
print("\n")

encoder = OneHotEncoder(sparse_output=False)

# 1. Ajustando (fit) e transformando (transform) os dados
# O scikit-learn espera um array 2D, por isso passamos df[['Cor']] em vez de df['Cor']
dados_codificados = encoder.fit_transform(df[['Cor']])

# 2. Transformando o resultado de volta em um DataFrame para facilitar a leitura
# get_feature_names_out() gera os nomes das novas colunas automaticamente
nomes_das_colunas = encoder.get_feature_names_out(['Cor'])
df_codificado = pd.DataFrame(dados_codificados, columns=nomes_das_colunas)

print("--- Dados após One-Hot Encoding ---")
print(df_codificado)

# Criando um DataFrame fictício
data = {
    'Color': ['Red', 'Blue', 'Green', 'Blue', 'Green', 'Red'],
    'Size': ['Small', 'Medium', 'Large', 'Large', 'Medium', 'Small'],
    'Condition': ['New', 'Used', 'New', 'Used', 'New', 'New']
}

df = pd.DataFrame(data)
dummies_df = pd.get_dummies(df) # Aplicando get_dummies, função familiar ao OH encoding
print(dummies_df) # Exibindo o DataFrame com variáveis dummy