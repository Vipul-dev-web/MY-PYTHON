# import day3

# print(day3.myname)

import random

# # random_integer = random.randint(1, 100)
# # print(random_integer)

# random_float = random.random()
# # print(random_float)

# new_num = int(random_float * 5 + 1)
# print(new_num)

# random_num = int(random.random() * 2 + 1)

# if random_num == 1:
#     print("It's Heads")
# if random_num == 2:
#     print("It's Tales'")

# fruits = ["Mango", "Apple", "Banana", "Orange",
#           "Papaya", "Pear", "Cherry", "Grape", "Kiwi"]

# num_of_fruits = len(fruits)
# print(num_of_fruits, len(fruits[7]))

# Random Name Generator

# print("Welcome to the Python random name generator")
# names_str = input(
#     "Write the names of all the persons whom you want to choose the name\nBe careful when typing the names, separate the names by a comma and a space.\n")
# names_list = names_str.split(", ")

# random_num = random.randint(0, len(names_list) - 1)

# print(f"{names_list[random_num]} is going to buy the meal today!")

# Treasure Mapper

# row1 = ["⬜️", "⬜️", "⬜️"]
# row2 = ["⬜️", "⬜️", "⬜️"]
# row3 = ["⬜️", "⬜️", "⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")

# print("These are the locations where you can map the treasure")
# position = input("Enter the position of your choice and it will be marked\n")

# x = int(position[0])
# y = int(position[1])

# # if x == 1 and y == 1:
# #     row1[0] = "X"
# # elif x == 1 and y == 2:
# #     row2[0] = "X"
# # elif x == 1 and y == 3:
# #     row3[0] = "X"
# # elif x == 2 and y == 1:
# #     row1[1] = "X"
# # elif x == 2 and y == 2:
# #     row2[1] = "X"
# # elif x == 2 and y == 3:
# #     row3[1] = "X"
# # elif x == 3 and y == 1:
# #     row1[2] = "X"
# # elif x == 3 and y == 2:
# #     row2[2] = "X"
# # elif x == 3 and y == 3:
# #     row3[2] = "X"

# map[y - 1][x - 1] = "X"

# print(f"{row1}\n{row2}\n{row3}")


# Rock, paper and scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

my_list = [rock, paper, scissors]

your_input = int(input(
    "Enter your choice i.e. number associated with ur choice, rock(0), paper(1) or scissors(2): \n"))

if your_input >= 3:
    print("You Lost!, because you have entered invalid number")
else:
    user_input = my_list[your_input]
    com_input = my_list[random.randint(0, len(my_list) - 1)]
    if user_input == com_input:
        print("It's a Draw")
    elif user_input == rock and com_input == my_list[2]:
        print(f"you chose {user_input}\n computer chose {com_input}")
        print("Hey, you won 🎉")
    elif user_input == paper and com_input == my_list[0]:
        print(f"you chose {user_input}\n computer chose {com_input}")
        print("Hey, you won 🎉")
    elif user_input == scissors and com_input == my_list[1]:
        print(f"you chose {user_input}\n computer chose {com_input}")
        print("Hey, you won 🎉")
    else:
        print(f"you chose {user_input}\n computer chose {com_input}")
        print("Aaah, you lost 😢")
