
from pathlib import Path

import matplotlib.pyplot as plt


PROJECT_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = PROJECT_DIR / "saved_charts"


def save_charts() -> None:
	"""Create example charts and save them as PNG files."""
	OUTPUT_DIR.mkdir(exist_ok=True)

	months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
	sales = [24, 31, 28, 40, 45, 52]

	plt.figure(figsize=(8, 5))
	plt.plot(months, sales, marker="o", color="steelblue")
	plt.title("Monthly Sales")
	plt.xlabel("Month")
	plt.ylabel("Sales")
	plt.grid(alpha=0.3)
	plt.tight_layout()
	plt.savefig(OUTPUT_DIR / "monthly_sales_line.png", dpi=150)
	plt.close()

	plt.figure(figsize=(8, 5))
	plt.bar(months, sales, color="darkorange")
	plt.title("Monthly Sales")
	plt.xlabel("Month")
	plt.ylabel("Sales")
	plt.tight_layout()
	plt.savefig(OUTPUT_DIR / "monthly_sales_bar.png", dpi=150)
	plt.close()


if __name__ == "__main__":
	save_charts()
	print(f"Charts saved to: {OUTPUT_DIR}")
