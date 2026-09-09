numbers = input("Enter numbers separated by space: ").split()

numbers = [int(x) for x in numbers]

print("Original list:", numbers)

numbers.append(int(input("Enter a number to append: ")))
print("After append:", numbers)

position = int(input("Enter position to insert: "))
value = int(input("Enter number to insert: "))
numbers.insert(position, value)
print("After insert:", numbers)

remove_number = int(input("Enter number to remove: "))
numbers.remove(remove_number)
print("After remove:", numbers)

numbers.sort()
print("After sort:", numbers)

numbers.reverse()
print("After reverse:", numbers)