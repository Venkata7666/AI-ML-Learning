import pandas as pd

results = {
    "Model": [
        "Logistic Regression",
        "Decision Tree",
        "Random Forest",
        "KNN"
    ],
    "Accuracy": [
        0.85,
        0.82,
        0.91,
        0.87
    ]
}

accuracy_df = pd.DataFrame(results)

print(accuracy_df)