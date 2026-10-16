
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

iris = load_iris()
X = iris.data

X_scaled = StandardScaler().fit_transform(X)

pca = PCA()
X_pca = pca.fit_transform(X_scaled)

variance_ratio = pca.explained_variance_ratio_
cumulative_variance = np.cumsum(variance_ratio)

print("Explained variance ratio:")
for i, ratio in enumerate(variance_ratio):
    print(f"PC{i + 1}: {ratio:.4f} ({ratio * 100:.2f}%)")

print("\nCumulative explained variance:")
for i, value in enumerate(cumulative_variance):
    print(f"First {i + 1} components: {value * 100:.2f}%")

plt.figure(figsize=(8, 5))
plt.bar(
    range(1, len(variance_ratio) + 1),
    variance_ratio * 100,
    label="Individual variance"
)
plt.plot(
    range(1, len(cumulative_variance) + 1),
    cumulative_variance * 100,
    marker="o",
    label="Cumulative variance"
)

plt.xlabel("Principal Components")
plt.ylabel("Explained Variance (%)")
plt.title("PCA Explained Variance")
plt.xticks(range(1, len(variance_ratio) + 1))
plt.legend()
plt.grid(axis="y")
plt.show()
