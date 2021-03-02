from turtle import Turtle
from turtle import Screen
from random import Random


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
        self.turtle.left(90)
        self.turtle.goto(0, -180)
        for i in range(7):
            for i in range(4):
                self.turtle.forward(40)
                self.turtle.right(90)
            self.turtle.forward(40)
        self.screen.mainloop()
t = TurtleOOP()
