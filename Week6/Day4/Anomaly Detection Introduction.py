
import numpy as np
import pandas as pd

data = pd.DataFrame({
    "TransactionAmount": [
        45, 50, 48, 52, 47, 55, 49, 51,
        46, 53, 50, 48, 500, 42, 1000
    ]
})

mean = data["TransactionAmount"].mean()
std = data["TransactionAmount"].std()

data["Z_Score"] = (
    data["TransactionAmount"] - mean
) / std

data["Z_Anomaly"] = data["Z_Score"].abs() > 3

Q1 = data["TransactionAmount"].quantile(0.25)
Q3 = data["TransactionAmount"].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

data["IQR_Anomaly"] = (
    (data["TransactionAmount"] < lower_bound) |
    (data["TransactionAmount"] > upper_bound)
)

print("Mean:", round(mean, 2))
print("Standard deviation:", round(std, 2))
print("Lower IQR bound:", lower_bound)
print("Upper IQR bound:", upper_bound)
print("\nAnomaly Detection Results:")
print(data.to_string(index=False))

print("\nZ-score anomalies:")
print(data[data["Z_Anomaly"]])

print("\nIQR anomalies:")
print(data[data["IQR_Anomaly"]])
