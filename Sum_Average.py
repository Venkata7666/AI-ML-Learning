def find_sum(numbers):
    total = 0

    for number in numbers:
        total = total + number

    return total


def find_average(numbers):
    total = find_sum(numbers)
    average = total / len(numbers)

    return average


numbers = input("Enter numbers separated by space: ").split()
numbers = [int(x) for x in numbers]

total = find_sum(numbers)
average = find_average(numbers)

print("Sum:", total)
print("Average:", average)