
import pandas as pd
import numpy as np

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix

from tensorflow.keras import Sequential
from tensorflow.keras.layers import Input, Dense

data = load_iris()

X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

X_test_original = X_test.copy()

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = Sequential([
    Input(shape=(4,)),
    Dense(16, activation="relu"),
    Dense(8, activation="relu"),
    Dense(3, activation="softmax")
])

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

model.fit(
    X_train,
    y_train,
    epochs=50,
    batch_size=8,
    verbose=0
)

probabilities = model.predict(X_test, verbose=0)
y_pred = np.argmax(probabilities, axis=1)

accuracy = accuracy_score(y_test, y_pred)

print("Test Accuracy:", round(accuracy, 4))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

wrong_indices = np.where(y_test != y_pred)[0]

print("\nTotal Test Samples:", len(y_test))
print("Incorrect Predictions:", len(wrong_indices))

if len(wrong_indices) == 0:
    print("No incorrect predictions found.")
else:
    errors = pd.DataFrame({
        "Actual Class": data.target_names[y_test[wrong_indices]],
        "Predicted Class": data.target_names[y_pred[wrong_indices]],
        "Sepal Length": X_test_original[wrong_indices, 0],
        "Sepal Width": X_test_original[wrong_indices, 1],
        "Petal Length": X_test_original[wrong_indices, 2],
        "Petal Width": X_test_original[wrong_indices, 3],
        "Prediction Confidence": np.max(
            probabilities[wrong_indices], axis=1
        ).round(4)
    })

    errors["Possible Reason"] = [
        "Similar features or overlapping class characteristics"
        for _ in wrong_indices
    ]

    print("\nMisclassified Samples:")
    print(errors.to_string(index=False))

    errors.to_csv("misclassified_samples.csv", index=False)

    print("\nError report saved to misclassified_samples.csv")

print("\nError Analysis Completed!")
