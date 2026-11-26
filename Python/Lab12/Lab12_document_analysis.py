sentence = input("Input: ")
print()
print("Enter a sentence:")
print("=" * 50)
print("DOCUMENT ANALYSIS REPORT")
print("=" * 50)
print(f"Sentence: {sentence}")
length = len(sentence)
print(f"Total characters: {length}")
print(" " * 50)
print("---Character Breakdown---")

words = sentence.split()
length_words = len(words)

vowels = 0
consonants = 0
digit = 0 
spaces = 0
special = 0

for ch in sentence:
    if ch.lower() in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digit += 1
    elif ch == " ":
        spaces += 1
    else:
        special += 1

print(f"Words              : {length_words}")
print(f"Vowels             : {vowels}")
print(f"Consonants         : {consonants}")
print(f"Digits             : {digit}")
print(f"Spaces             : {spaces}")
print(f"Special Characters : {special}")
print(" " * 50)
print("---Summary---")
total_letters = vowels + consonants
vowel_percentage = vowels * 100 / total_letters
print(f"Total Letters    : {total_letters}")
print(f"Vowel Percentage : {vowel_percentage:.1f}%")
print(" " * 50)
print("=" * 50)
print("Analysis Complete!")
print("=" * 50)