import numpy as np
import pandas as pd
values = np.array([1, 2, 3, 4, 5])
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("shape:", matrix.shape, "dimensions:", matrix.ndim, "dtype:", matrix.dtype)

# Common constructors and sequences
zeros = np.zeros((2, 3))
ones = np.ones(4)
identity = np.eye(3)
sequence = np.arange(0, 10, 2)
evenly_spaced = np.linspace(0, 1, 5)

# %% Indexing, slicing, reshaping, and combining
print(values[0], values[-1], values[1:4])
print(matrix[0, 1], matrix[:, 1], matrix[1, :])
reshaped = np.arange(12).reshape(3, 4)
flattened = reshaped.ravel()
print("reshaped:\n", reshaped, "\nflattened:", flattened)
print("vertical:\n", np.vstack([values, values + 10]))
print("horizontal:", np.hstack([values, values + 10]))

# A view can share memory; copy creates independent data.
view = reshaped[:, :2]
independent_copy = reshaped[:, :2].copy()

# %% Vectorized operations, broadcasting, filtering, and aggregation
print("arithmetic:", values * 2 + 1)
print("broadcasted:\n", matrix + np.array([10, 20, 30]))
print("boolean filter:", values[values > 2])
print("sum/mean/min/max:", values.sum(), values.mean(), values.min(), values.max())
print("column means:", matrix.mean(axis=0))
print("row sums:", matrix.sum(axis=1))
print("unique values:", np.unique(np.array([1, 2, 2, 3])))
print("where:", np.where(values % 2 == 0, "even", "odd"))
print("matrix multiplication:\n", matrix @ matrix.T)
print("random sample:\n", np.random.default_rng(42).normal(size=(2, 2)))


sales = pd.DataFrame(
	{
		"name": ["Ana", "Ben", "Cara", "Dan"],
		"department": ["A", "B", "A", "B"],
		"sales": [120, 95, 150, np.nan],
		"units": [10, 8, 12, 7],
	},
	index=[101, 102, 103, 104],
)
department = sales["department"]
print(sales.head(), "\n", sales.shape, sales.dtypes)
print(sales.info())

# Selection: [] selects columns, loc uses labels, iloc uses positions.
print(sales["sales"])
print(sales[["name", "sales"]])
print(sales.loc[101:103, ["name", "sales"]])
print(sales.iloc[:2, :2])
print(sales[sales["sales"].fillna(0) > 100])

# %% Cleaning and transforming data
print("missing values:\n", sales.isna().sum())
sales["sales"] = sales["sales"].fillna(sales["sales"].median())
sales["sales_per_unit"] = sales["sales"] / sales["units"]
sales["performance"] = np.where(sales["sales"] >= 120, "high", "standard")
sales = sales.rename(columns={"name": "employee"})
sales = sales.drop_duplicates()
print(sales.sort_values("sales", ascending=False))

# %% Descriptive statistics, grouping, and reshaping
print(sales.describe())
print(sales.groupby("department")["sales"].agg(["count", "sum", "mean"]))
summary = sales.groupby("department", as_index=False).agg(
	total_sales=("sales", "sum"), average_units=("units", "mean")
)
print(summary)
print(pd.crosstab(sales["department"], sales["performance"]))
pivot = sales.pivot_table(index="department", values="sales", aggfunc="mean")
print(pivot)

# %% Combining tables and working with dates
targets = pd.DataFrame({"department": ["A", "B"], "target": [250, 200]})
combined = sales.merge(targets, on="department", how="left")
print(combined)
combined = pd.concat([combined, combined.iloc[[0]]], ignore_index=True)
combined = combined.drop_duplicates()

dates = pd.to_datetime(["2025-01-01", "2025-01-15", "2025-02-01"])
date_frame = pd.DataFrame({"date": dates, "value": [10, 20, 15]}).set_index("date")
date_frame["month"] = date_frame.index.month
print(date_frame.resample("ME")["value"].sum())

 
print("\nSummary complete.")
