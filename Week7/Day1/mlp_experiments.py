
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

data = load_iris()
X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

experiments = [
    {"hidden_layers": (5,), "activation": "relu", "epochs": 50},
    {"hidden_layers": (10,), "activation": "relu", "epochs": 100},
    {"hidden_layers": (20,), "activation": "relu", "epochs": 200},
    {"hidden_layers": (10,), "activation": "tanh", "epochs": 100},
    {"hidden_layers": (10, 5), "activation": "relu", "epochs": 200}
]

results = []

for exp in experiments:
    model = MLPClassifier(
        hidden_layer_sizes=exp["hidden_layers"],
        activation=exp["activation"],
        max_iter=exp["epochs"],
        random_state=42,
        solver="adam",
        early_stopping=False
    )

    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    results.append({
        "Hidden Layers": str(exp["hidden_layers"]),
        "Activation": exp["activation"],
        "Max Epochs": exp["epochs"],
        "Actual Iterations": model.n_iter_,
        "Accuracy": round(accuracy, 4),
        "Converged": model.n_iter_ < exp["epochs"]
    })

df = pd.DataFrame(results)
print(df.to_string(index=False))
