word = input("Enter a word: ")

reverse = ""

for letter in word:
    reverse = letter + reverse

if word == reverse:
    print("It is a Palindrome")
else:
    print("It is not a Palindrome")