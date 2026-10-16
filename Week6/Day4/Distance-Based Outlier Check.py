
import numpy as np
import matplotlib.pyplot as plt

X = np.array([
    [2, 3],
    [3, 4],
    [4, 3],
    [3, 2],
    [4, 4],
    [2, 4],
    [15, 15]
])

center = X.mean(axis=0)

distances = np.sqrt(np.sum((X - center) ** 2, axis=1))

threshold = 5

outliers = distances > threshold

print("Dataset center:", center)
print("\nDistances from center:")

for i, distance in enumerate(distances):
    print(f"Point {X[i]}: Distance = {distance:.2f}")

print("\nDetected outliers:")
print(X[outliers])

plt.scatter(X[~outliers, 0], X[~outliers, 1], label="Normal points")
plt.scatter(X[outliers, 0], X[outliers, 1], label="Outliers")

plt.scatter(center[0], center[1], marker="x", label="Dataset center")

plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("Distance-Based Outlier Detection")
plt.legend()
plt.grid(True)
plt.show()
