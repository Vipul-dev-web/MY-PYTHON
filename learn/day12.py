import random

print('Welcome to "Guess the number" game')
random_num = random.randint(1, 100)

print("There are three levels of game choose one of these (easy/medium/hard)")
level = input("Your choice of level: ").lower()


def assign_turns():
    num_of_turns = 0
    if level == "hard":
        num_of_turns = 5
    elif level == "medium":
        num_of_turns = 10
    elif level == "easy":
        num_of_turns = 15
    return num_of_turns


user_turns = assign_turns()
print(user_turns)

print(">>>>Your guess should be a number<<<<")

is_game_over = False
# For continuity of the game

guess = input("Enter your guess: ")

