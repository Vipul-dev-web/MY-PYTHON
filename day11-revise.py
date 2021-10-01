import random
import os


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

print("BLACKJACK")

user_cards = []
com_cards = []
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def choose_cards():
    random_num = int(random.random() * len(cards))
    return cards[random_num]


def deal_cards(list):
    for i in range(2):
        list.append(choose_cards())


deal_cards(user_cards)
deal_cards(com_cards)
print(user_cards, com_cards)
# user_cards = [11, 10]


def sum_cards(list):
    sum = 0
    for card in list:
        sum += card
    return sum


ask = ""


def check_blackjack():
    if sum_cards(user_cards) == 21:
        return "Yes there is a blackjack for the user. You Win!"
    elif sum_cards(com_cards) == 21:
        return "Yes there is a blackjack for the house. You Lose!"
    else:
        print("No there is not any blackjack")
        if sum_cards(user_cards) > 21:
            if 11 in user_cards:
                user_cards.remove(11).append(1)
                if sum_cards(user_cards) > 21:
                    print("You Lose!")
                else:
                    ask = input(
                        "Do you want to get another card? Type yes or no: \n")
                    if ask == "yes":
                        user_cards.append(choose_cards())
                        sum_cards(user_cards)
                        check_blackjack()
                    else:
                        while sum_cards(com_cards) < 17:
                            com_cards.append(choose_cards())
                            if sum_cards(com_cards) > 21:
                                print("You win!")
                            else:
                                if sum_cards(com_cards) > sum_cards(user_cards):
                                    print("You lose!")
                                elif sum_cards(com_cards) < sum_cards(user_cards):
                                    print("You win!")
                                elif sum_cards(com_cards) == sum_cards(user_cards):
                                    print("It's a draw'")
            else:
                print("No there is not any blackjack")
        else:
            ask = input(
                "Do you want to get another card? Type yes or no: \n")
            if ask == "yes":
                user_cards.append(choose_cards())
                sum_cards(user_cards)
                check_blackjack()
            else:
                while sum_cards(com_cards) < 17:
                    com_cards.append(choose_cards())
                    if sum_cards(com_cards) > 21:
                        print("You win!")
                    if sum_cards(com_cards) > sum_cards(user_cards):
                        print("You lose!")
                    elif sum_cards(com_cards) < sum_cards(user_cards):
                        print("You win!")
                    elif sum_cards(com_cards) == sum_cards(user_cards):
                        print("It's a draw'")


print(sum_cards(user_cards), sum_cards(com_cards))
check_blackjack()
