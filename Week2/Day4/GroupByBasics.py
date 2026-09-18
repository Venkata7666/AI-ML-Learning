import pandas as pd


def main() -> None:
	sales = pd.DataFrame(
		{
			"category": ["Books", "Books", "Games", "Games", "Games", "Music"],
			"item": ["Novel", "Notebook", "Chess", "Puzzle", "Cards", "Album"],
			"price": [12.0, 8.0, 25.0, 18.0, 10.0, 15.0],
		}
	)

	# Count the number of products in each category.
	counts = sales.groupby("category").size().rename("count")

	# Calculate the average price for each category.
	average_prices = sales.groupby("category")["price"].mean().rename("average_price")

	# Multiple aggregations can be combined in one grouped result.
	summary = sales.groupby("category").agg(
		count=("item", "count"),
		average_price=("price", "mean"),
	)

	print("Counts by category:")
	print(counts)
	print("\nAverage price by category:")
	print(average_prices)
	print("\nCategory summary:")
	print(summary)


if __name__ == "__main__":
	main()
