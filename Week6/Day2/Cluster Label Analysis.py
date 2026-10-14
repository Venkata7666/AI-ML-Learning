import pandas as pd
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

X, y = make_blobs(n_samples=300, centers=4, random_state=42)

df = pd.DataFrame(X, columns=['Feature1', 'Feature2'])

kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)

df['Cluster'] = kmeans.fit_predict(X)

print("Dataset with Cluster Labels:")
print(df.head())

print("\nNumber of Data Points in Each Cluster:")
print(df['Cluster'].value_counts().sort_index())

print("\nCluster Analysis:")
print(df.groupby('Cluster')[['Feature1', 'Feature2']].mean())

plt.scatter(df['Feature1'], df['Feature2'], c=df['Cluster'], cmap='viridis')

plt.xlabel('Feature1')
plt.ylabel('Feature2')
plt.title('Cluster Label Analysis')
plt.show()