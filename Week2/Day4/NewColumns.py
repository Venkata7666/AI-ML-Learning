
import pandas as pd


students = pd.DataFrame(
	{
		"Student": ["Aarav", "Diya", "Kabir"],
		"Maths": [85, 92, 76],
		"Science": [90, 88, 81],
		"English": [78, 95, 74],
	}
)

# New columns can be calculated directly from existing columns.
students["Total Marks"] = students[["Maths", "Science", "English"]].sum(axis=1)
students["Percentage"] = students["Total Marks"] / 300 * 100
students["Passed"] = students["Percentage"] >= 40
students["Grade"] = students["Percentage"].apply(
	lambda percentage: (
		"A" if percentage >= 90 else
		"B" if percentage >= 75 else
		"C" if percentage >= 60 else
		"D"
	)
)

print(students)
