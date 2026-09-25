import pandas as pd

df = pd.read_csv("data.csv")

# Remove duplicate rows
df = df.drop_duplicates().reset_index(drop=True)

# Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_", regex=False)

# Standardize text values
for column in df.select_dtypes(include="object"):
	df[column] = df[column].str.strip().str.lower()

print(df)
