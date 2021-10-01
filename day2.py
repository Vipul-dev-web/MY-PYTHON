# print("Enter a two digit number of your choice")
# user_input = str(input("Enter the number.\n"))
# user_input_digit_one = int(user_input[0])
# user_input_digit_two = int(user_input[1])
# digits_sum = user_input_digit_one + user_input_digit_two
# print("The sum of the digits of the number is " + str(digits_sum))


# print(3 * 3 + 3 / 3 - 3)
# print(3 * ((3 + 3) / 3) - 3)

# bmi calc

# height = input("Enter your height in m: ")
# weight = input("Enter your weight in kg: ")

# height_num = float(height)
# weight_num = float(weight)

# bmi = int(weight_num / height_num ** 2)
# print(input("Enter Your name") + ", Your BMI is: " + str(bmi) + ".")

# considering that there are only 365 days in year calculate no. of days weeks and months left until u become 90 years old.

# user_birth_year = int(input("Enter Your birth year\n"))
# curr_year = int(input("Enter Current year\n"))

# user_age = curr_year - user_birth_year
# years_left = 90 - user_age

# days_left = years_left * 365
# months_left = years_left * 12
# weeks_left = years_left * 52
# print(
#     f"Number of years left: {years_left}, Number of months left: {months_left}, Number of weeks left: {weeks_left}, Number of days left: {days_left}")

### TIP CALCULATOR ###

# print("Welcome to the python TIP calculator")
# amount = input("What was the total bill? Enter the bill amount: $")
# tip = input("What percentage tip would to you like to give?10, 12, or 15? ")
# people = input("Number of people you want to split the bill: ")
# tip_value = (float(amount) * float(tip)) / 100
# total_value = float(amount) + float(tip_value)
# each_person_contribution = total_value / float(people)
# each_person_contribution_format = "{:.2f}".format(each_person_contribution)
# print(f"Each person should pay ${each_person_contribution_format}")


# name = input("Enter your name\n")
# print(f"Hello, {name} we are going to calculate your BMI")
# weight = input("Enter your weight in Kg:\n")
# height = input("Enter your height in m:\n")
# Bmi = float(weight) / float(height) ** 2
# print(f"{name} your bmi is {Bmi}")
