from turtle import Turtle, Screen
from etch_sketch import EtchASketch

screen = Screen()

etch_a_sketch = EtchASketch(Turtle())

screen.listen()
screen.onkey(key="w", fun=etch_a_sketch.move_forward)
screen.onkey(key="s", fun=etch_a_sketch.move_backward)
screen.onkey(key="d", fun=etch_a_sketch.move_clockwise)
screen.onkey(key="a",fun=etch_a_sketch.move_counter_clockwise)
screen.onkey(key="c", fun=etch_a_sketch.reset)
screen.exitonclick()