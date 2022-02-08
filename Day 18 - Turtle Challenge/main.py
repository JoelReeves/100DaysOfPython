from turtle import Turtle, Screen
import colorgram
import random

# Turtle documentation https://docs.python.org/3/library/turtle.html#module-turtle

tim = Turtle()
screen = Screen()
screen.colormode(255)

# def random_color():
#   r = random.randint(0, 255)
#   g = random.randint(0, 255)
#   b = random.randint(0, 255)
#
#   return (r, g, b)

# for _ in range(4):
#   tim.forward(75)
#   tim.right(90)

# for _ in range(5):
#   tim.forward(15)
#   tim.penup()
#   tim.forward(15)
#   tim.pendown()

# Drawing different shapes (3 - 10 sided shapes)
# sides = 3
# angle = 0
# colors = ['pink', 'blue', 'yellow', 'black', 'orange', 'purple', 'red', 'gray']

# def draw_shape(sides):
#   tim.color(random.choice(colors))
#   angle = 360 / sides
#   for _ in range(sides):
#       tim.forward(100)
#       tim.right(angle)

# for sides in range(3, 11):
#   draw_shape(sides)

# Generating random walk
# directions = [0, 90, 180, 270]
# tim.speed("fastest")
# tim.pensize(15)

# for _ in range(1000):
#   tim.color(random_color())
#   tim.setheading(random.choice(directions))
#   tim.forward(20)

# Drawing spirograph
# tim.pensize(2)
# tim.speed("fastest")
#
# for i in range(5000):
#   tim.color(random_color())
#   tim.circle(100)
#   tim.left(10)

# Using Colorgram package to extract colors from image
# colors = colorgram.extract('hirst_spots.jpeg', 20)
# extracted_colors = []
#
# for color in colors:
#     print(color)
#     color_rgb = (color.rgb.r, color.rgb.g, color.rgb.b)
#     extracted_colors.append(color_rgb)
#
# print(extracted_colors)

color_list = [(250, 246, 243), (248, 245, 246), (211, 154, 98), (53, 107, 131), (242, 249, 246), (235, 240, 244), (177, 78, 33), (198, 142, 35), (116, 155, 171), (124, 79, 98)]

x_position = -150.0
y_position = 0.0

tim.hideturtle()
tim.speed("fastest")
tim.penup()
tim.setx(x_position)

for _ in range(10):
  for color in color_list:
      tim.dot(20, random.choice(color_list))
      tim.penup()
      tim.forward(40)
      tim.pendown()

  tim.penup()
  tim.setx(x_position)
  y_position -= 30.0
  tim.sety(y_position)

screen.exitonclick()
