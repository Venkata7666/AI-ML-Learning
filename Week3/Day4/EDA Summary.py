import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("your_dataset.csv")

df['Age'].hist()
plt.title('Age Distribution')
plt.show()

df['Gender'].value_counts().plot(kind='bar')
plt.title('Gender Count')
plt.show()

df.groupby('Gender')['Salary'].mean().plot(kind='bar')
plt.title('Average Salary')
plt.show()

df.plot(x='Age', y='Salary', kind='scatter')
plt.title('Age vs Salary')
plt.show()

df.corr(numeric_only=True).plot(kind='bar')
plt.title('Correlation')
plt.show()