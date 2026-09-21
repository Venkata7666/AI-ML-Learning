import matplotlib.pyplot as plt
import numpy as np


rng = np.random.default_rng(42)
data = rng.normal(loc=50, scale=10, size=500)

fig, axes = plt.subplots(1, 3, figsize=(15, 4), sharex=True, sharey=True)

for ax, bin_count in zip(axes, (5, 15, 30)):
	ax.hist(data, bins=bin_count, color="steelblue", edgecolor="black")
	ax.set_title(f"{bin_count} bins")
	ax.set_xlabel("Value")
	ax.set_ylabel("Frequency")
	ax.grid(axis="y", alpha=0.3)

fig.suptitle("Histogram of Random Numeric Data")
fig.tight_layout()
plt.show()
