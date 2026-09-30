from sklearn.linear_model import LinearRegression
import numpy as np


X = np.array([[1], [2], [3], [4], [5]])
y = np.array([20, 40, 50, 65, 80])

model = LinearRegression()


model.fit(X, y)


predictions = model.predict(X)

print("Predictions:", predictions)

new_prediction = model.predict([[6]])

print("Predicted score for 6 hours:", new_prediction[0])