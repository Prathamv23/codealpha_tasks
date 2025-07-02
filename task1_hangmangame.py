import random

# List of words
word_list = ["apple", "banana", "cherry", "grape", "mango"]

# Randomly select a word
chosen_word = random.choice(word_list)

# Display underscores for each letter
display_word = ["_"] * len(chosen_word)

# Store already guessed letters
letters_guessed = []

# Number of attempts
max_wrong_attempts = 6
wrong_attempts = 0

print("Welcome to Hangman!")
print("Try to guess the word.")
print("Word to guess:", " ".join(display_word))

# Continue until the word is guessed or player runs out of attempts
while wrong_attempts < max_wrong_attempts and "_" in display_word:
    guessed_letter = input("Enter a letter: ").lower()

    # Validate the input
    if len(guessed_letter) != 1 or not guessed_letter.isalpha():
        print("Please enter a single letter (a-z).")
        continue

    # Check if the letter was already guessed
    if guessed_letter in letters_guessed:
        print(f"You already guessed '{guessed_letter}'. Try another letter.")
        continue

    # Add the guessed letter to the list of guessed letters
    letters_guessed.append(guessed_letter)

    # If the guessed letter is in the chosen word
    if guessed_letter in chosen_word:
        print(f"Good job! The letter '{guessed_letter}' is in the word.")
        # Reveal all positions of the guessed letter in the display word
        for index, letter in enumerate(chosen_word):
            if letter == guessed_letter:
                display_word[index] = guessed_letter
    else:
        wrong_attempts += 1
        remaining_attempts = max_wrong_attempts - wrong_attempts
        print(f"Wrong guess. You have {remaining_attempts} attempts left.")

    # Show the current progress and guessed letters so far
    print("Current word:", " ".join(display_word))
    print("Letters guessed:", ", ".join(letters_guessed))
    print("-" * 40)

# Determine the final outcome
if "_" not in display_word:
    print(f"Congratulations! You guessed the word: '{chosen_word}'")
else:
    print(f"Game over! The word was: '{chosen_word}'.")
