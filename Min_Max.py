numbers = input("Enter numbers separated by space: ").split()

numbers = [int(x) for x in numbers]

largest = numbers[0]
smallest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

    if number < smallest:
        smallest = number

print("Largest number:", largest)
print("Smallest number:", smallest)