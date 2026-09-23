
import matplotlib.pyplot as plt


months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [120, 150, 135, 180, 210, 240]
products = ["A", "B", "C", "D"]
units_sold = [35, 50, 42, 65]
advertising = [10, 15, 20, 25, 30, 35]
customers = [100, 125, 140, 165, 190, 225]


# Purpose - identify the trend in sales over time.
plt.figure(figsize=(7, 4))
plt.plot(months, sales, marker="o", color="steelblue")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()

# Purpose - compare the number of units sold for each product.
plt.figure(figsize=(7, 4))
plt.bar(products, units_sold, color="darkorange")
plt.title("Units Sold by Product")
plt.xlabel("Product")
plt.ylabel("Units Sold")
plt.tight_layout()

# Purpose - examine the relationship between advertising and customers.
plt.figure(figsize=(7, 4))
plt.scatter(advertising, customers, color="seagreen", s=70)
plt.title("Advertising Spend vs. Customers")
plt.xlabel("Advertising Spend (thousands)")
plt.ylabel("Number of Customers")
plt.grid(True, linestyle=":", alpha=0.6)
plt.tight_layout()

plt.show()
