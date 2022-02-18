class EtchASketch:
  def __init__(self, turtle):
    self.turtle = turtle
    self.heading = 0

  def move_forward(self):
    self.turtle.forward(10)

  def move_backward(self):
    self.turtle.backward(10)

  def move_clockwise(self):
    self.heading -= 10
    self.turtle.setheading(self.heading)

  def move_counter_clockwise(self):
    self.heading += 10
    self.turtle.setheading(self.heading)

  def reset(self):
    self.turtle.reset()
    self.turtle.home()