def even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


numbers = input("Enter 5 numbers: ").split()

for number in numbers:
    number = int(number)
    result = even_odd(number)
    print(number, "is", result)