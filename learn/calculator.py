import os


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def addition(n1, n2):
    return n1 + n2


def subtraction(n1, n2):
    return n1 - n2


def multiplication(n1, n2):
    return n1 * n2


def division(n1, n2):
    return n1 / n2


operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division,
}

num1 = float(input("Enter the first number: \n"))
should_run = True


def start_calc():
    global num1
    for char in operations:
        print(f"\'{char}\'")
    operator = input("Enter the symbol of operation\n")
    num2 = float(input("Enter the second number: \n"))
    result = operations[operator](num1, num2)
    clearConsole()
    num1 = result
    print(f"The result of the opeartion between {num1} & {num2} is {result}")


while should_run:
    start_calc()
    stop = input("TO STOP CALCULATOR TYPE \"STOP\" otherwise hit enter")
    if stop == "STOP":
        should_run = False
