import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "Hours_Studied": [1, 2, 3, 8, 9, 10, 15, 16, 17],
    "Test_Score": [20, 25, 30, 75, 80, 85, 90, 95, 98]
})

X = data[["Hours_Studied", "Test_Score"]]

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)

data["Cluster"] = kmeans.fit_predict(X)

print("Cluster Assignments:")
print(data)

print("\nCluster Centers:")
print(kmeans.cluster_centers_)

plt.scatter(
    data["Hours_Studied"],
    data["Test_Score"],
    c=data["Cluster"],
    cmap="viridis"
)

plt.scatter(
    kmeans.cluster_centers_[:, 0],
    kmeans.cluster_centers_[:, 1],
    marker="X",
    s=200,
    color="red",
    label="Centroids"
)

plt.xlabel("Hours Studied")
plt.ylabel("Test Score")
plt.title("K-Means Clustering")
plt.legend()
plt.show()