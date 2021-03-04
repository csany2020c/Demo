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
        #self.turtle.forward(20)
        #self.turtle.right(30)
        #self.turtle.forward(20)
        self.turtle.begin_fill()
        self.turtle.circle(60, 400)
        self.turtle.color("red")
        self.turtle.end_fill()


        self.turtle.begin_fill()
        self.turtle.color("white")
        self.turtle.penup()
        self.turtle.goto(130, 170)
        self.turtle.pendown()
        self.turtle.end_fill()
        self.turtle.circle(10, 400)

        self.turtle.penup()
        self.turtle.goto(90, 170)
        self.turtle.pendown()
        self.turtle.circle(10, 400)
        self.turtle.penup()
        self.turtle.goto(80, 220)
        self.turtle.pendown()
        self.turtle.circle(10, 400)
        self.turtle.penup()
        self.turtle.goto(70, 160)
        self.turtle.pendown()
        self.turtle.circle(10, 400)
        self.turtle.penup()
        self.turtle.goto(100, 220)
        self.turtle.pendown()
        self.turtle.circle(10, 400)
        self.turtle.penup()
        self.turtle.goto(100, 160)
        self.turtle.pendown()
        self.turtle.circle(10, 400)
        self.turtle.penup()
        self.turtle.goto(45, 180)
        self.turtle.pendown()
        self.turtle.circle(10, 400)
        self.turtle.end_fill()

