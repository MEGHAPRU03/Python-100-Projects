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
