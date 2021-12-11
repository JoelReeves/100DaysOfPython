print("Hello World")
print("Hello\nHow are you this morning?")

# string concatenation
print("Hello" + ", Joel")

# f-string (string interpolation)
name = "Jeanette Reeves"
print(f"Good morning, {name}. I love you so much!")

# getting user input
name = input("What is your name? ")
print("Hello, " + name)

# Day 1 Project: Band Name Generator
print("Hello! Welcome to the Band Name Generator")
city = input("What is the name of the city you grew up in?\n")
pet = input("What is the name of a pet?\n")
print("Your band name is " + city + " " + pet)

# Data Types

# Strings
my_first_name = "Joel"
print(my_first_name + " has " + str(len(my_first_name)) + " characters")
print("The first character of " + my_first_name + " is " + my_first_name[0])
print("The last character of " + my_first_name + " is " + my_first_name[len(my_first_name) - 1])

# Integers
my_age = 21

# Float
pi = 3.14159

# Boolean
is_true = True
is_false = False

# type checking variable - using type keywords
print(my_first_name + " is a " + str(type(my_first_name)))

# calculating BMI = weight / height ** 2
height = input("enter your height in meters: ")
weight = input("enter your weight in kg: ")
bmi = int(weight) / float(height) ** 2
print("Your BMI is " + str(int(bmi)))

# rounding numbers
value = 8 / 3
print("8 / 3 rounded is " + str(round(value)))
print("8 / 3 rounded to 2 decimal places is " + str(round(value, 2)))

# floor division
floor_div_value = 16 // 5 # is 3.2
print("16 // 5 is " + str(floor_div_value))

# Day 2 Project: Tip Calculator
print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people_split = int(input("How many people should split the bill? "))
total_with_tip = (tip / 100 * total_bill) + total_bill
answer = round(total_with_tip / people_split, 2)
print(f"Each person should pay: ${answer}")

# Control Flow and Logical Operators

height = int(input("What is your height in cm? "))
if height > 120:
    print("You can ride the rollercoaster!")
    # nested if/else
    age = int(input("How old are you? "))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you're not tall enough to ride!")


# BMI 2.0
# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.

"Your BMI is 18, you are underweight."
"Your BMI is 22, you have a normal weight."
"Your BMI is 28, you are slightly overweight."
"Your BMI is 33, you are obese."
"Your BMI is 40, you are clinically obese."

height = input("enter your height in meters: ")
weight = input("enter your weight in kg: ")
bmi = round(int(weight) / float(height) ** 2)
message = ""
if bmi < 18.5:
    message = "you are underweight."
elif bmi > 18.5 and bmi < 25:
    message = "you have a normal weight."
elif bmi > 25 and bmi < 30:
    message = "you are slightly overweight."
elif bmi > 30 and bmi < 35:
    message = "you are obese."
else:
    message = " you are clinically obese."

print(f"Your BMI is {str(int(bmi))}, {message}")

# Leap Year
year = int(input("Which year do you want to check? "))

is_leap_year = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
if is_leap_year:
    print("Leap year.")
else:
    print("Not leap year.")

# Python Pizza Program - based on a user's order, work out their final bill.
# - Small Pizza: $15
# - Medium Pizza: $20
# - Large Pizza: $25
# - Pepperoni for Small Pizza: +$2
# - Pepperoni for Medium or Large Pizza: +$3
# - Extra cheese for any size pizza: + $1
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L? ")
add_pepperoni = input("Do you want pepperoni? Y or N? ")
extra_cheese = input("Do you want extra cheese? Y or N? ")

final_bill = 0

if size == "S":
    final_bill += 15
    if add_pepperoni == "Y":
        final_bill += 2
elif size == "M":
    final_bill += 20
    if add_pepperoni == "Y":
        final_bill += 3
else:
    final_bill += 25
    if add_pepperoni == "Y":
        final_bill += 3

if extra_cheese == "Y":
    final_bill += 1

print(f"Your final bill is: ${final_bill}.")

# Logical operators
age = 15
logical_not = False
print(f"Are you a teenager? {age >= 13 and age <= 17}") #using and
print(f"Are you a teenager? {age >= 13 or age <= 17}") #using or
print(f"Opposite of False is {not logical_not}") #using not

# Love Calculator - calculating the love score between two people:
# Take both people's names and check for the number of times the letters in the word TRUE occurs.
# Then check for the number of times the letters in the word LOVE occurs.
# Then combine these numbers to make a 2 digit number.
#
# For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is **x**, you go together like coke and mentos."
#
# For Love Scores between 40 and 50, the message should be:
# "Your score is **y**, you are alright together."
#
# Otherwise, the message will just be their score. e.g.:
# "Your score is **z**."
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_names = name1.lower() + name2.lower()

t_count = combined_names.count("t")
r_count = combined_names.count("r")
u_count = combined_names.count("u")
e_count = combined_names.count("e")

l_count = combined_names.count("l")
o_count = combined_names.count("o")
v_count = combined_names.count("v")

true_count = t_count + r_count + u_count + e_count
love_count = l_count + o_count + v_count + e_count
love_score = int(str(true_count) + str(love_count))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")

# Treasure Island
print("Welcome to Treasure Island!\nYour mission is to find the treasure.")
first_action = input("You arrive at a path. Do you want to go LEFT or RIGHT? Left or Right? ").lower()
if first_action == "left":
    second_action = input("You arrive at a lake. Do you SWIM or GO AROUND? Swim or Around? ").lower()
    if second_action == "around":
        print("You arrive at different colored doors (Red, Blue, Green).")
        third_action = input("Which door do you want to go through? Red, Blue, Green? ").lower()
        if third_action == "red":
            print("You were burned by fire! Game Over!")
        elif third_action == "blue":
            print("You were eaten by zombies! Game Over!")
        else:
            print("You got the treasure and escaped the island. You WIN!!!")
    else:
        print("You were stung by a jellyfish! Game Over!")
else:
    print("Oops. You fell into a hole. Game Over!")

