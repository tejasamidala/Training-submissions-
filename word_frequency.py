text = input("Enter a sentence: ").lower()

words = text.split()
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("\nWord Frequency:")
for word, count in frequency.items():
    print(f"{word}: {count}")