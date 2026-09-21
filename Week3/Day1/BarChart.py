import matplotlib.pyplot as plt
categories = ["Apples", "Bananas", "Cherries", "Dates"]
values = [25, 40, 30, 15]

plt.bar(categories, values, color="steelblue")
plt.title("Fruit Sales")
plt.xlabel("Fruit")
plt.ylabel("Quantity Sold")
plt.tight_layout()
plt.show()
