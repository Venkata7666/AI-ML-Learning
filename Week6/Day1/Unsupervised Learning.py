import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "Annual_Spending": [20, 25, 30, 80, 85, 90, 150, 160, 170],
    "Purchase_Frequency": [2, 3, 4, 8, 9, 10, 15, 16, 17]
})

scaler = StandardScaler()
X = scaler.fit_transform(data)

model = KMeans(n_clusters=3, random_state=42, n_init=10)
data["Cluster"] = model.fit_predict(X)

print(data)

plt.scatter(
    data["Annual_Spending"],
    data["Purchase_Frequency"],
    c=data["Cluster"]
)
plt.xlabel("Annual Spending")
plt.ylabel("Purchase Frequency")
plt.title("Customer Clustering")
plt.show()