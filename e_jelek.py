from turtle import Turtle
from turtle import Screen
from random import Random


class Jel:
    turtle: Turtle

    def __init__(self, turtle: Turtle):
        self.turtle = turtle

    def domino(self,a):
        for i in range(2):
            self.turtle.forward(a)
            self.turtle.left(90)
            self.turtle.forward(a / 2)
            self.turtle.left(90)
        self.turtle.forward(a / 2)
        self.turtle.left(90)
        self.turtle.forward(a / 2)
        self.turtle.backward(a / 4)
        self.turtle.left(90)
        self.turtle.penup()
        self.turtle.forward(a / 4)
        self.turtle.pendown()
        self.turtle.left(90)
        self.turtle.begin_fill()
        self.turtle.circle(a / 15)
        self.turtle.end_fill()
        self.turtle.left(90)
        self.turtle.penup()
        self.turtle.forward(a / 2)
        self.turtle.left(90)
        self.turtle.pendown()
        self.turtle.begin_fill()
        self.turtle.circle(a / 15)
        self.turtle.end_fill()


    def cseresznye(self):
        self.turtle.circle(25, 360, 360)
        self.turtle.penup()
        self.turtle.forward(80)
        self.turtle.pendown()
        self.turtle.circle(25, 540, 360)
        self.turtle.right(60)
        self.turtle.forward(80)
        self.turtle.left(120)
        self.turtle.forward(80)

        self.turtle.right(90)
        self.turtle.forward(100)
        self.turtle.left(90)
        self.turtle.forward(50)
        self.turtle.left(90)
        self.turtle.forward(100)
        self.turtle.right(50)
        self.turtle.forward(0)
        for i in range(22):
            self.turtle.right(45)
            self.turtle.circle(20, 60)

    def korte(self, a):
        self.turtle.begin_fill()
        self.turtle.left(270)
        for i in range(8):
            self.turtle.forward(a)
            self.turtle.left(10)
        for i in range(10):
            self.turtle.forward(a-2)
            self.turtle.right(15)
        self.turtle.right(20)
        self.turtle.forward(50)
        self.turtle.forward(50)
        for i in range(10):
            self.turtle.forward(a-2)
            self.turtle.right(15)
        for i in range(8):
            self.turtle.forward(a)
            self.turtle.left(10)
        self.turtle.right(110)
        self.turtle.forward(35)
        self.turtle.end_fill()
        self.turtle.left(180)

    def nap(self):
        for i in range(25):
            self.turtle.forward(128)
            self.turtle.left(165)

    def jel(self, tipus: int):
        tipus = tipus % 2
        if tipus == 0:
            self.cseresznye()
            return
        if tipus == 1:
            self.nap()
            return


class Szekreny:
    turtle: Turtle

    def color(self, r: float, g: float, b: float):
        self.turtle.color((r, g, b))
        self.turtle.fillcolor((r, g, b))

    def __init__(self, turtle: Turtle):
        self.turtle = turtle

    def polc(self, width: int, height: int, depth: int = 40):
        self.color(0.6, 0.6, 0.6)
        self.turtle.begin_fill()
        self.turtle.pendown()
        for i in range(2):
            self.turtle.forward(width)
            self.turtle.left(90)
            self.turtle.forward(height)
            self.turtle.left(90)
        self.turtle.end_fill()
        self.turtle.penup()

        self.color(0.8, 0.8, 0.8)
        self.turtle.left(90)
        self.turtle.forward(height)
        self.turtle.right(45)
        self.turtle.pendown()
        self.turtle.begin_fill()
        self.turtle.forward(depth)
        self.turtle.right(45)
        self.turtle.forward(width)
        self.turtle.right(135)
        self.turtle.forward(depth)
        self.turtle.right(45)
        self.turtle.forward(width)
        self.turtle.end_fill()

        self.turtle.penup()
        self.color(0.5, 0.5, 0.5)
        self.turtle.right(180)
        self.turtle.forward(width)
        self.turtle.pendown()
        self.turtle.left(45)
        self.turtle.begin_fill()
        self.turtle.forward(depth)
        self.turtle.right(135)
        self.turtle.forward(height)
        self.turtle.right(45)
        self.turtle.forward(depth)
        self.turtle.right(135)
        self.turtle.forward(height)
        self.turtle.end_fill()
        self.turtle.penup()

    def szekreny(self, countx: int = 8, county: int = 2, width: int = 180, height: int = 240, depth: int = 20):
        startx = self.turtle.xcor()
        starty = self.turtle.ycor()
        jelrajzolo = Jel(self.turtle)
        for x in range(countx):
            for y in range(county):
                self.turtle.penup()
                self.turtle.goto(startx + x * (width + 10), starty + y * (height + 2))
                self.turtle.setheading(0)
                self.polc(width, height, depth)
                self.color(0, 0, 0)
                self.turtle.penup()
                self.turtle.goto(startx + x * (width + 10) + width / 2, starty + y * (height + 2) + height / 2)
                self.turtle.pendown()
                jelrajzolo.jel(x + y * x)


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
        sz = Szekreny(self.turtle)
        self.turtle.goto(self.left, self.bottom)
        sz.szekreny(5, 3)

        self.screen.mainloop()


t = TurtleOOP()

