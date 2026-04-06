import pandas as pd

data = {
    "Name": ["A", "B", "C"],
    "Age": [21, 22, 23]
}

df = pd.DataFrame(data)

print(df)
print(df.describe())