import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([20, 40, 50, 65, 80])

model = LinearRegression()
model.fit(X, y)


y_pred = model.predict(X)


print("Actual values:", y)
print("Predicted values:", y_pred)


plt.scatter(y, y_pred)

plt.xlabel("Actual Values")
plt.ylabel("Predicted Values")
plt.title("Actual vs Predicted Values")

plt.show()