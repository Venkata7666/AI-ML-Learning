print("Simple Calculator")
print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")

choice = input("Choose 1, 2, 3 or 4: ")

a = float(input("First number: "))
b = float(input("Second number: "))

if choice == "1":
    answer = a + b
elif choice == "2":
    answer = a - b
elif choice == "3":
    answer = a * b
elif choice == "4":
    if b == 0:
        print("Cannot divide by zero")
        answer = None
    else:
        answer = a / b
else:
    print("Wrong choice")
    answer = None

if answer is not None:
    print("Answer =", answer)