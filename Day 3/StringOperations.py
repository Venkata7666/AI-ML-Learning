def string_length(text):
    return len(text)
def to_uppercase(text):
    return text.upper()

def to_lowercase(text):
    
    return text.lower()


def reverse_string(text):
    
    return text[::-1]


def vowel_count(text):
    
    vowels = "aeiou"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count

if __name__ == "__main__":
    sample = "Techquest"

    print("Original:", sample)
    print("Length:", string_length(sample))
    print("Uppercase:", to_uppercase(sample))
    print("Lowercase:", to_lowercase(sample))
    print("Reversed:", reverse_string(sample))
    print("Vowel Count:", vowel_count(sample))

