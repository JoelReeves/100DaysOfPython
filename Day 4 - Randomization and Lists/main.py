import random

# random int between 1-10 (including both numbers)
random_int = random.randint(1, 10)
print(random_int)

# random float between 0.0 and 1.0 (not including 1.0)
random_float = random.random()
print(random_float)

# random float between 0 and 10
print(random_float * 5)

# Heads or Tails
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

coin_flip = random.randint(0, 1)
if coin_flip == 1:
    print("Heads")
else:
    print("Tails")

# Lists
states = ["Oregon", "Hawaii", "California"]
print(states)
print(f"There are {len(states)} states")
print(f"The first state is {states[0]}")
print(f"The last state is {states[-1]}")
print(f"The second to the last state is {states[-2]}")

states.append("Georgia") # adds to end of list
print(states)

first_two_states = states[0:2]
print(first_two_states)

# Banker Roulette
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

random_index = random.randint(0, len(names) - 1)
print(f"{names[random_index]} is going to buy the meal today!")

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

# Use the syntax list[n] to access the nth element of list.
# If the nth of list is another list, use list[n][k] to access the kth element of list[n].
print(dirty_dozen[1][1]) # Kale

# Treasure Map
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

horizontal = int(position[0])
vertical = int(position[1])

selected_row = map[vertical - 1]
selected_row[horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")

# Rock, Paper Scissors
random.seed(random.randint(0, 1000))
print("Welcome to Rock, Paper, Scissors")
print("Type 0 for ROCK, 1 for PAPER, or 2 for SCISSORS.")
rock = "ROCK"
paper = "PAPER"
scissors = "SCISSORS"
player_choice = int(input("What do you choose? "))

if player_choice < 0 or player_choice >= 3:
    print("You entered an invalid number. You lose!")
    quit()

computer_choice = random.randint(0, 2)

if player_choice == 0:
    print(f"You chose {rock}")
elif player_choice == 1:
    print(f"You chose {paper}")
elif player_choice == 2:
    print(f"You chose {scissors}")

if computer_choice == 0:
    print(f"Computer chose {rock}")
elif computer_choice == 1:
    print(f"Computer chose {paper}")
else:
    print(f"Computer chose {scissors}")

if player_choice == computer_choice:
    print("It's a TIE")
elif player_choice == 0:
    if computer_choice == 2:
        print("Rock breaks scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif player_choice == 1:
    if computer_choice == 0:
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
else:
    if computer_choice == 1:
        print("Scissors cuts paper! You win!")
    else:
        print("Rock breaks scissors! You lose.")
