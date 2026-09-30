import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

X = np.array([[1], [2], [3], [4], [5]])
y = np.array([20, 40, 50, 65, 80])


model = LinearRegression()
model.fit(X, y)

coefficient = model.coef_[0]
intercept = model.intercept_


y_pred = model.predict(X)

new_prediction = model.predict([[6]])[0]


mae = mean_absolute_error(y, y_pred)
mse = mean_squared_error(y, y_pred)

print("Coefficient:", coefficient)
print("Intercept:", intercept)
print("Actual Values:", y)
print("Predicted Values:", y_pred)
print("Prediction for X = 6:", new_prediction)
print("MAE:", mae)
print("MSE:", mse)


print("\nInterpretation Notes:")
print("1. The coefficient shows how much the predicted output changes when X increases by 1 unit.")
print("2. The intercept represents the predicted output when X is 0.")
print("3. The model predicts the expected output for a new input value.")
print("4. Lower MAE and MSE indicate that predictions are closer to the actual values.")
print("5. The model shows a positive linear relationship between X and y.")