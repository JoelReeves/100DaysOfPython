fruits = ["Apple", "Pear", "Peaches"]
for fruit in fruits:
    print(fruit)

# Average Height - calculating average height from a list of heights
# Don't use sum() or len() functions
student_heights = input("Input a list of student heights separated by a space: ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total = 0
counter = 0
for height in student_heights:
    total += height
    counter += 1

print(round(total / counter))

# High Score - calculating highest score from a list of scores
# Don't use max() function
student_scores = input("Input a list of student scores separated by a space: ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

high_score = student_scores[0]
for score in student_scores:
    if score > high_score:
        high_score = score

print(f"The highest score in the class is: {high_score}")

# For Loops and range() function - generating a range of numbers to loop through
for number in range(1, 10):
    print(number)

for number in range(1, 10, 2): # using step size to increment by that amount
    print(number)

total = 0
for number in range(1, 101):
    total += number
print(total)

# Adding even numbers - calculating the sum of all the even numbers from 1 to 100
total = 0
for number in range(1, 101):
    if number % 2 == 0:
        total += number

print(total)

# FizzBuzz
# Printing each number from 1 to 100
# When the number is divisible by 3, print "Fizz".
# When the number is divisible by 5, print "Buzz".`
# If the number is divisible by both 3 and 5 e.g. 15, print "FizzBuzz"
# Otherwise print the number
for number in range(1, 101):
    if number % 15 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

# Password Generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password? "))
nr_symbols = int(input(f"How many symbols would you like? "))
nr_numbers = int(input(f"How many numbers would you like? "))

password = ""
for letter in range(1, nr_letters + 1):
    password += random.choice(letters)

for symbol in range(1, nr_symbols + 1):
    password += random.choice(symbols)

for number in range(1, nr_numbers + 1):
    password += random.choice(numbers)

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
hard_password = "".join(random.sample(password, len(password)))
print(hard_password)

hard_password_alt = list(password)
random.shuffle(hard_password_alt)
print("".join(hard_password_alt))
