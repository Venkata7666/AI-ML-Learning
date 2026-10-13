import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = pd.DataFrame({
    "Hours_Studied": [1, 2, 3, 8, 9, 10, 15, 16, 17],
    "Test_Score": [20, 25, 30, 75, 80, 85, 90, 95, 98]
})

X = data[["Hours_Studied", "Test_Score"]]

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
data["Cluster"] = kmeans.fit_predict(X)

plt.figure(figsize=(8, 5))

plt.scatter(
    data["Hours_Studied"],
    data["Test_Score"],
    c=data["Cluster"],
    cmap="viridis",
    s=100
)

centers = kmeans.cluster_centers_

plt.scatter(
    centers[:, 0],
    centers[:, 1],
    marker="X",
    s=250,
    color="red",
    label="Centroids"
)

plt.xlabel("Hours Studied")
plt.ylabel("Test Score")
plt.title("K-Means Cluster Visualization")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()