import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.DataFrame({
    "Color": ["Red", "Blue", "Green", "Red"],
    "Size": ["Small", "Medium", "Large", "Small"]
})

le = LabelEncoder()
df["Color_Label"] = le.fit_transform(df["Color"])

df_onehot = pd.get_dummies(df, columns=["Size"], dtype=int)

print("Label Encoding:")
print(df[["Color", "Color_Label"]])

print("\nOne-Hot Encoding:")
print(df_onehot)