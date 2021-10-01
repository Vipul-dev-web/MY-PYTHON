# loops

# print("Let's calculate the average height of the students in the class")
# students_heights = input(
#     "Enter the height of each student separated by a space.\n")
# students_list = students_heights.split(" ")

# height_sum = 0
# for each_height in students_list:
#     height_sum += float(each_height)

# num_students = 0
# for each_student in students_list:
#     num_students += 1

# # avg_height = round(height_sum / len(students_list))
# avg_height = round(height_sum / num_students)
# print(f"The average height of the studentin the class is {avg_height}")

# High score finder

# print("Let's find the high score of the class")
# scores_str = input(
#     "Enter the score of each student in the class separated by a space: ")
# scores_list = scores_str.split(" ")

# high_score = int(scores_list[0])
# for score in scores_list:
#     if int(score) >= high_score:
#         high_score = int(score)

# print(f"The highest score in the class is: {high_score}")

# sumx = 0
# for number in range(2, 101, 2):
#     sumx += number
# print(sumx)

# new_sum = 0
# for number in range(1, 101):
#     if number % 2 == 0:
#         new_sum += number
# print(new_sum)


# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 != 0:
#         print("Fizz")
#     elif number % 5 == 0 and number % 3 != 0:
#         print("Buzz")
#     elif number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     else:
#         print(number)

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

letter_str = ""
for number in range(1, nr_letters + 1):
    letter_str += letters[int(random.random() * len(letters))]
# print(letter_str)

symbol_str = ""
for number in range(1, nr_symbols + 1):
    symbol_str += symbols[int(random.random() * len(symbols))]
# print(symbol_str)

numberx_str = ""
for number in range(1, nr_numbers + 1):
    numberx_str += numbers[int(random.random() * len(numbers))]
# print(numberx_str)

# easy string
easy_pass = letter_str + symbol_str + numberx_str
print(f"Your new password is: {easy_pass}")

# hard string
new_list = []
for number in range(0, len(easy_pass)):
    new_list.append(easy_pass[number])
print(new_list)

random.shuffle(new_list)
print(new_list)

hard_pass = ""
for char in new_list:
    hard_pass += char
print(hard_pass)


# hard_pass = ""
# for number in range(0, len(new_list)):
#     hard_pass += new_list[int(random.random() * len(new_list))]
# print(hard_pass)
