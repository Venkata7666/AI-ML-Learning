
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

iris = load_iris()

X = iris.data
y = iris.target

X_scaled = StandardScaler().fit_transform(X)

pca = PCA(n_components=2)
X_2d = pca.fit_transform(X_scaled)

plt.figure(figsize=(8, 6))

for i, species in enumerate(iris.target_names):
    plt.scatter(
        X_2d[y == i, 0],
        X_2d[y == i, 1],
        label=species
    )

plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("2D Projection Using PCA")
plt.legend()
plt.grid(True)
plt.show()

print("Original shape:", X.shape)
print("Projected shape:", X_2d.shape)
print("Variance retained:",
      round(pca.explained_variance_ratio_.sum() * 100, 2), "%")
