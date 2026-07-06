import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

target = "https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data"
filename = "auto-mpg.data"

response = requests.get(target)
response.raise_for_status() 
with open(filename, "wb") as f:
    f.write(response.content)
print(f"Arquivo {filename} está disponível")

column_names = [
    "mpg", "cylinders", "displacement", "horsepower", "weight",
    "acceleration", "model_year", "origin", "car_name"
]

df_auto = pd.read_csv(
    filename,
    names=column_names,
    na_values="?",
    sep=r'\s+'
)

print(df_auto.head())

# Remove o target e o nome do carro
non_target_numeric = df_auto.drop(columns=['mpg', 'car_name'])
correlation_matrix = non_target_numeric.corr()

plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlação entre variáveis Não-Alvo")
plt.tight_layout()
plt.show()

# Correlação com Spearman
correlation_matrix = non_target_numeric.corr(method="spearman")
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlação (Spearman) entre variáveis Não-Alvo")
plt.tight_layout()
plt.show()

# Correlação do target 'mpg'
correlation_with_target = df_auto.corr(numeric_only=True)['mpg'].drop('mpg').sort_values(ascending=False)

# Convert to DataFrame for display
correlation_table = correlation_with_target.reset_index()
correlation_table.columns = ['Variável', 'Correlação com mpg']
