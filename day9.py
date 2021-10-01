# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }
# # 🚨 Don't change the code above 👆

# # TODO-1: Create an empty dictionary called student_grades.
# student_grades = {}

# for item in student_scores:
#     student_grades[item] = student_scores[item]

# # Scores 91 - 100: Grade = "Outstanding"

# # Scores 81 - 90: Grade = "Exceeds Expectations"

# # Scores 71 - 80: Grade = "Acceptable"

# # Scores 70 or lower: Grade = "Fail"
# # TODO-2: Write your code below to add the grades to student_grades.👇
# for item in student_grades:
#     if student_grades[item] >= 91:
#         student_grades[item] = "Outstanding"
#     elif student_grades[item] >= 81:
#         student_grades[item] = "Exceeds Expectations"
#     elif student_grades[item] >= 71:
#         student_grades[item] = "Acceptable"
#     else:
#         student_grades[item] = "Fail"

# # 🚨 Don't change the code below 👇
# print(student_grades)
import os
# Silent bidding program
print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')

all_bidders = []


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def add_bidder():
    name_input = input("Enter your name.\n")
    bid_price = input("Enter your bid. \n$")
    bidder = {}
    bidder["name"] = name_input
    bidder["bid"] = bid_price
    all_bidders.append(bidder)


add_bidder()

more = input('More people to bid. "yes" or "no"')
while more == "yes":
    clearConsole()
    add_bidder()
    more = input('More people to bid. "yes" or "no"')

if more == "no":
    print(all_bidders)
    # for number in range(len(all_bidders)):
    #     print(all_bidders[number]["bid"])
    all_bids = []
    for bidder in all_bidders:
        all_bids.append(bidder["bid"])
    print(all_bids)

    max_bid = all_bids[0]
    for bid in all_bids:
        if int(bid) >= int(max_bid):
            max_bid = bid
    print(f"The highest bid is {max_bid}")
