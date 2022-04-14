from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from gameconstants import SCREEN_SIZE, FOOD_COLLISION_SIZE, NEGATIVE_BOUNDARY, POSITIVE_BOUNDARY, TAIL_COLLISION_SIZE
import time

screen = Screen()
screen.setup(width=SCREEN_SIZE, height=SCREEN_SIZE)
screen.bgcolor("black")
screen.title("SnakeGame")
screen.tracer(0) # turns off turtle animation

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_running = True
while game_running:
  screen.update()
  time.sleep(0.1)
  snake.move()

  # Detecting food collision = within X pixels
  if snake.head.distance(food) < FOOD_COLLISION_SIZE:
    food.refresh()
    snake.grow()
    scoreboard.increment_score()

  # Detecting wall collision
  if snake.head.xcor() > POSITIVE_BOUNDARY or snake.head.xcor() < NEGATIVE_BOUNDARY or snake.head.ycor() > POSITIVE_BOUNDARY or snake.head.ycor() < NEGATIVE_BOUNDARY:
    game_running = False
    scoreboard.game_over()

  # Detecting tail collision
  # using list slicing to check for every segment except the head
  for segment in snake.segments[1:]:
    if snake.head.distance(segment) < TAIL_COLLISION_SIZE:
      game_running = False
      scoreboard.game_over()

screen.exitonclick()
