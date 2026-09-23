import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "sales": [24, 31, 18, 42, 35, 27, 51, 39, 46, 58],
    "customers": [12, 16, 9, 21, 17, 13, 24, 19, 22, 28],
    "profit": [5, 7, 3, 10, 8, 6, 12, 9, 11, 14]
})

correlation = data.corr()

sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()