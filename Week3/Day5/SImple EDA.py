import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# load data
df = pd.read_csv("sample.csv")

print("First 5 rows")
print(df.head())

print("\nDataset shape")
print(df.shape)

print("\nColumn names")
print(df.columns)

print("\nData types")
print(df.dtypes)

print("\nSummary statistics")
print(df.describe())

# missing values
print("\nMissing values")
print(df.isnull().sum())

# duplicate rows
print("\nDuplicate rows")
print(df.duplicated().sum())

# separate columns
num_cols = df.select_dtypes(include=np.number).columns
cat_cols = df.select_dtypes(include="object").columns

print("\nNumerical columns")
print(list(num_cols))

print("\nCategorical columns")
print(list(cat_cols))


# numerical columns distribution
for col in num_cols:
    plt.figure(figsize=(7, 4))
    plt.hist(df[col].dropna(), bins=20, edgecolor="black")
    plt.title("Distribution of " + col)
    plt.xlabel(col)
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()


# box plots
for col in num_cols:
    plt.figure(figsize=(7, 4))
    sns.boxplot(x=df[col])
    plt.title("Box Plot of " + col)
    plt.xlabel(col)
    plt.tight_layout()
    plt.show()


# categorical columns
for col in cat_cols:

    if df[col].nunique() <= 15:

        plt.figure(figsize=(8, 5))

        df[col].value_counts().plot(
            kind="bar"
        )

        plt.title("Distribution of " + col)
        plt.xlabel(col)
        plt.ylabel("Count")
        plt.xticks(rotation=45)

        plt.tight_layout()
        plt.show()


# correlation
if len(num_cols) > 1:

    plt.figure(figsize=(10, 7))

    sns.heatmap(
        df[num_cols].corr(),
        annot=True,
        cmap="coolwarm",
        fmt=".2f"
    )

    plt.title("Correlation Between Numerical Variables")
    plt.tight_layout()
    plt.show()


# scatter plot
if len(num_cols) >= 2:

    x = num_cols[0]
    y = num_cols[1]

    plt.figure(figsize=(7, 5))

    plt.scatter(
        df[x],
        df[y],
        alpha=0.6
    )

    plt.title(x + " vs " + y)
    plt.xlabel(x)
    plt.ylabel(y)

    plt.tight_layout()
    plt.show()


# outlier check using IQR
print("\nOutlier information")

for col in num_cols:

    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)

    iqr = q3 - q1

    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr

    outliers = df[
        (df[col] < lower) |
        (df[col] > upper)
    ]

    print(
        col,
        "->",
        len(outliers),
        "outliers"
    )


# simple findings
print("\nEDA Findings")
print("-------------------------")

print(
    "The dataset contains",
    df.shape[0],
    "rows and",
    df.shape[1],
    "columns."
)

missing = df.isnull().sum().sum()

if missing == 0:
    print("There are no missing values.")
else:
    print(
        "There are",
        missing,
        "missing values in the dataset."
    )

duplicates = df.duplicated().sum()

if duplicates == 0:
    print("There are no duplicate records.")
else:
    print(
        "There are",
        duplicates,
        "duplicate records."
    )

print(
    "The dataset has",
    len(num_cols),
    "numerical columns and",
    len(cat_cols),
    "categorical columns."
)

print("EDA analysis completed.")