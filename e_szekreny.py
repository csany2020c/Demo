from turtle import Turtle

class Szekreny:
    turtle: Turtle

    def color(self, r: float, g: float, b: float):
        self.turtle.color((r, g, b))
        self.turtle.fillcolor((r, g, b))

    def __init__(self, turtle: Turtle):
        self.turtle = turtle

    def polc(self, width: int = 180, height: int = 240, depth: int = 40):
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

        self.color(0, 0, 0)
        self.turtle.penup()
        self.turtle.left(90)
        self.turtle.forward(width / 2)
        self.turtle.left(90)
        self.turtle.forward(height / 2)
        self.turtle.left(90)
        self.turtle.pendown()

    def szekreny(self, countx: int = 8, county: int = 2, width: int = 180, height: int = 240, depth: int = 20):
        startx = self.turtle.xcor()
        starty = self.turtle.ycor()
        for x in range(countx):
            for y in range(county):
                self.turtle.penup()
                self.turtle.goto(startx + x * (width + 10), starty + y * (height + 2))
                self.turtle.setheading(0)
                self.polc(width, height, depth)

