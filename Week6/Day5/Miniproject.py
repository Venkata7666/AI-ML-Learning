
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Load dataset
df = pd.read_csv("Mall_Customers.csv")

# Inspect data
print(df.head())
print(df.info())
print(df.isnull().sum())

# Clean data
df = df.drop_duplicates()
df = df.dropna(subset=[
    "Annual Income (k$)",
    "Spending Score (1-100)"
])

# Select features
X = df[[
    "Annual Income (k$)",
    "Spending Score (1-100)"
]]

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Elbow analysis
inertia = []

for k in range(1, 11):
    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )
    model.fit(X_scaled)
    inertia.append(model.inertia_)

plt.plot(range(1, 11), inertia, marker="o")
plt.xlabel("Number of Clusters")
plt.ylabel("Inertia")
plt.title("Elbow Method")
plt.show()

# Train final model
kmeans = KMeans(
    n_clusters=5,
    random_state=42,
    n_init=10
)

df["Cluster"] = kmeans.fit_predict(X_scaled)

# Visualize clusters
sns.scatterplot(
    data=df,
    x="Annual Income (k$)",
    y="Spending Score (1-100)",
    hue="Cluster",
    palette="viridis"
)

plt.title("Customer Segmentation")
plt.show()

# Interpret clusters
print(df.groupby("Cluster")[
    ["Annual Income (k$)", "Spending Score (1-100)"]
].mean().round(2))
