
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, adjusted_rand_score

iris = load_iris()
X = iris.data
y = iris.target

X_scaled = StandardScaler().fit_transform(X)

kmeans_original = KMeans(n_clusters=3, random_state=42, n_init=10)
clusters_original = kmeans_original.fit_predict(X_scaled)

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

kmeans_pca = KMeans(n_clusters=3, random_state=42, n_init=10)
clusters_pca = kmeans_pca.fit_predict(X_pca)

print("Original data silhouette score:",
      round(silhouette_score(X_scaled, clusters_original), 3))

print("PCA data silhouette score:",
      round(silhouette_score(X_pca, clusters_pca), 3))

print("Original data adjusted Rand index:",
      round(adjusted_rand_score(y, clusters_original), 3))

print("PCA data adjusted Rand index:",
      round(adjusted_rand_score(y, clusters_pca), 3))

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].scatter(
    X_pca[:, 0], X_pca[:, 1],
    c=clusters_original, cmap="viridis"
)
axes[0].set_title("KMeans on Original Features")
axes[0].set_xlabel("PC1")
axes[0].set_ylabel("PC2")

axes[1].scatter(
    X_pca[:, 0], X_pca[:, 1],
    c=clusters_pca, cmap="viridis"
)
axes[1].set_title("KMeans on PCA Features")
axes[1].set_xlabel("PC1")
axes[1].set_ylabel("PC2")

plt.tight_layout()
plt.show()
