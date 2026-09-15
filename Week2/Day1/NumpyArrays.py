
import numpy as np
array_1d = np.array([1, 2, 3, 4, 5])
array_2d = np.array([[1, 2, 3], [4, 5, 6]])


for name, array in (("1D array", array_1d), ("2D array", array_2d)):
	print(name)
	print(array)
	print(f"Shape: {array.shape}")
	print(f"Size: {array.size}")
	print(f"Number of dimensions: {array.ndim}")
