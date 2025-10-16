"""
CP1404 Practical 05
word occurrences
Estimate: 20 min
Actual: 9 min
"""

word_to_count = {}
text = input("Enter some text: ")
words = text.split()
for word in words:
    frequency = word_to_count.get(word, 0)
    word_to_count[word] = frequency + 1

max_length = max(len(word) for word in words)
for word in sorted(word_to_count):
    print(f"{word:{max_length}} : {word_to_count[word]}")
