# Regressão Linear em Machine Learning
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

filename = "Salary_Data.csv"
df = pd.read_csv(filename)
# print(df.head())
# df.info()
# df.describe()

X = df[["Years of Experience"]] # Matriz de recursos 
y = df["Salary"] # Vetor alvo

# Dividindo em treino e teste (?)
years_range = pd.DataFrame({'Years of Experience': list(range(1, 13))})
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit Linear
lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)
y_pred = lin_reg.predict(X_test)

plt.scatter(df[["Years of Experience"]], df["Salary"])
plt.plot(years_range, lin_reg.predict(years_range), color='red')
plt.xlabel("Anos de Experiência")
plt.ylabel("Salário")
plt.show()