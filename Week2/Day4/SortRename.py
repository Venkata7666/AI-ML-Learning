
import pandas as pd
def main() -> None:
	students = pd.DataFrame(
		{
			"Student Name": ["Ava", "Noah", "Mia", "Liam"],
			"Course Score": [88, 95, 88, 76],
			"Study Hours": [6, 8, 7, 5],
		}
	)

	# Rename columns to concise, Python-friendly names.
	renamed = students.rename(
		columns={
			"Student Name": "name",
			"Course Score": "score",
			"Study Hours": "hours",
		}
	)

	# Sort by score descending, then hours ascending for tied scores.
	sorted_students = renamed.sort_values(
		by=["score", "hours"],
		ascending=[False, True],
	).reset_index(drop=True)

	print("Renamed and sorted records:")
	print(sorted_students.to_string(index=False))
if __name__ == "__main__":
	main()
