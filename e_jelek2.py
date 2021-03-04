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


    def fenyoag (self):
        for i in range(20):
            self.turtle.color("brown")
            self.turtle.forward(3)
            self.turtle.left(2)
            self.turtle.color("green")
            self.turtle.right(90)
            self.turtle.left(45)
            self.turtle.forward(10)
            self.turtle.backward(10)
            self.turtle.right(90)
            self.turtle.backward(10)
            self.turtle.forward(10)
            self.turtle.left(135)













