#Conduct a coding test on arrays, DataFrames, filtering, and basic statistics.
import numpy as np
import pandas as pd

arr = np.array([10, 20, 30, 40, 50])

print("Array:",arr)
print("Sum:", arr.sum())
print("Mean:", arr.mean())
print("Maximum:", arr.max())
print("Minimum:", arr.min())

data = {
    "Name": ["RAJ", "Ram", "kiran", "harsha", "buddy"],
    "Age": [25, 30, 22, 35, 28],
    "Salary": [50000, 70000, 45000, 80000, 65000]
}

df=pd.DataFrame(data)
print("\nDataFrame:")
print(df)
print("\nSalaryis greater than 60000:")
print(df[df["Salary"] > 60000])

print("\nAverage Salary:", df["Salary"].mean())
print("Highest Salary:", df["Salary"].max())
print("Lowest Salary:", df["Salary"].min())

print("\nSorted by Salary:")
print(df.sort_values("Salary", ascending=False))
print("\nSorted by Age:")
print(df.sort_values("Age", ascending=False))
