import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "sales": [24, 31, 18, 42, 35, 27, 51, 39, 46, 58],
    "customers": [12, 16, 9, 21, 17, 13, 24, 19, 22, 28]
})

# Distribution
sns.histplot(data["sales"], kde=True)
plt.show()

sns.histplot(data["customers"], kde=True)
plt.show()

# Mean and Median
print("Sales Mean:", data["sales"].mean())
print("Sales Median:", data["sales"].median())

print("Customers Mean:", data["customers"].mean())
print("Customers Median:", data["customers"].median())