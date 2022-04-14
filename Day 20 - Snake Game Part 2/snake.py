from turtle import Turtle
from gameconstants import STARTING_POSITIONS, MOVE_DISTANCE, MOVE_UP, MOVE_DOWN, MOVE_LEFT, MOVE_RIGHT

class Snake:
    def __init__(self):
        self.segments = []

        for position in STARTING_POSITIONS:
            self.add_segment(position)

        self.head = self.segments[0]

    def move(self):
        # start = length of segments list, stop = 0, step = -1
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        # allowed going up if not moving down - no backwards movement
        if self.head.heading() != MOVE_DOWN:
            self.head.setheading(MOVE_UP)

    def down(self):
        # allowed going down if not moving up - no backwards movement
        if self.head.heading() != MOVE_UP:
            self.head.setheading(MOVE_DOWN)

    def left(self):
        # allowed going left if not moving right - no backwards movement
        if self.head.heading() != MOVE_RIGHT:
            self.head.setheading(MOVE_LEFT)

    def right(self):
        # allowed going right if not moving left - no backwards movement
        if self.head.heading() != MOVE_LEFT:
            self.head.setheading(MOVE_RIGHT)

    def add_segment(self, position):
        segment = Turtle("square")
        segment.penup()
        segment.color("white")
        segment.goto(position)
        self.segments.append(segment)

    def grow(self):
        # with lists, -1 is used to grab the last position
        last_position = self.segments[-1].position()
        self.add_segment(last_position)
