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

    def coords(self):
        self.turtle.penup()
        self.turtle.goto(self.left, 0)
        self.turtle.pendown()
        self.turtle.goto(self.right, 0)

        self.turtle.penup()
        self.turtle.goto(0, self.top)
        self.turtle.pendown()
        self.turtle.goto(0, self.bottom)

    def f(self, x: float):
        return x * x * 0.005 + x + 8

    def g(self, x: float):
        return x*x*x * 0.005 + x*x * 0.005 - x + 3

    def e(self, x: float):
        return x * 5 + 30

    # https://mathworld.wolfram.com/FourierSeriesSquareWave.html
    def squarewave(self, x: float, L: float = 20, height: float = 100, iterations: int = 27):
        y = 0.0
        for n in range(1, iterations, 2):
            y = y + 1 / float(n) * sin(n * pi * x / L)
        return 4.0 / pi * y * height

    def __init__(self):
        self.turtle._delay(0)
        self.turtle.speed(0)
        self.turtle.penup()

        self.coords()

        self.turtle.penup()
        self.turtle.goto(self.left, 0)
        self.turtle.pendown()
        for x in range(self.left, self.right, 1):
            self.turtle.goto(x, self.e(x))


        self.turtle.penup()
        self.turtle.goto(self.left, 0)
        self.turtle.pendown()
        for x in range(self.left, self.right, 1):
            self.turtle.goto(x, int(self.squarewave(x * 0.1, 20, 100, 100)))

        self.turtle.penup()
        self.turtle.goto(self.left, 0)
        self.turtle.pendown()
        for x in range(self.left, self.right, 1):
            self.turtle.goto(x, int(self.f(x)))

        self.turtle.penup()
        self.turtle.goto(self.left, 0)
        self.turtle.pendown()
        for x in range(self.left, self.right, 1):
            self.turtle.goto(x, self.g(x))


        self.screen.mainloop()


t = TurtleOOP()

