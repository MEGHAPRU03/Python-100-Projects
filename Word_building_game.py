import random
import enchant
from collections import Counter
import time

letters_pool = list('abcdefghijklmnopqrstuvwxyz')

# Load dictionaries
d1 = enchant.Dict("en_US")  # American English
d2 = enchant.Dict("en_GB")  # British English
d3 = enchant.Dict("en_CA")  # Canadian English
d4 = enchant.Dict("en_AU")  # Australian English

letters = [random.choice(letters_pool) for _ in range(9)]

print('*' * 20)
print("Welcome to the Word Building Game!!".center(50))
print('RULES'.center(50,'-'))
print('Use the given letters to form words.')
print('Each letter can be used only as many times as it appears.')
print('Words must be real dictionary words.')
print('Each word counts only once.')
print('You have 60 seconds to enter as many words as possible.')
print('*' * 50)

print("Your letters are:", letters)
print("Start typing your words!\n")

valid_words = set()
time_limit = 60
start_time = time.time()

while True:
    elapsed = time.time() - start_time
    if elapsed >= time_limit:
        print("\nTime's up!")
        break

    word = input("Enter a word: ").lower()

    # Check if letters are used correctly
    word_count = Counter(word)
    letters_count = Counter(letters)
    valid_letters = True
    for char in word_count:
        if char not in letters_count:
            print(f"'{char}' is not in the given letters.")
            valid_letters = False
            break
        if word_count[char] > letters_count[char]:
            print(f"'{char}' is used too many times.")
            valid_letters = False
            break
    if not valid_letters:
        continue

    # Check dictionary
    if d1.check(word) or d2.check(word) or d3.check(word) or d4.check(word):
        if word in valid_words:
            print("You already entered this word!")
        else:
            valid_words.add(word)
            print("Valid word!")
    else:
        print("Invalid word (not found in dictionary)")


print('\n' + '-'*50)
print("Game Summary".center(50,'-'))
print("Your valid unique words:", valid_words)
print("Total valid unique words:", len(valid_words))
print("Total Score =", len(valid_words))
print('-'*50)


#1. import random
# 
# The random module is part of Python’s standard library.
# It is used to generate random numbers and make random selections.
# In games, it helps to create unpredictable outcomes.
# You can use random.choice() to select a random item from a list.
# random.randint(a, b) returns a random integer between a and b.
# random.shuffle() can shuffle elements in a list randomly.
# Randomness adds fairness and unpredictability to games.
# It is lightweight and easy to use without extra installation.
# In our game, it selects 7 random letters from the alphabet.
# It ensures each playthrough is unique and different every time.
# 
# 2. import enchant
# 
# enchant is a Python library for spellchecking.
# It allows us to verify whether a word exists in a dictionary.
# Supports multiple dictionaries like US, UK, Canadian, and Australian English.
# The Dict() object is used to create a dictionary instance.
# check(word) method returns True if the word is valid.
# Useful in word games to prevent players from entering gibberish.
# Can be used for autocorrect, grammar checks, and educational apps.
# Requires installation via pip install pyenchant.
# It helps maintain real-world correctness in word-building games.
# Ensures that only meaningful words are counted for scoring.
# 
# 3. from collections import Counter
# 
# collections is a standard Python module with useful data structures.
# Counter is a subclass of dictionary in the collections module.
# It counts the frequency of each element in a list or string.
# Useful for comparing how many times letters appear in a word.
# Helps validate that the user does not exceed letter limits.
# Counter(word) returns a dictionary-like object with letter counts.
# Supports arithmetic operations between counters for comparisons.
# Makes code cleaner compared to manually counting letters in loops.
# Provides methods like .most_common() to get frequent elements.
# Essential for checking valid word formation in our game.
# 
# 4. import time
# 
# The time module is part of Python’s standard library.
# It allows access to the system clock and time-related functions.
# time.time() returns the current time in seconds since epoch.
# Useful for tracking elapsed time in games or programs.
# Can implement countdown timers and time-limited challenges.
# time.sleep(seconds) pauses program execution for a given time.
# Helps make interactive programs more engaging.
# Used in our game to implement a 60-second play limit.
# Allows real-time game events without blocking user input.
# Essential for adding timing mechanics to interactive Python projects.

