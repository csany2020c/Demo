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

    def pottyoslabda(self):
        self.turtle.penup()
        self.turtle.right(180)
        self.turtle.forward(60)
        self.turtle.left(90)
        for i in range(360):
            self.turtle.begin_fill()
            self.turtle.color('red')
            self.turtle.pendown()
            self.turtle.forward(1)
            self.turtle.left(1)
            self.turtle.end_fill()

        self.turtle.penup()
        self.turtle.left(90)
        self.turtle.forward(60)
        self.turtle.pendown()
        self.turtle.begin_fill()
        self.turtle.color('white')
        self.turtle.circle(10)
        self.turtle.end_fill()
        self.turtle.penup()
        self.turtle.left(180)
        self.turtle.forward(35)
        self.turtle.pendown()
        self.turtle.begin_fill()
        self.turtle.color('white')
        self.turtle.circle(10)
        self.turtle.end_fill()
        self.turtle.penup()
        self.turtle.left(180)
        self.turtle.forward(45)
        self.turtle.right(90)
        self.turtle.forward(25)
        self.turtle.pendown()
        self.turtle.begin_fill()
        self.turtle.color('white')
        self.turtle.circle(10)
        self.turtle.end_fill()
        self.turtle.penup()
        self.turtle.left(180)
        self.turtle.forward(65)
        self.turtle.left(90)
        self.turtle.forward(30)
        self.turtle.begin_fill()
        self.turtle.color('white')
        self.turtle.circle(10)
        self.turtle.end_fill()
        self.turtle.penup()
        self.turtle.right(180)
        self.turtle.forward(40)
        self.turtle.right(90)
        self.turtle.forward(10)
        self.turtle.begin_fill()
        self.turtle.color('white')
        self.turtle.circle(10)
        self.turtle.end_fill()
        self.turtle.penup()
        self.turtle.forward(600)

