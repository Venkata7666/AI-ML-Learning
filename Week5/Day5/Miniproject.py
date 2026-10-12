import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

df = pd.DataFrame({
    "StudyHours": [1, 2, 3, 4, 5, 6, 7, 8, 2, 9],
    "Attendance": [50, 55, 60, 65, 70, 75, 80, 90, 58, 95],
    "PreviousScore": [35, 40, 45, 50, 55, 65, 70, 85, 42, 90],
    "Pass": [0, 0, 0, 1, 1, 1, 1, 1, 0, 1]
})

X = df.drop("Pass", axis=1)
y = df["Pass"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

models = {
    "Logistic Regression": LogisticRegression(),
    "Random Forest": RandomForestClassifier(random_state=42)
}

results = {}

for name, model in models.items():
    if name == "Logistic Regression":
        model.fit(X_train_scaled, y_train)
        predictions = model.predict(X_test_scaled)
    else:
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    results[name] = accuracy

    print("\nModel:", name)
    print("Accuracy:", accuracy)
    print(classification_report(y_test, predictions, zero_division=0))

best_model = max(results, key=results.get)

print("Best Model:", best_model)
print("Best Accuracy:", results[best_model])