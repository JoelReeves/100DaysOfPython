from turtle import Turtle, Screen
from turtle_racing import TurtleRacer
import random

race_started = False

screen = Screen()
screen_width = 500
screen.setup(width=screen_width, height=400)

user_bet = ""

def is_bet_valid(bet):
    return bet == "red" or bet == "orange" or bet == "yellow" or bet == "green" or bet == "blue" or bet == "purple"

while not race_started:
  user_bet = screen.textinput(title="Place your bet", prompt="Which turtle will win? (red, orange, yellow, green, blue, purple)")
  user_bet = user_bet.lower()

  if not is_bet_valid(user_bet):
    print("Invalid bet! Please choose a valid color")
  else:
    race_started = True

    turtle_racers = [
      TurtleRacer(Turtle(shape="turtle"), "red", screen_width, 125),
      TurtleRacer(Turtle(shape="turtle"), "orange", screen_width, 75),
      TurtleRacer(Turtle(shape="turtle"), "yellow", screen_width, 25),
      TurtleRacer(Turtle(shape="turtle"), "green", screen_width, -25),
      TurtleRacer(Turtle(shape="turtle"), "blue", screen_width, -75),
      TurtleRacer(Turtle(shape="turtle"), "purple", screen_width, -125)
    ]

while race_started:
  for turtle in turtle_racers:
    if turtle.is_winner():
      race_started = False
      winner = turtle.pencolor()
      if winner == user_bet:
        print(f"You won! The {winner} turtle won!")
      else:
        print(f"You lost! The {winner} turtle is the winner!")

    random_speed = random.randint(0, 10)
    turtle.move(random_speed)

screen.exitonclick()