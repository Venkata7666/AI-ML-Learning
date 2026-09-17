
import pandas as pd


students = pd.DataFrame(
    {
        "name": ["Asha", "Ben", "Chloe", "Diego"],
        "age": [20, 21, 19, 22],
        "course": ["Python", "SQL", "Python", "ML"],
        "score": [88, 72, 95, 64],
    }
)

names = students["name"]

student_scores = students[["name", "course", "score"]]

high_scores = students[students["score"] >= 80]

python_students = students[
    (students["course"] == "Python") & (students["score"] >= 90)
]

top_students = students.loc[students["score"] >= 80, ["name", "score"]]

print("All students:\n", students)
print("\nNames:\n", names)
print("\nSelected columns:\n", student_scores)
print("\nScores of 80 or higher:\n", high_scores)
print("\nPython students scoring at least 90:\n", python_students)
print("\nTop student details:\n", top_students)