
"""Coding test: loops, strings, lists, and functions.
"""
def analyze_sentence(sentence):
	words = sentence.split()
	longest_word = ""

	for word in words:
		cleaned_word = word.strip(".,!?;:").lower()
		if len(cleaned_word) > len(longest_word):
			longest_word = cleaned_word

	return words, len(words), len(sentence), longest_word


def count_vowels(sentence):
	vowels = "aeiou"
	count = 0

	for character in sentence.lower():
		if character in vowels:
			count += 1

	return count


def main():
	sentence = input("Enter a sentence: ").strip()

	if not sentence:
		print("Please enter at least one word.")
		return

	words, word_count, character_count, longest_word = analyze_sentence(sentence)
	unique_words = []

	for word in words:
		cleaned_word = word.strip(".,!?;:").lower()
		if cleaned_word not in unique_words:
			unique_words.append(cleaned_word)

	print("\nResults")
	print(f"Words: {words}")
	print(f"Word count: {word_count}")
	print(f"Character count: {character_count}")
	print(f"Vowel count: {count_vowels(sentence)}")
	print(f"Longest word: {longest_word}")
	print(f"Unique words: {unique_words}")


if __name__ == "__main__":
	main()
