import random
import os


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

print(logo)

# 11 is the Ace.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    card = random.choice(cards)
    return card


def compare_score(user_score, computer_score):
    if user_score == computer_score:
        return "It's a Draw ¯\_(ツ)_/¯"
    elif user_score == 0:
        return "Win with a Blackjack (⌐■_■)"
    elif computer_score == 0:
        return "Lose, Opponent has a Blackjack 😨"
    elif user_score > 21:
        return "You went over 21, Your lose😥"
    elif computer_score > 21:
        return "Opponent went over. You win 😎"
    elif user_score > computer_score:
        return "You Win (づ￣ 3￣)づ"
    else:
        return "You Lose 😭"


def give_cards(list):
    for i in range(2):
        list.append(deal_card())


def calculate_score(list):
    score = 0
    for i in range(len(list)):
        score += list[i]
    # Check Blackjack
    if len(list) == 2 and score == 21:
        return 0
    if 11 in list and score > 21:
        list.remove(11)
        list.append(1)
    return score


def start_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    give_cards(user_cards)
    give_cards(computer_cards)

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"\n>>>>>>>>Your Cards: {user_cards} and score: {user_score}",
              f"\n>>>>>>>>Computer's First Card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            ask_for_card = input(
                "Do you want to draw another card if yes Type \'yes\' otherwise type \'no\':\n")
            if ask_for_card == 'yes':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"   Your Final Hand: {user_cards} and score: {user_score}")
    print(
        f"   House's Final Hand: {computer_cards} and score: {computer_score}")
    print(compare_score(user_score, computer_score))


while input('Do you want to play a game of Blackjack? "yes" or "no"') == 'yes':
    clearConsole()
    print(logo)
    start_game()
