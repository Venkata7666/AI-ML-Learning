"""Practice NumPy array indexing and slicing."""

import numpy as np
numbers = np.array([10, 20, 30, 40, 50])
print("Original array:", numbers)
print("First element:", numbers[0])
print("Last element:", numbers[-1])
print("Elements 2 through 4:", numbers[1:4])
print("Every second element:", numbers[::2])

matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
])
print("\nMatrix:\n", matrix)
print("Element at row 2, column 3:", matrix[1, 2])
print("First row:", matrix[0, :])
print("Last column:", matrix[:, -1])
print("First two rows:\n", matrix[:2, :])
print("Columns 2 and 3:\n", matrix[:, 1:3])
top_left = matrix[:2, :2]
top_left[0, 0] = 99
print("\nMatrix after changing its top-left slice:\n", matrix)