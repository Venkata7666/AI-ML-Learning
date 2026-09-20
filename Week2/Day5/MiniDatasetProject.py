import pandas as pd


def main():
    data = [
        {"student": "Aisha", "subject": "Math", "marks": "78"},
        {"student": "Ben", "subject": "Math", "marks": "65"},
        {"student": "Chloe", "subject": "Science", "marks": "88"},
        {"student": "Diego", "subject": "Science", "marks": None},
        {"student": "Aisha", "subject": "Math", "marks": "78"},  # duplicate
        {"student": "Eva", "subject": "English", "marks": "92"},
        {"student": "Farah", "subject": "English", "marks": "71"},
    ]

    df = pd.DataFrame(data)
    print("Original dataset:\n", df, "\n", sep="")

    df["student"] = df["student"].str.strip()
    df["subject"] = df["subject"].str.strip().str.title()
    df["marks"] = pd.to_numeric(df["marks"], errors="coerce")
    df = df.drop_duplicates().copy()
    df["marks"] = df["marks"].fillna(df["marks"].mean()).round(1)
    df["marks"] = df["marks"].clip(0, 100)

    def grade(mark):
        if mark >= 90:
            return "A"
        if mark >= 80:
            return "B"
        if mark >= 70:
            return "C"
        if mark >= 60:
            return "D"
        return "F"

    df["grade"] = df["marks"].apply(grade)

    print("Cleaned dataset:\n", df.to_string(index=False), "\n", sep="")
    print("Summary")
    print(f"Students/records: {len(df)}")
    print(f"Average mark: {df['marks'].mean():.1f}")
    print(f"Highest mark: {df['marks'].max():.1f} ({df.loc[df['marks'].idxmax(), 'student']})")
    print(f"Lowest mark: {df['marks'].min():.1f} ({df.loc[df['marks'].idxmin(), 'student']})")
    print(f"Pass rate (mark >= 50): {(df['marks'].ge(50).mean() * 100):.1f}%")
    print("Average by subject:")
    print(df.groupby("subject")["marks"].mean().round(1).to_string())
    print("Grade counts:")
    print(df["grade"].value_counts().sort_index().to_string())


if __name__ == "__main__":
    main()