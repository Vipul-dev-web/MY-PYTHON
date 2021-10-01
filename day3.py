# print("Welcome to code-coster")
# height = int(input("Enter the height in cms:\n"))
# if height >= 120:
#     print("U can ride the python code-codster")
# else:
#     print("Sorry, you can't ride the python code-codster'")

# odd-even check

# print("Enter the integer of your choice")
# num = int(input("Enter here: "))

# if num % 2 == 0:
#     print(f"{num}, the number of your choice is even")
# else:
#     print(f"{num}, the number of your choice is odd")


# print("Welcome to the python code-codster")
# height = int(input("Enter your height in cms: "))
# if height >= 120:
#     print("You can ride the python code-codster")
#     print("To ride the code-codster you need a ticket, go to ticket window and get ur ticket")
#     age = int(input("Enter your age in years: "))
#     if age > 12:
#         print("you have to pay $16")
#     elif age >= 18:
#         print("as an adult u have to pay $20 to ride")
#     else:
#         print("u have to pay $12 to ride")
# else:
#     print("Sorry but you first have to grow taller in order to ride the python code-codster")


# BMI TRACker

# print("Welcome to python BMI calculator")

# weight = float(input("Enter your weight in Kg: \n"))
# height = float(input("Enter your height in m: \n"))
# bmi = weight / height ** 2
# bmi_format = "{:.2f}".format(bmi)
# # print(type(bmi_format))
# print(f"Your Bmi is {bmi_format}")

# if float(bmi_format) < 18.5:
#     print("You are underweight")
# elif float(bmi_format) <= 25:
#     print("You are normalweight")
# elif float(bmi_format) <= 30:
#     print("You are overweight")
# elif float(bmi_format) <= 35:
#     print("You are obese")
# else:
#     print("You are clinicially obese")

# print leap years

# if year is divisible by 400 then is_leap_year
# else if year is divisible by 100 then not_leap_year
# else if year is divisible by 4 then is_leap_year
# else not_leap_year

# print("Welcome to the leap year checker")
# year = int(input("Enter the year of your choice like 2001, 1989 or anyyear\n"))
# print(f"The year you have entered is {year}")

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("The year is a leap year")
#         else:
#             print("The year is not a leap year")
#     else:
#         print("The year is not a leap year")
# else:
#     print("The year is not a leap year")4

# =================================================================================================
# print("Welcome to the roller-coster ride")
# age = float(input("Enter your age\n"))
# height = float(input("Enter your height \n"))
# bill = 0

# if height > 120:
#     print("You are allowed to take the ride")
#     if age <= 12:
#         bill = 12
#         print(f"Please pay ${bill} for the child-ticket")
#     elif age <= 18:
#         bill = 16
#         print(f"Please pay ${bill} for the youth-ticket")
#     else:
#         bill = 20
#         print(f"Please pay ${bill} for the adult-ticket")

#     print("Do u want photos?")
#     response = input("Yes or No \n")
#     if response == "Yes":
#         bill += 3

#     print(f"Your total bill is ${bill}")
# else:
#     print("You are not allowed to take the ride, grow taller to take the ride")


# =============================================================================
# pixxa delivery method

# print("Welcome to Python Pizza Point")
# size = input("What size pizza do you want? S(small), M(medium) or L(large)\n")
# add_pepperoni = input("Do you want pepperoni? Y or N\n")
# add_extra_cheese = input("Do you want extra cheese? Y or N\n")
# bill = 0

# if size == "S":
#     bill += 15
#     if add_pepperoni == "Y":
#         bill += 2
#     if add_extra_cheese == "Y":
#         bill += 1
#     print(f"This is your final bill and you have to Pay ${bill}")

# elif size == "M":
#     bill += 20
#     if add_pepperoni == "Y":
#         bill += 3
#     if add_extra_cheese == "Y":
#         bill += 1
#     print(f"This is your final bill and you have to Pay ${bill}")

# elif size == "L":
#     bill += 25
#     if add_pepperoni == "Y":
#         bill += 3
#     if add_extra_cheese == "Y":
#         bill += 1
#     print(f"This is your final bill and you have to Pay ${bill}")

# else:
#     print("Wrong input")

"""
print("Welcome to the Python Love Calculator")
your_name = input("Please enter your name\n")
their_name = input("Please enter their name\n")
print("Let's check the \"True Love\"")

num_t = your_name.lower().count("t") + their_name.lower().count("t")
num_r = your_name.lower().count("r") + their_name.lower().count("r")
num_u = your_name.lower().count("u") + their_name.lower().count("u")
num_e = your_name.lower().count("e") + their_name.lower().count("e")
num_l = your_name.lower().count("l") + their_name.lower().count("l")
num_o = your_name.lower().count("o") + their_name.lower().count("o")
num_v = your_name.lower().count("v") + their_name.lower().count("v")

sum_true = num_t + num_r + num_u + num_e
sum_love = num_l + num_o + num_v + num_e

true_love_num = str(sum_true) + str(sum_love)
print(f"Your \"True Love\" score is {true_love_num}%")

if (int(true_love_num) < 10 or int(true_love_num) > 90):
    print(
        f"\"Your score is {true_love_num}%, you go together like coke and mentos.\"")
elif (int(true_love_num) > 40 and int(true_love_num) < 50):
    print(f"\"Your score is {true_love_num}%, you are alright together.\"")
else:
    print(f"\"Your score is {true_love_num}%\"")
"""
myname = "Vipul"


print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
way = input("You are in the middle of the jungle and there are two ways to go ahead and you have to choose one of them, so which way do you want to go?\nLeft or Right\n")

if way == 'Left':
    print("You have made it to the right way")
    at_river = input(
        "You have reached to next level and there is a river in your way, do u want to wait for the boat or do u want to cross the river by swimming? Wait or Swim\n")
    if at_river == "Wait":
        print("Waiting was worth, u have made it to the final level")
        final = input("Now you have finally reached the castle and there are three doors and treasure is behind one of these doors but choose carefully which door u want to open, one wrong door and u will be done, Red, Yellow or Blue\n")
        if final == "Yellow":
            print("Congratulations, You have finally made it to the treasure🎉")
        elif final == "Red":
            print("Aaaaaaah, you have fallen into lava, game over 😢")
        elif final == "Blue":
            print("Beast killed you, sorry but you lost 😢")
        else:
            print("Game Over")
    else:
        print("Corocodiles ate you alive, game over 😢")
else:
    print("You became a dinner of a large snake, Game Over😢")
