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

    def fagyi(self):
        self.turtle.right(110)
        self.turtle.forward(50)
        self.turtle.right(150)
        self.turtle.forward(50)
        self.turtle.right(105)
        self.turtle.forward(25)
        self.turtle.circle(20)
        self.turtle.penup()
        self.turtle.left(80)
        self.turtle.forward(10)
        self.turtle.pendown()
        self.turtle.circle(20)
        self.turtle.penup()
        self.turtle.right(10)
        self.turtle.forward(20)
        self.turtle.pendown()
        self.turtle.circle(20)

