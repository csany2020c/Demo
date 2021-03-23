from turtle import *
from math import *


class TurtleOOP:

    turtle = Turtle()
    screen = Screen()
    screen.setup(height=680)

    left: int = int(-screen.window_width() / 2)
    right: int = int(screen.window_width() / 2)
    top: int = int(screen.window_height() / 2)
    bottom: int = int(-screen.window_height() / 2)

    def __init__(self):
        self.turtle._delay(0)
        self.turtle.speed(0)

        for x in range(-300, 300, 50):
            for y in range(-300, 300, 50):
                self.turtle.goto(x,y)
                for f in range(5):
                    for i in range(36):
                        self.turtle.forward((f + 1))
                        self.turtle.left(10)


        self.screen.mainloop()


t = TurtleOOP()

