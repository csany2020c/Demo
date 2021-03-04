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

    def kifli(self):
        self.turtle.width(2)
        self.turtle.fillcolor("#c9b75b")
        self.turtle.begin_fill()
        self.turtle.left(50)
        self.turtle.forward(100)
        for i in range(12):
            self.turtle.left(15)
            self.turtle.forward(3)
        for i in range(1):
            self.turtle.forward(100)
        for i in range(12):
            self.turtle.left(15)
            self.turtle.forward(3)
        self.turtle.end_fill()
        for i in range(1):
            self.turtle.forward(15)
            self.turtle.left(50)
            self.turtle.forward(29)
            self.turtle.right(50)
            self.turtle.forward(45)
            self.turtle.right(125)
            self.turtle.forward(30)
