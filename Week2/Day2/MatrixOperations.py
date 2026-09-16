import numpy as np
matrix_a = np.array([
    [1, 2],
    [3, 4],
])
matrix_b = np.array([
    [5, 6],
    [7, 8],
])

addition = matrix_a + matrix_b
multiplication = matrix_a @ matrix_b

print("Matrix A:")
print(matrix_a)
print("\nMatrix B:")
print(matrix_b)
print("\nAddition:")
print(addition)
print("\nMultiplication:")
print(multiplication)