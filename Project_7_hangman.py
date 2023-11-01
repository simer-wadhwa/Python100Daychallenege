# Step 2

import random
from extra_files import hangman_words,hangman_art


print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)

# Testing code
#print(f'Pssst, the solution is {chosen_word}.')

# TODO-1: - Create an empty List called display.
# For each letter in the chosen_word, add a "_" to 'display'.
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
guess_list = ["_" for i in range(len(chosen_word))]
print(guess_list)

# TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
lives = 6

while "_" in guess_list and lives > 0:
    guess = input("Guess a letter: ").lower()

    temp = False
    for index, letter in enumerate(chosen_word):
        if letter == guess:
            guess_list[index] = guess
            temp = True

    if not temp:
        lives -= 1
        print(lives)

    print( f" {''.join(guess_list)}" )
    print(hangman_art.stages[lives])

if lives == 0 and "_" in guess_list:
    print("You lost")
else:
    print("You Win")

# TODO-2: - Loop through each position in the chosen_word;
# If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].


# TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
# Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
