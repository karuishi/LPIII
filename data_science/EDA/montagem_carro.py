import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)

# Vamos simular utilizando uma distribuição normal para a qualidade da produção robotizada
x = np.linspace(0, 1, 30)
robotic_quality = np.clip(np.random.normal(loc=0.89, scale=0.03, size=30), 0, 1)

# Vamos simular utilizando uma variação ao longo do dia (30 carros) para demonstrar produção híbrida
trend = np.piecewise(x,
                     [x < 0.4, (x >= 0.4) & (x < 0.8), x >= 0.8],
                     [lambda x: 0.80 + 0.25*x/0.4,
                      lambda x: 0.85 + 0.05*(x-0.4)/0.4,
                      lambda x: 0.90 - 0.20*(x-0.8)/0.2])

hybrid_quality_trended = np.clip(trend + np.random.normal(0, 0.02, size=30), 0, 1)

df_quality = pd.DataFrame({
    "Robotic": robotic_quality,
    "Hybrid": hybrid_quality_trended
})

print(df_quality.head())

# Gráfico de dispersão (Scatter Plot)
plt.figure(figsize=(10, 5))

plt.scatter(df_quality.index, df_quality["Robotic"], label="Robotic")
plt.scatter(df_quality.index, df_quality["Hybrid"], label="Hybrid")

plt.title("Qualidade por método de produção")
plt.xlabel("Número de carros produzidos no dia")
plt.ylabel("Score de qualidade")
plt.ylim(.5, 1)
plt.legend()
plt.grid(True)
plt.show()

# Gráfico de Linha
df_quality.plot(figsize=(10, 5), marker="o")
plt.title("Qualidade por método de produção")
plt.xlabel("Número de carros produzidos no dia")
plt.ylabel("Score de qualidade")
plt.ylim(.5, 1)
plt.grid(True)
plt.show()

# Histograma
bins = np.linspace(.5, 1, 11)  # 10 equal-width bins from 0 to 1

plt.figure(figsize=(10, 5))

plt.hist(
    df_quality["Robotic"],
    bins=bins,
    alpha=0.6,
    label="Robotic",
    edgecolor="black"
)

plt.hist(
    df_quality["Hybrid"],
    bins=bins,
    alpha=0.6,
    label="Hybrid",
    edgecolor="black"
)

plt.title("Histogram Comparison of Quality Scores")
plt.xlabel("Quality Score")
plt.ylabel("Frequency")
plt.xlim(.5, 1)
plt.legend()
plt.grid(True)

plt.show()

# Boxplot
morning_robotic = df_quality["Robotic"].iloc[:15]
afternoon_robotic = df_quality["Robotic"].iloc[15:]

morning_hybrid = df_quality["Hybrid"].iloc[:15]
afternoon_hybrid = df_quality["Hybrid"].iloc[15:]

plt.figure(figsize=(10, 5))

plt.boxplot(
    [
        morning_robotic,
        morning_hybrid,
        afternoon_robotic,
        afternoon_hybrid
    ],
    tick_labels=[
        "Robotic\nMorning",
        "Hybrid\nMorning",
        "Robotic\nAfternoon",
        "Hybrid\nAfternoon"
    ],
    showmeans=True,
    meanline=True,
    meanprops={
        "linestyle": "--",
        "linewidth": 2,
        "color": "red"
    },
    medianprops={
        "linewidth": 2,
        "color": "black"
    }
)

plt.title("Quality Score Comparison by Method and Time of Day")
plt.ylabel("Quality Score")
plt.ylim(.7, 1.01)
plt.grid(True, axis="y")

plt.show()

# Barplot
grouped_quality = pd.DataFrame({
    "Robotic": [
        df_quality["Robotic"].iloc[:15].mean(),
        df_quality["Robotic"].iloc[15:].mean()
    ],
    "Hybrid": [
        df_quality["Hybrid"].iloc[:15].mean(),
        df_quality["Hybrid"].iloc[15:].mean()
    ]
}, index=["Manhã", "Tarde"])

ax = grouped_quality.plot(
    kind="bar",
    ylabel="Qualidade Média",
    xlabel="Turno",
    ylim=(0.7, 1),
    rot=0,
    figsize=(8, 5)
)

plt.title("Comparativo de Qualidade Média por Turno e Método")
plt.grid(axis="y")

plt.tight_layout()
plt.show()