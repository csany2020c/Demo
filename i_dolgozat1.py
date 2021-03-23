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

    def ethernetplug(self, color: str = "lightblue", size: float = 1):
        x = self.turtle.xcor()
        y = self.turtle.ycor()
        rot = self.turtle.heading()

        self.turtle.pendown()
        self.turtle.fillcolor(color)
        self.turtle.begin_fill()
        self.turtle.forward(28 * size)
        self.turtle.left(90)
        self.turtle.forward(15 * size)
        self.turtle.right(90)
        self.turtle.forward(5 * size)
        self.turtle.left(90)
        self.turtle.forward(15 * size)
        self.turtle.left(90)
        self.turtle.forward(38 * size)
        self.turtle.left(90)
        self.turtle.forward(15 * size)
        self.turtle.left(90)
        self.turtle.forward(5 * size)
        self.turtle.right(90)
        self.turtle.forward(15 * size)
        self.turtle.end_fill()

        self.turtle.penup()
        self.turtle.backward(30 * size)
        self.turtle.pendown()

        for i in range(8):
            self.turtle.forward(5 * size)
            self.turtle.penup()
            self.turtle.backward(5 * size)
            self.turtle.left(90)
            self.turtle.forward(4 * size)
            self.turtle.right(90)
            self.turtle.pendown()

        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.setheading(rot)

    def router(self, size: float = 1):
        self.turtle.pendown()
        self.turtle.fillcolor("lightgrey")
        self.turtle.begin_fill()
        self.turtle.forward(230 * size)
        for i in range(180):
            self.turtle.left(1)
            self.turtle.forward(size / 2)
        self.turtle.forward(230 * size)
        for i in range(180):
            self.turtle.left(1)
            self.turtle.forward(size / 2)
        self.turtle.end_fill()

        self.turtle.penup()
        self.turtle.left(90)
        self.turtle.forward(size * 12)
        self.turtle.right(90)
        self.turtle.pendown()

        for i in range(5):
            if i == 0:
                self.ethernetplug(color="lightblue", size=size)
            else:
                self.ethernetplug(color="yellow", size=size)
            self.turtle.forward(size * 50)

    def __init__(self):
        self.turtle._delay(0)
        self.turtle.speed(0)
        self.turtle.penup()
        self.turtle.goto(-300, -300)
        self.router(size=1.1)

        self.turtle.penup()
        self.turtle.left(27)
        self.turtle.goto(-300, 0)
        self.router(size=0.6)

        self.turtle.penup()
        self.turtle.right(77)
        self.turtle.goto(100, 200)
        self.router(size=1.7)

        self.screen.mainloop()


t = TurtleOOP()

