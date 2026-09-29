import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


data = {
    "Hours_Studied": [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    "Attendance": [60, 65, 70, 75, 80, 82, 85, 90, 92, 95],
    "Previous_Score": [50, 55, 58, 62, 65, 70, 72, 78, 82, 85],
    "Exam_Score": [52, 57, 61, 65, 69, 73, 76, 82, 86, 90]
}

df = pd.DataFrame(data)


X = df[["Hours_Studied", "Attendance", "Previous_Score"]]
y = df["Exam_Score"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
model = LinearRegression()


model.fit(X_train, y_train)


y_pred = model.predict(X_test)


mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)


print("Actual Values:")
print(y_test.values)

print("\nPredicted Values:")
print(y_pred)

print("\nModel Evaluation:")
print("Mean Absolute Error (MAE):", mae)
print("Mean Squared Error (MSE):", mse)
print("R2 Score:", r2)