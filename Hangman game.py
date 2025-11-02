import random

print('-'*174)
print("🎯 Welcome to the Hangman Game!".center(175))
print('-'*174)

# Step 1: Word list
words = ['python', 'java', 'kotlin', 'javascript', 'hangman','javascript','system','snowflake','cloud','aws','gcp','amazon','redshift']
word = random.choice(words)

# Step 2: Setup
display = ['_' for _ in word]
lives = 6
guessed_letters = []

# Step 3: Main Game Loop
while True:
    print("\nWord:", " ".join(display))
    print(f"Lives left: {lives}")

    guess = input("Guess a letter: ").lower()

    # Check for invalid input
    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter a single alphabetic character.")
        continue

    # Already guessed letter
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue
    guessed_letters.append(guess)

    # Correct guess
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
        print("✅ Good guess!")
    else:
        lives -= 1
        print("❌ Wrong guess!")

    # Check win condition
    if "_" not in display:
        print("\n🎉 You win! The word was:", word)
        break

    # Check lose condition
    if lives == 0:
        print("\n💀 You lost! The word was:", word)
        break
