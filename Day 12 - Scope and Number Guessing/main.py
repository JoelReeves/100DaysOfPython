enemies = 1

def increase_enemies():
  # global enemies - global is used to modify global variables
  enemies = 2
  print(f"enemies inside function: {enemies}") # local scope enemies

increase_enemies()
print(f"enemies outside function: {enemies}")# global scope enemies

# Number Guessing Game
import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100 ")

answer = random.randint(1, 100)
# print(f"Debug testing. The number is {answer}")

rounds = 0
game_over = False

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == "easy":
  rounds = 10
else:
  rounds = 5

while game_over == False:
  print(f"You have {rounds} attempts to guess the number.")
  user_guess = int(input("Make a guess: "))

  if user_guess == answer:
    print(f"Correct! The answer was {user_guess}")
    game_over = True
  else:
    if user_guess < answer:
      print("Too low")
    else:
      print("Too high")

    rounds = rounds - 1
    if rounds < 1:
      print("You ran out of guesses, you lose")
      game_over = True
    else:
      print("Guess again")
