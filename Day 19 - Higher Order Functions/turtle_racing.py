class TurtleRacer:
  def __init__(self, turtle, color, screen_width, ypos):
    self.turtle = turtle
    self.turtle.penup()
    self.turtle.color(color)
    self.screen_width = screen_width
    self.turtle.goto(x=20-(screen_width / 2), y=ypos)

  def move(self, forward):
    self.turtle.forward(forward)

  def is_winner(self):
    # turtle default width is 40
    return self.turtle.xcor() > self.screen_width - (40 / 2)

  def pencolor(self):
    return self.turtle.pencolor()