# Anagrams

> Creates a list of anagrams with a length greater than or equal to 8---and their corresponding words---found in the Brown Corpus (via NLTK).

This script was produced using Python 3.7.2 and was originally submitted as homework for LING 38600 'Computational Linguistics' taught by John Goldsmith at the University of Chicago, spring quarter 2019.

The code is fairly straightforward and operates under the following steps:

1. Import the Brown Corpus using NLTK (note that this contains 1.15M words as opposed to the 235K-word slice provided by Prof. Goldsmith).
2. Retrieve all words greater than 8 characters in length and lowercase them, stored in `words`.
3. Create a dictionary `anagrams`.
4. For each unique word in `words`: alphabetize the word, then check if the alphabetized word (i.e., the word's anagram in this case) is already in `anagrams`. If not, create a new key for the anagram in `anagrams` and add the unique word as its first value. If the anagram *is* already in `anagrams`, simply append the unique word to its corresponding anagram key in `anagrams`.
5. Write each anagram and its corresponding values found in the Brown Corpus to `anagrams_output.txt`.
