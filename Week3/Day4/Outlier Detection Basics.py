import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({"values": [10, 12, 11, 13, 12, 14, 15, 13, 100]})

q1 = data["values"].quantile(0.25)
q3 = data["values"].quantile(0.75)
iqr = q3 - q1
lower_limit = q1 - 1.5 * iqr
upper_limit = q3 + 1.5 * iqr

outliers = data[(data["values"] < lower_limit) | (data["values"] > upper_limit)]
print("Outliers:")
print(outliers)


plt.boxplot(data["values"])
plt.ylabel("Values")
plt.title("Outlier Detection with a Box Plot")
plt.show()