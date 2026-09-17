
import pandas as pd


# Create a DataFrame from a dictionary of equally sized lists.
students = {
	"Name": ["Aisha", "Ben", "Carlos", "Diana"],
	"Age": [20, 21, 19, 22],
	"Score": [88, 92, 79, 95],
}
students_df = pd.DataFrame(students)
courses = [
	{"Course": "Python", "Hours": 10},
	{"Course": "Pandas", "Hours": 8},
	{"Course": "NumPy", "Hours": 6},
]
courses_df = pd.DataFrame(courses)
attendance = [
	["Aisha", 5],
	["Ben", 4],
	["Carlos", 5],
]
attendance_df = pd.DataFrame(attendance, columns=["Name", "Days Present"])


if __name__ == "__main__":
	print("Students DataFrame:\n", students_df)
	print("\nFirst two rows:\n", students_df.head(2))
	print("\nLast row:\n", students_df.tail(1))
	print("\nColumn names:", list(students_df.columns))
	print("Row labels:", list(students_df.index))
	print("Shape (rows, columns):", students_df.shape)
	print("\nScore column:\n", students_df["Score"])
	print("\nCourses DataFrame:\n", courses_df)
	print("\nAttendance DataFrame:\n", attendance_df)

