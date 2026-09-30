import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

X = np.array([[1], [2], [3], [4], [5]])
y = np.array([20, 40, 50, 65, 80])

model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)

mae = mean_absolute_error(y, y_pred)

mse = mean_squared_error(y, y_pred)

print("Actual values:", y)
print("Predicted values:", y_pred)
print("MAE:", mae)
print("MSE:", mse)