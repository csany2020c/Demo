from turtle import *
from math import *
from random import *


class TurtleOOP:

    turtle = Turtle()
    screen = Screen()
    screen.setup(height=680, width=1280)

    left: int = int(-screen.window_width() / 2)
    right: int = int(screen.window_width() / 2)
    top: int = int(screen.window_height() / 2)
    bottom: int = int(-screen.window_height() / 2)

    def bluerect(self, size: float = 20):
        self.turtle.fillcolor("lightblue")
        self.turtle.begin_fill()
        for i in range(4):
            self.turtle.forward(size)
            self.turtle.left(90)
        self.turtle.end_fill()


    def window(self, size: float = 20):
        x = self.turtle.xcor()
        y = self.turtle.ycor()
        rot = self.turtle.heading()
        self.turtle.forward(size / 2)
        self.turtle.left(90)
        self.turtle.forward(size / 2)
        for i in range(4):
            self.bluerect(size / 2)
            self.turtle.left(90)
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.setheading(rot)

    def house(self, size: float = 200):
        x = self.turtle.xcor()
        y = self.turtle.ycor()
        rot = self.turtle.heading()

        self.turtle.pendown()
        self.turtle.fillcolor(random(), random(), random())
        self.turtle.begin_fill()
        for i in range(4):
            self.turtle.forward(size)
            self.turtle.left(90)
        self.turtle.end_fill()

        self.turtle.penup()
        self.turtle.left(90)
        self.turtle.forward(size / 2)
        self.turtle.right(90)
        self.turtle.forward(size / 5)
        self.turtle.pendown()
        self.window(size / 4)
        self.turtle.penup()
        self.turtle.forward(size / 3)
        self.turtle.pendown()
        self.window(size / 4)

        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.setheading(rot)

        self.turtle.left(90)
        self.turtle.forward(size)
        self.turtle.left(90)
        self.turtle.forward(size/5)

        self.turtle.fillcolor("red")
        self.turtle.begin_fill()
        self.turtle.pendown()
        self.turtle.right(135)
        self.turtle.forward(size)
        self.turtle.right(90)
        self.turtle.forward(size)
        self.turtle.right(135)
        self.turtle.forward(size/5 * 2 + size)
        self.turtle.end_fill()

        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.setheading(rot)



    def __init__(self):
        self.turtle._delay(0)
        self.turtle.speed(0)
        self.turtle.penup()
        self.turtle.goto(self.left, self.bottom / 3)
        self.turtle.pendown()
        for i in range(8):
            self.turtle.pendown()
            self.turtle.left(random() * 40 - 20)
            self.turtle.forward(random() * 100 + 20)
            # self.turtle.setheading(0)
            self.house(100)
            self.turtle.forward(100)
        self.screen.mainloop()


t = TurtleOOP()

