import nltk
from nltk.corpus import brown

# Get all words in brown corpus greater than 8 characters and lowercase them.
words = [w.lower() for w in brown.words() if len(w) >= 8]
# Create anagram dict.
anagrams = {}

for w in set(words):

    # Alphabetize the word
    alphabetized_word = ''.join(sorted(w))

    # Append the word to the appropriate anagram.
    # If anagram is not in 'anagrams' dict, create key and append word.
    if alphabetized_word not in anagrams:
        anagrams[alphabetized_word] = [w]
    else:
        anagrams[alphabetized_word].append(w)

# Write anagrams and keys to file by increasing length
f = open('anagrams_output.txt', 'w')
for a in sorted(anagrams, key=len):
    assoc_words = ', '.join(anagrams[a])
    f.write(f'Anagram: {a}\nAssociated word(s): {assoc_words}\n\n')
f.close()
