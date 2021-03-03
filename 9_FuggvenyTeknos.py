from turtle import Turtle
from turtle import Screen
from math import *


class TurtleOOP:
    screen = Screen()
    turtle = Turtle()

    def square(self, a:int):

        drawing = self.turtle._drawing

        self.turtle.penup()
        self.turtle.forward(a / 2)
        self.turtle.left(90)
        self.turtle.forward(a / 2)

        self.turtle.pendown()
        for i in range(4):
            self.turtle.left(90)
            self.turtle.forward(a)

        self.turtle.penup()
        self.turtle.back(a / 2)
        self.turtle.right(90)
        self.turtle.back(a / 2)

        self.turtle._drawing = drawing

    def __init__(self):
        # turtle._delay(0)
        self.turtle.speed(1)
        self.turtle.left(23)
        self.square(128)
        self.turtle.left(23)
        self.square(128)
        self.screen.mainloop()


TurtleOOP()