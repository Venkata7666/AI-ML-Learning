import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv("data.csv")

X = df.drop("target", axis=1)
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

tree = DecisionTreeClassifier(
    random_state=42
)

forest = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

tree.fit(X_train, y_train)
forest.fit(X_train, y_train)

tree_pred = tree.predict(X_test)
forest_pred = forest.predict(X_test)

tree_accuracy = accuracy_score(y_test, tree_pred)
forest_accuracy = accuracy_score(y_test, forest_pred)

print("Decision Tree Accuracy:", tree_accuracy)
print("Random Forest Accuracy:", forest_accuracy)

print("\nDecision Tree Classification Report:")
print(classification_report(y_test, tree_pred))

print("\nRandom Forest Classification Report:")
print(classification_report(y_test, forest_pred))

print("\nComparison:")
if forest_accuracy > tree_accuracy:
    print("Random Forest performed better than Decision Tree.")
elif tree_accuracy > forest_accuracy:
    print("Decision Tree performed better than Random Forest.")
else:
    print("Both models performed equally.")