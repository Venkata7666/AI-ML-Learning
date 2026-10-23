
import numpy as np
import tensorflow as tf
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.models import load_model

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

loss, accuracy = model.evaluate(X_test, y_test, verbose=0)

print("Original Model Accuracy:", round(accuracy, 4))

model.save("iris_model.keras")
print("Model saved successfully!")

loaded_model = load_model("iris_model.keras")
print("Model loaded successfully!")

predictions = loaded_model.predict(X_test[:5], verbose=0)
predicted_classes = np.argmax(predictions, axis=1)

print("Predicted Classes:", predicted_classes)
print("Actual Classes:", y_test[:5])

print(
    "Predictions match:",
    np.array_equal(predicted_classes, model.predict_classes(X_test[:5]))
    if hasattr(model, "predict_classes")
    else np.array_equal(
        predicted_classes,
        np.argmax(model.predict(X_test[:5], verbose=0), axis=1)
    )
)
