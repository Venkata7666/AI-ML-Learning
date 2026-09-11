def square(n):
    return n * n


def cube(n):
    return n * n * n

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

num1 = int(input("Enter a number for square: "))
print("Square:", square(num1))

num2 = int(input("Enter a number for cube: "))
print("Cube:", cube(num2))

num3 = int(input("Enter a number for factorial: "))
print("Factorial:", factorial(num3))

principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time in years: "))

print("Simple Interest:", simple_interest(principal, rate, time))