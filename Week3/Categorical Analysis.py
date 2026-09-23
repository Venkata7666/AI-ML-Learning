import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "category": ["A", "B", "A", "C", "B", "A", "C", "B", "A", "C"],
    "sales": [24, 31, 18, 42, 35, 27, 51, 39, 46, 58]
})

# Count by category
sns.countplot(data=data, x="category")
plt.title("Category Counts")
plt.show()

# Average sales by category
avg_sales = data.groupby("category")["sales"].mean()

avg_sales.plot(kind="bar")
plt.title("Average Sales by Category")
plt.xlabel("Category")
plt.ylabel("Average Sales")
plt.show()