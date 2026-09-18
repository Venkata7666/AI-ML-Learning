import pandas as pd
data = pd.DataFrame(
    {
        "name": ["Ava", "Ben", "Chloe", "Diego", "Emma"],
        "age": [22, None, 31, 28, None],
        "score": [88.5, 92.0, None, 76.5, 85.0],
        "city": ["London", "Paris", None, "Berlin", "Paris"],
    }
)

print("Original dataset:\n", data)

print("\nMissing-value mask:\n", data.isna())
print("\nMissing values per column:\n", data.isna().sum())
print("\nRows containing missing values:\n", data[data.isna().any(axis=1)])

filled = data.copy()
filled["age"] = filled["age"].fillna(filled["age"].median())
filled["score"] = filled["score"].fillna(filled["score"].median())
filled["city"] = filled["city"].fillna(filled["city"].mode()[0])
print("\nAfter filling missing values:\n", filled)

print("\nAfter dropping incomplete rows:\n", data.dropna())

print("\nColumns without missing values:\n", data.dropna(axis="columns"))