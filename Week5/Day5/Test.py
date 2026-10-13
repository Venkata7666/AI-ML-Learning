#Conduct a coding test on model training, prediction, and evaluation.
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
data = {
    "Hours": [1, 2, 3, 4, 5, 6],
    "Marks": [20, 40, 60, 40, 80, 100 ]
}

df = pd.DataFrame(data)
X = df[["Hours"]]
y = df["Marks"]     

model = LinearRegression()
model.fit(X, y)     
y_pred = model.predict(X)

print("Predictions:", y_pred)
print("MAE:", mean_absolute_error(y, y_pred))
print("MSE:", mean_squared_error(y, y_pred))
print("R2 Score:", r2_score(y, y_pred))
print("New Prediction:", model.predict(pd.DataFrame({"Hours": [7]})))
