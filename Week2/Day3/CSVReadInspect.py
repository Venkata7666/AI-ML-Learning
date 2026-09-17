
from pathlib import Path

import pandas as pd

CSV_FILE = Path(__file__).with_name("sample_data.csv")


def create_sample_csv() -> None:
	data = pd.DataFrame(
		{
			"name": ["Alice", "Bob", "Charlie", "Diana", "Evan"],
			"age": [25, 31, 29, 35, 27],
			"department": ["Sales", "IT", "Sales", "HR", "IT"],
			"salary": [52000, 68000, 58000, 61000, 72000],
		}
	)
	data.to_csv(CSV_FILE, index=False)


if not CSV_FILE.exists():
	create_sample_csv()

df = pd.read_csv(CSV_FILE)

print("First five rows:")
print(df.head())

print("\nLast five rows:")
print(df.tail())

print("\nDataFrame information:")
df.info()

print("\nDescriptive statistics:")
print(df.describe(include="all"))
