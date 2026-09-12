
marks = {
    "ramu": [85, 90, 78, 88, 92],
    "raj": [70, 75, 80, 82, 78],
    "rai": [64, 68, 72, 70, 74],
    "shiva": [88, 91, 95, 90, 93],
    "kittu": [76, 80, 79, 82, 84]
}

def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

print("Student Marks Report")
print("=" * 25)

for student, scores in marks.items():
    average = sum(scores) / len(scores)
    grade = calculate_grade(average)
    print(f"{student}: Average = {average:.2f}, Grade = {grade}")
