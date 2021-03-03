from turtle import Turtle
from turtle import Screen
from random import Random


class Jel:
    turtle: Turtle
    screen = Screen()

    def __init__(self, turtle: Turtle):
        self.turtle = turtle


    def jel(self, tipus: int):
        tipus = tipus % 10
        # if tipus == 0:
        #     self.hold() #Márkus Bence
        #     return

    def mintajel(self):
        self.turtle.forward(20)
        self.turtle.right(30)
        self.turtle.forward(20)

    def kocsi(self):
        self.turtle.penup()
        self.turtle.back(85)
        self.turtle.pendown()
        self.turtle.left(90)
        self.turtle.forward(20)
        self.turtle.right(90)
        self.turtle.forward(40)
        self.turtle.left(70)
        self.turtle.forward(40)
        self.turtle.right(70)
        self.turtle.forward(60)
        self.turtle.right(70)
        self.turtle.forward(40)
        self.turtle.left(70)
        self.turtle.forward(40)
        self.turtle.right(90)
        self.turtle.forward(20)
        self.turtle.right(90)
        self.turtle.forward(20)

        for i in range(15):
            self.turtle.left(3)
            self.turtle.forward(1)

        for i in range(35):
            self.turtle.right(3)
            self.turtle.forward(1)

        self.turtle.left(60)
        self.turtle.forward(40)

        for i in range(15):
            self.turtle.left(3)
            self.turtle.forward(1)

        for i in range(35):
            self.turtle.right(3)
            self.turtle.forward(1)

        self.turtle.left(60)
        self.turtle.forward(20)


