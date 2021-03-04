from e_szekreny1 import *


class TurtleOOP:

    turtle = Turtle()
    screen = Screen()

    left = -screen.window_width() / 2
    right = screen.window_width() / 2
    top = screen.window_height() / 2
    bottom = -screen.window_height() / 2

    def __init__(self):
        self.turtle._delay(0)
        self.turtle.speed(0)
        self.turtle.penup()
        sz = Szekreny1(self.turtle)

        self.turtle.goto(self.left, self.bottom)
        sz.szekreny(5, 3)

        self.screen.mainloop()


t = TurtleOOP()

