import string

speech = '''Four score and seven years ago our fathers brought forth
on this continent a new nation, conceived in Liberty, and
dedicated to the proposition that all men are created equal.'''

# Remove punctuation and convert to lowercase
translator = str.maketrans('', '', string.punctuation)
speech_cleaned = speech.translate(translator).lower()

# Split the cleaned sentence into words
words = speech_cleaned.split()

# Sort the words alphabetically
sorted_words = sorted(words)

# Print the sorted list of words
print("Words in alphabetical order:")
print(sorted_words)

# Print the first two words and the last two words
print("\nFirst two words:", sorted_words[:2])
print("Last two words:", sorted_words[-2:])
