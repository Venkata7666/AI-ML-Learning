# Monday Test: Visualization and EDA
# Inspect data, create charts, and summarize findings.

import pandas as pd
import matplotlib.pyplot as plt

# Create a sample dataset.
df = pd.DataFrame({
	"Product": ["A", "B", "A", "C", "B", "A", "C", "B", "A", "C"],
	"Sales": [120, 90, 150, 80, 110, 130, 95, 105, 160, 100],
	"Rating": [4.2, 3.8, 4.5, 3.5, 4.0, 4.6, 3.9, 4.1, 4.8, 4.0],
})

# Inspect the dataset.
print("First five rows:\n", df.head())
print("\nSummary statistics:\n", df.describe())
print("\nMissing values:\n", df.isnull().sum())

fig, axes = plt.subplots(1, 3, figsize=(13, 4))
df["Sales"].plot(kind="hist", bins=5, ax=axes[0], title="Sales Distribution")
axes[0].set_xlabel("Sales")

df.groupby("Product")["Sales"].mean().plot(
	kind="bar", ax=axes[1], title="Average Sales by Product", color="skyblue"
)
axes[1].set_ylabel("Average sales")
axes[1].tick_params(axis="x", rotation=0)

axes[2].scatter(df["Sales"], df["Rating"])
axes[2].set(title="Sales vs. Rating", xlabel="Sales", ylabel="Rating")
plt.tight_layout()
plt.show()

average_sales = df.groupby("Product")["Sales"].mean()
best_product = average_sales.idxmax()
print(f"\nFindings: Product {best_product} has the highest average sales ({average_sales.max():.1f}).")
print(f"Overall average sales: {df['Sales'].mean():.1f}")
print(f"Overall average rating: {df['Rating'].mean():.2f}")
