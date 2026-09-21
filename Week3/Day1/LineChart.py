import matplotlib.pyplot as plt
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
values = [12, 18, 15, 22, 25, 20, 28]

plt.figure(figsize=(8, 5))
plt.plot(days, values, marker="o", linewidth=2, color="steelblue", label="Value")
plt.title("Weekly Values", fontsize=16)
plt.xlabel("Day", fontsize=12)
plt.ylabel("Value", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()
