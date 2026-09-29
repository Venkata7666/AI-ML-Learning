import pandas as pd

data = {
    "Hours_Studied": [2, 4, 5, 6, 8, 9, 10],
    "Attendance": [60, 70, 75, 80, 85, 90, 95],
    "Previous_Score": [50, 55, 60, 65, 70, 75, 80],
    "Exam_Score": [55, 60, 65, 70, 78, 85, 90]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

X = df[["Hours_Studied", "Attendance", "Previous_Score"]]
y = df["Exam_Score"]
print("\nIndependent Variables (Features):")
print(X)
print("\nDependent Variable (Target):")
print(y)

print("\nFeature Names:")
print(X.columns.tolist())

print("\nTarget Name:")
print(y.name)