
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "TransactionAmount": [
        45, 50, 48, 52, 47, 55, 49, 51, 46, 53,
        50, 48, 52, 47, 49, 500, 1000
    ]
})

Q1 = df["TransactionAmount"].quantile(0.25)
Q3 = df["TransactionAmount"].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

df["IsOutlier"] = (
    (df["TransactionAmount"] < lower_bound) |
    (df["TransactionAmount"] > upper_bound)
)

df_removed = df.loc[~df["IsOutlier"]].copy()

df_capped = df.copy()
df_capped["TransactionAmount"] = (
    df_capped["TransactionAmount"]
    .clip(lower=lower_bound, upper=upper_bound)
)

print("IQR lower bound:", lower_bound)
print("IQR upper bound:", upper_bound)
print("Original rows:", len(df))
print("Outliers detected:", df["IsOutlier"].sum())
print("Rows after removal:", len(df_removed))

comparison = pd.DataFrame({
    "Method": ["Original", "Outliers Removed", "Outliers Capped"],
    "Count": [
        len(df),
        len(df_removed),
        len(df_capped)
    ],
    "Mean": [
        df["TransactionAmount"].mean(),
        df_removed["TransactionAmount"].mean(),
        df_capped["TransactionAmount"].mean()
    ],
    "Median": [
        df["TransactionAmount"].median(),
        df_removed["TransactionAmount"].median(),
        df_capped["TransactionAmount"].median()
    ],
    "Maximum": [
        df["TransactionAmount"].max(),
        df_removed["TransactionAmount"].max(),
        df_capped["TransactionAmount"].max()
    ]
})

print("\nComparison:")
print(comparison.round(2).to_string(index=False))

plt.figure(figsize=(9, 5))
plt.boxplot(
    [
        df["TransactionAmount"],
        df_removed["TransactionAmount"],
        df_capped["TransactionAmount"]
    ],
    tick_labels=["Original", "Removed", "Capped"]
)
plt.ylabel("Transaction Amount")
plt.title("Outlier Handling Comparison")
plt.grid(axis="y")
plt.show()
