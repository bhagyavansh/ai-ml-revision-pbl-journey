import pandas as pd

data = {
    "Name":["A","B","C","D"],
    "Age":[21, None, 23,None],
    "Salary":[50000, 60000, None, 55000]
}

df = pd.DataFrame(data)
print("Before Cleaning:\n", df)
df["Age"].fillna(df["Age"].mean(), inplace = True)
df["Salary"].fillna(df["Salary"].mean(), inplace = True)
print("\nAfter Cleaning:\n", df)
