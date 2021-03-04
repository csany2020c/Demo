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
        for i in range(82):
            self.turtle.forward(1)
            self.turtle.right(10)

        self.turtle.left(95)
        self.turtle.forward(50)

        for i in range(82):
            self.turtle.forward(1)
            self.turtle.right(10)

        self.turtle.left(180)
        self.turtle.forward(20)
        self.turtle.left(90)
        self.turtle.forward(20)
        self.turtle.right(90)
        self.turtle.forward(20)
        self.turtle.left(90)
        self.turtle.forward(30)
        self.turtle.left(90)
        self.turtle.forward(20)
        self.turtle.right(90)
        self.turtle.forward(15)
        self.turtle.left(90)
        self.turtle.forward(25)
