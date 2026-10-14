import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

data = {
    'Customer': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    'Annual_Income': [15, 16, 17, 18, 45, 48, 50, 80, 85, 90],
    'Spending_Score': [80, 85, 78, 82, 40, 45, 42, 20, 15, 18]
}

df = pd.DataFrame(data)

X = df[['Annual_Income', 'Spending_Score']]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df['Cluster'] = kmeans.fit_predict(X_scaled)

print("Customer Dataset with Cluster Labels:")
print(df)

print("\nNumber of Customers in Each Cluster:")
print(df['Cluster'].value_counts().sort_index())

print("\nAverage Values for Each Cluster:")
print(df.groupby('Cluster')[['Annual_Income', 'Spending_Score']].mean().round(2))

plt.figure(figsize=(8, 5))
plt.scatter(
    df['Annual_Income'],
    df['Spending_Score'],
    c=df['Cluster'],
    cmap='viridis',
    s=100
)

for i, customer in enumerate(df['Customer']):
    plt.annotate(customer, (df['Annual_Income'][i], df['Spending_Score'][i]))

plt.xlabel('Annual Income (in thousands)')
plt.ylabel('Spending Score')
plt.title('Customer Segmentation Using K-Means')
plt.show()