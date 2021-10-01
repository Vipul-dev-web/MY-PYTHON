# Step 2

import random
import hangman_art
import hangman_words
import os


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


print(hangman_art.logo)

stages = hangman_art.stages
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []
for num in range(len(chosen_word)):
    display.append("_")
print(display)

lives = 6
end_of_game = False


def guess_letter():

    guess = input("Guess a letter: ").lower()

    clearConsole()

    if guess in display:
        print(f"The letter you entered is {guess} and it is already guessed")

    for num in range(len(chosen_word)):
        if chosen_word[num] == guess:
            display[num] = guess

    if guess not in chosen_word:
        global lives
        lives -= 1
        print(
            f"The letter you entered {guess} is not in the hidden word and now you have only {lives} lives left.")
        if lives == 0:
            global end_of_game
            end_of_game = True
            print("=/=/=/You Lose\=\=\=")


while not end_of_game:
    guess = guess_letter()
    print(' '.join(display))
    print(stages[lives])
    if "_" not in display:
        end_of_game = True
        print(display)
        print(f'"""""""""You Win"""""""""')
