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
        self.turtle.penup()
        self.turtle.goto(100, 90)
        self.turtle.pendown()
        self.turtle.begin_fill()
        self.turtle.circle(70,400)
        self.turtle.color('red')
        self.turtle.end_fill()

        self.turtle.penup()
        self.turtle.begin_fill()
        self.turtle.color('white')
        self.turtle.goto(100, 120)
        self.turtle.end_fill()
        self.turtle.pendown()
        self.turtle.circle(10, 400)
        self.turtle.penup()
        self.turtle.goto(70, 180)
        self.turtle.pendown()
        self.turtle.circle(10, 400)
        self.turtle.penup()
        self.turtle.goto(130, 160)
        self.turtle.pendown()
        self.turtle.circle(10, 400)
        self.turtle.penup()
        self.turtle.goto(120, 190)
        self.turtle.pendown()
        self.turtle.circle(10, 400)
        self.turtle.penup()
        self.turtle.goto(60, 150)
        self.turtle.pendown()
        self.turtle.circle(10, 400)





