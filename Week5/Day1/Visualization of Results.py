from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

iris = load_iris()

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = DecisionTreeClassifier(max_depth=3, random_state=42)

model.fit(X_train, y_train)

importance = model.feature_importances_

plt.bar(iris.feature_names, importance)
plt.xticks(rotation=45)
plt.ylabel("Importance")
plt.title("Decision Tree Feature Importance")
plt.tight_layout()
plt.show()