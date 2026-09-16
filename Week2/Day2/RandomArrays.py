"""Generate random integer and floating-point arrays and inspect their ranges."""

import numpy as np


# A seed makes the example reproducible while still using random generation.
rng = np.random.default_rng(42)

random_integers = rng.integers(1, 101, size=10)
random_floats = rng.random(10)

print("Random integers:", random_integers)
print("Integer range:", random_integers.min(), "to", random_integers.max())
print("Integer shape:", random_integers.shape)

print("\nRandom floats:", random_floats)
print("Float range:", random_floats.min(), "to", random_floats.max())
print("Float shape:", random_floats.shape)
