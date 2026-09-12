
# Problem 1: Text Analyzer
# Combine strings, loops, conditionals, and lists.
def analyze_text(text):
    words = text.split()
    vowel_count = 0
    letter_count = 0

    for char in text.lower():
        if char.isalpha():
            letter_count += 1
        if char in "aeiou":
            vowel_count += 1

    consonant_count = letter_count - vowel_count

    return {
        "word_count": len(words),
        "letter_count": letter_count,
        "vowel_count": vowel_count,
        "consonant_count": consonant_count,
    }


# Problem 2: Student Score Report
# Combine dictionaries, loops, conditions, and averages.
def score_report(scores):
    total = 0
    for subject, score in scores.items():
        total += score

    average = total / len(scores)

    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"

    return {
        "average": round(average, 2),
        "grade": grade,
        "highest_subject": max(scores, key=scores.get),
    }


# Problem 3: Prime Number Generator
# Combine functions, loops, conditionals, and lists.
def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    divisor = 3
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 2

    return True


def first_n_primes(n):
    if n <= 0:
        return []

    primes = []
    current = 2

    while len(primes) < n:
        if is_prime(current):
            primes.append(current)
        current += 1

    return primes


#  runs for the mini practice set.
if __name__ == "__main__":
    print("Problem 1: Text Analyzer")
    text_result = analyze_text("This is best programming language ")
    print(text_result)

    print("\nProblem 2: Student Score Report")
    student_scores = {
        "Math": 88,
        "Science": 94,
        "English": 82,
        "History": 76,
    }
    print(score_report(student_scores))

    print("\nProblem 3: First 8 Prime Numbers")
    print(first_n_primes(8))

