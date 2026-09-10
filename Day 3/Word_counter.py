sentence = input("Enter a sentence: ")

words = sentence.split()

print("Number of words:", len(words))

for word in words:
    print(f"{word}: {len(word)}")
