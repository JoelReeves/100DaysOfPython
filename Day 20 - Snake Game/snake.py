from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
MOVE_UP = 90
MOVE_DOWN = 270
MOVE_LEFT = 180
MOVE_RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []

        for position in STARTING_POSITIONS:
            segment = Turtle("square")
            segment.penup()
            segment.color("white")
            segment.goto(position)
            self.segments.append(segment)

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
