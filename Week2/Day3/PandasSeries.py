
import pandas as pd

temperatures = pd.Series([22, 25, 19, 28, 24])
days = pd.Series(
    [22, 25, 19, 28, 24],
    index=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    name="Temperature (C)",
)
scores = pd.Series({"Alice": 88, "Bob": 76, "Charlie": 93, "Diana": 84})

first_temperature = temperatures.iloc[0]
thursday_temperature = days.loc["Thursday"]
first_two_days = days.iloc[:2]
selected_days = days.loc[["Monday", "Friday"]]
score_values = scores.values

hot_days = days[days > 23]
passing_scores = scores[scores >= 80]


if __name__ == "__main__":
    print("Temperatures:\n", temperatures)
    print("\nNamed Series:\n", days)
    print("\nScores:\n", scores)
    print("\nFirst temperature:", first_temperature)
    print("Thursday temperature:", thursday_temperature)
    print("\nFirst two days:\n", first_two_days)
    print("\nSelected days:\n", selected_days)
    print("\nHot days:\n", hot_days)
    print("\nPassing scores:\n", passing_scores)
    print("\nScore values:", score_values)