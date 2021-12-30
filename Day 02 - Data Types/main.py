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
