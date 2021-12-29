# Functions with Outputs

def format_name(first_name, last_name):
    if first_name == "" or last_name == "":
        return "Please provide a valid first and last name"

    title_first_name = first_name.title()
    title_last_name = last_name.title()

    return f"Formatted name: {title_first_name} {title_last_name}"

first_name = input("Input a first name: ")
last_name = input("Input a last name: ")
formatted_name = format_name(first_name, last_name)
print(formatted_name)

# Days in Month
def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    if month < 1 or month > 12:
        return "Invalid month"

    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_leap(year):
        return 29

    return month_days[month - 1]


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

# Calculator
from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(logo)

    should_calculate = True
    number1 = float(input("What is the first number? "))

    for operation in operations:
        print(operation)

    while should_calculate:
        symbol = input("Pick an operation: ")
        number2 = float(input("What is the next number? "))
        math_operation = operations[symbol]
        answer = math_operation(number1, number2)

        print(f"{number1} {symbol} {number2} = {answer}")

        continue_calculation = input(f"Continue calculating with {answer}? Type 'y' to continue or 'n' to start a new calculation: ").lower()
        if continue_calculation == "y":
            number1 = answer
        else:
            should_calculate = False
            calculator()

calculator()