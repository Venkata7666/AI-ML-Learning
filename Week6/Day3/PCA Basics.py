
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

iris = load_iris()

X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

df = pd.DataFrame(X_pca, columns=["PC1", "PC2"])
df["Species"] = [iris.target_names[i] for i in y]

print("Original dataset shape:", X.shape)
print("Reduced dataset shape:", X_pca.shape)
print("Explained variance ratio:", pca.explained_variance_ratio_)
print("Total variance retained:",
      round(pca.explained_variance_ratio_.sum() * 100, 2), "%")

print(df.head())

for species in iris.target_names:
    subset = df[df["Species"] == species]
    plt.scatter(subset["PC1"], subset["PC2"], label=species)

plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("PCA - Iris Dataset")
plt.legend()
plt.show()
