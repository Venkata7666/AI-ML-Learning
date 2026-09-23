import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "category": ["A", "B", "A", "C", "B", "A", "C", "B", "A", "C"],
    "sales": [24, 31, 18, 42, 35, 27, 51, 39, 46, 58],
    "customers": [12, 16, 9, 21, 17, 13, 24, 19, 22, 28]
})

sns.set_theme(style="whitegrid")

# Count Plot
sns.countplot(data=data, x="category")
plt.show()

# Box Plot
sns.boxplot(data=data, x="category", y="sales")
plt.show()

# Pair Plot
sns.pairplot(data, vars=["sales", "customers"], hue="category")
plt.show()