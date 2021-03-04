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

    def katica(self):
        self.turtle.penup()
        self.turtle.right(125)
        self.turtle.forward(50)
        self.turtle.left(125)
        self.turtle.pendown()
        self.turtle.fillcolor("red")
        self.turtle.begin_fill()
        self.turtle.circle(75, 90)
        self.turtle.circle(25, 90)
        self.turtle.circle(75, 90)
        self.turtle.circle(25, 90)
        self.turtle.end_fill()
        self.turtle.penup()
        self.turtle.circle(75, 90)
        self.turtle.right(90)
        self.turtle.pendown()
        self.turtle.fillcolor("black")
        self.turtle.begin_fill()
        self.turtle.circle(10, 90)
        self.turtle.circle(25, 90)
        self.turtle.circle(10, 90)
        self.turtle.end_fill()
        self.turtle.penup()
        self.turtle.right(90)
        self.turtle.circle(75, 15)
        self.turtle.right(90)
        self.turtle.pendown()
        self.turtle.forward(10)
        self.turtle.left(45)
        self.turtle.forward(20)
        for i in range(2):
            self.turtle.penup()
            self.turtle.backward(20)
            self.turtle.right(45)
            self.turtle.backward(10)
            self.turtle.left(90)
            self.turtle.circle(75, 30)
            self.turtle.right(90)
            self.turtle.pendown()
            self.turtle.forward(10)
            self.turtle.left(45)
            self.turtle.forward(20)

        self.turtle.penup()
        self.turtle.backward(20)
        self.turtle.right(45)
        self.turtle.backward(10)
        self.turtle.left(90)
        self.turtle.circle(75, 15)
        self.turtle.circle(25, 90)
        self.turtle.circle(75, 15)
        self.turtle.right(90)
        self.turtle.pendown()
        self.turtle.forward(10)
        self.turtle.right(45)
        self.turtle.forward(20)
        for i in range(2):
            self.turtle.penup()
            self.turtle.backward(20)
            self.turtle.left(45)
            self.turtle.backward(10)
            self.turtle.left(90)
            self.turtle.circle(75, 30)
            self.turtle.right(90)
            self.turtle.pendown()
            self.turtle.forward(10)
            self.turtle.right(45)
            self.turtle.forward(20)
        self.turtle.penup()
        self.turtle.backward(20)
        self.turtle.left(45)
        self.turtle.backward(10)
        self.turtle.left(90)
        self.turtle.circle(75, 15)
        self.turtle.circle(25, 45)
        self.turtle.left(90)
        self.turtle.pendown()
        self.turtle.forward(125)