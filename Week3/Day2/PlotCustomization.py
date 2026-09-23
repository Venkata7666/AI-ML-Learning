

import matplotlib.pyplot as plt


months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales_2023 = [120, 135, 128, 150, 165, 180]
sales_2024 = [130, 142, 145, 158, 175, 195]

plt.figure(figsize=(10, 6))
plt.plot(months, sales_2023, marker="o", linewidth=2, label="2023")
plt.plot(months, sales_2024, marker="s", linewidth=2, label="2024")

plt.title("Monthly Sales Comparison", fontsize=16)
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend(title="Year")
plt.tight_layout()
plt.show()