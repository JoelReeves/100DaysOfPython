from turtle import Turtle
import random
from gameconstants import FOOD_SIZE, NEGATIVE_BOUNDARY, POSITIVE_BOUNDARY

class Food(Turtle):

    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=FOOD_SIZE, stretch_wid=FOOD_SIZE)
        self.color("blue")
        self.speed("fastest")
        random_x = random.randint(NEGATIVE_BOUNDARY, POSITIVE_BOUNDARY)
        random_y = random.randint(NEGATIVE_BOUNDARY, POSITIVE_BOUNDARY)
        self.goto(random_x, random_y)
        self.refresh()

    def refresh(self):
        random_x = random.randint(NEGATIVE_BOUNDARY, POSITIVE_BOUNDARY)
        random_y = random.randint(NEGATIVE_BOUNDARY, POSITIVE_BOUNDARY)
        self.goto(random_x, random_y)
