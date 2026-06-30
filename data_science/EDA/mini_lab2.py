import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

FILENAME = 'Salary_Data.csv'

df = pd.read_csv(FILENAME)
df = df.dropna()
df["Education Level"] = df["Education Level"].replace({
    "Bachelor's Degree": "Bachelor's", 
    "phD": "PhD", 
    "Master's Degree": "Master's"
    })

sorted_degrees = ["High School", "Bachelor's", "Master's", "PhD"]
df["Education Level"] = pd.Categorical(
    df["Education Level"], 
    ordered=True, 
    categories=sorted_degrees
    )
# 1. Salary & Years of Experience per degree (scatter plot)
    # Question: Does education ever stop mattering?

plt.figure(figsize=(10, 5))

degrees = df.groupby(by="Education Level")
for group_name, group_df in degrees:
    plt.scatter(
        group_df["Years of Experience"],
        group_df["Salary"],
        label=group_name
    )

plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Salary vs. Years of Experience by Education Level")
plt.legend()
plt.show()
