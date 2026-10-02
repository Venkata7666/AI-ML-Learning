import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

iris = load_iris()

X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target

print("Dataset:")
print(X.head())

print("\nShape:")
print(X.shape)

print("\nTarget Classes:")
print(iris.target_names)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

logistic_model = LogisticRegression(max_iter=200)
logistic_model.fit(X_train_scaled, y_train)

logistic_pred = logistic_model.predict(X_test_scaled)

logistic_accuracy = accuracy_score(y_test, logistic_pred)

print("\nLogistic Regression Accuracy:")
print(logistic_accuracy)

print("\nLogistic Regression Classification Report:")
print(classification_report(
    y_test,
    logistic_pred,
    target_names=iris.target_names
))

knn_model = KNeighborsClassifier(n_neighbors=5)
knn_model.fit(X_train_scaled, y_train)

knn_pred = knn_model.predict(X_test_scaled)

knn_accuracy = accuracy_score(y_test, knn_pred)

print("\nKNN Accuracy:")
print(knn_accuracy)

print("\nKNN Classification Report:")
print(classification_report(
    y_test,
    knn_pred,
    target_names=iris.target_names
))

print("\nLogistic Regression Confusion Matrix:")
print(confusion_matrix(y_test, logistic_pred))

print("\nKNN Confusion Matrix:")
print(confusion_matrix(y_test, knn_pred))

results = pd.DataFrame({
    "Model": ["Logistic Regression", "KNN"],
    "Accuracy": [logistic_accuracy, knn_accuracy]
})

print("\nModel Comparison:")
print(results)