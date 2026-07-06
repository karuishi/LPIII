import pandas as pd

data = {
    'Employee_ID': [10, 20, 15, 25, 30],
    'Gender': ['M', 'F', 'F', 'M', 'F'],
    'Remarks': ['Good', 'Nice', 'Good', 'Great', 'Nice']
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

encoded_df = pd.get_dummies(
    df,
    columns=['Gender', 'Remarks'],
    drop_first=True
)

print("\nOne-Hot Encoded Data:")
print(encoded_df)

"""
Pandas provides the get_dummies() function to perform one-hot encoding on categorical columns.
1. Converts categorical values into binary columns
2. Easy and efficient for preprocessing datasets
3. drop_first=True removes one redundant column to avoid multicollinearity
4. Example: Gender with values M and F becomes Gender_M and Gender_F columns
"""
