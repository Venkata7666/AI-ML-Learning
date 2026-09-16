import numpy as np

# Create a 1D array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

print("Original array:")
print(arr)
print("Shape:", arr.shape)

# Reshape 1D array into 2D
reshaped = arr.reshape(3, 4)

print("\nReshaped array:")
print(reshaped)
print("Shape:", reshaped.shape)

# Flatten the 2D array
flattened = reshaped.flatten()

print("\nFlattened array:")
print(flattened)
print("Shape:", flattened.shape)

# Compare
print("\nOriginal == Flattened:", np.array_equal(arr, flattened))