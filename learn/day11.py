# MAKING OF BLACKJACK
import os
import random


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


print("""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
      )

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def card_choice():
    random_num = int(random.random() * len(cards))
    card = cards[random_num]
    return card


def play():
    user_cards = []
    computer_cards = []

    # user_cards.append(card_choice())
    # user_cards.append(card_choice())
    # computer_cards.append(card_choice())
    # computer_cards.append(card_choice())
    # print(user_cards, computer_cards)

    for number in range(2):
        user_cards.append(card_choice())
        computer_cards.append(card_choice())
    print(user_cards, computer_cards)

    # user_cards = [11, 10]

    def calculate_score(list):
        sum = 0
        for num in range(len(list)):
            sum += int(list[num])
        # 0 will represent a blackjack in our game.
        if sum == 21 and len(list) == 2:
            return 0
        elif 11 in list and sum > 21:
            list.remove(list.index(11))
            list.append(1)
            sum = 0
            for i in range(len(list)):
                sum += int(list[i])
            return sum
        else:
            return sum

    print(calculate_score(user_cards))

    while calculate_score(computer_cards) < 17:
        computer_cards.append(card_choice())

    if calculate_score(user_cards) == 21 or calculate_score(computer_cards) == 21:
        print("Game Ends")
    elif calculate_score(user_cards) > 21:
        print("Game Ends")
    elif calculate_score(computer_cards) <= 21 and calculate_score(user_cards) <= 21 and calculate_score(computer_cards) == calculate_score(user_cards):
        print("IT's a DRAW")
    else:
        if input("Type yes to draw another card else type no: \n") == "yes":
            user_cards.append(card_choice())
            calculate_score(user_cards)
        else:
            print("Game Ends")


play()
again = input("Type yes to play again else type no")

while again == "yes":
    play()
