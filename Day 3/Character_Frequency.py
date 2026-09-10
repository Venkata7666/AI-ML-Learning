text = input("Enter a string: ")

frequency = {}

for character in text:
    if character in frequency:
        frequency[character] = frequency[character] + 1
    else:
        frequency[character] = 1

print("Character frequency:")

for character in frequency:
    print(character, ":", frequency[character])