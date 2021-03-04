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

    def gyongysor(self):
        self.turtle.penup()
        self.turtle.goto(170, 130)
        self.turtle.setheading(225)
        self.turtle.pendown()
        for i in range(90):
            self.turtle.forward(2)
            self.turtle.right(1)

        self.turtle.fillcolor("red")

        self.turtle.begin_fill()
        self.turtle.penup()
        self.turtle.goto(135, 105)
        self.turtle.pendown()
        self.turtle.circle(13)
        self.turtle.end_fill()

        self.turtle.fillcolor("blue")

        self.turtle.begin_fill()
        self.turtle.penup()
        self.turtle.goto(100, 100)
        self.turtle.pendown()
        self.turtle.circle(13)
        self.turtle.end_fill()

        self.turtle.fillcolor("yellow")

        self.turtle.begin_fill()
        self.turtle.penup()
        self.turtle.goto(65, 105)
        self.turtle.pendown()
        self.turtle.circle(13)
        self.turtle.end_fill()