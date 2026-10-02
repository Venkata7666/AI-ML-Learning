import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

data = {
    "Age": [22, 25, 28, 35, 40, 45, 50, 55, 60, 65],
    "Income": [25000, 30000, 35000, 45000, 50000, 60000, 70000, 80000, 90000, 100000],
    "Purchased": [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[["Age", "Income"]]
y = df["Purchased"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

standard_scaler = StandardScaler()

X_train_standard = standard_scaler.fit_transform(X_train)
X_test_standard = standard_scaler.transform(X_test)

knn_standard = KNeighborsClassifier(n_neighbors=3)
knn_standard.fit(X_train_standard, y_train)

pred_standard = knn_standard.predict(X_test_standard)

standard_accuracy = accuracy_score(y_test, pred_standard)

minmax_scaler = MinMaxScaler()

X_train_minmax = minmax_scaler.fit_transform(X_train)
X_test_minmax = minmax_scaler.transform(X_test)

knn_minmax = KNeighborsClassifier(n_neighbors=3)
knn_minmax.fit(X_train_minmax, y_train)

pred_minmax = knn_minmax.predict(X_test_minmax)

minmax_accuracy = accuracy_score(y_test, pred_minmax)

print("StandardScaler Accuracy:", standard_accuracy)
print("MinMaxScaler Accuracy:", minmax_accuracy)