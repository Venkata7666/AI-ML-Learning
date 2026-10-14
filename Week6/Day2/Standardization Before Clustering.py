import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

X, y = make_blobs(n_samples=300, centers=4, random_state=42)

df = pd.DataFrame(X, columns=['Feature1', 'Feature2'])

X_scaled = StandardScaler().fit_transform(X)

kmeans1 = KMeans(n_clusters=4, random_state=42, n_init=10)
df['Cluster_Before'] = kmeans1.fit_predict(X)

kmeans2 = KMeans(n_clusters=4, random_state=42, n_init=10)
df['Cluster_After'] = kmeans2.fit_predict(X_scaled)

print("Cluster Counts Before Scaling:")
print(df['Cluster_Before'].value_counts().sort_index())

print("\nCluster Counts After Scaling:")
print(df['Cluster_After'].value_counts().sort_index())

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].scatter(df['Feature1'], df['Feature2'], c=df['Cluster_Before'], cmap='viridis')
axes[0].set_title('Before Scaling')
axes[0].set_xlabel('Feature1')
axes[0].set_ylabel('Feature2')

axes[1].scatter(df['Feature1'], df['Feature2'], c=df['Cluster_After'], cmap='viridis')
axes[1].set_title('After Scaling')
axes[1].set_xlabel('Feature1')
axes[1].set_ylabel('Feature2')

plt.tight_layout()
plt.show()