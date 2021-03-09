from turtle import Turtle
from turtle import Screen
from random import Random
from math import *


class Jel:
    turtle: Turtle
    screen = Screen()

    def __init__(self, turtle: Turtle):
        self.turtle = turtle


    def jel(self, tipus: int):
        tipus = tipus % 6

        if tipus == 0:
            self.fenyofa() # Fekete Félix
            return
        if tipus == 1:
            self.katica() # Horváth Márk
            return
        if tipus == 2:
            self.kocsi() # Szabó Bálint
            return
        if tipus == 3:
            self.pottyoslabda() # Kollár Bálint
            return
        if tipus == 4:
            self.gyongysor() # Mándli Ivett
            return
        if tipus == 5:
            self.kifli() # Konczik Ádám
            return

    def fagyi(self):
        self.turtle.right(110)
        self.turtle.forward(50)
        self.turtle.right(150)
        self.turtle.forward(50)
        self.turtle.right(105)
        self.turtle.forward(25)
        self.turtle.circle(23)
        self.turtle.penup()
        self.turtle.left(80)
        self.turtle.forward(10)
        self.turtle.pendown()
        self.turtle.circle(23)
        self.turtle.penup()
        self.turtle.right(11)
    # def mintajel(self):
        # self.turtle.forward(20)
        # self.turtle.right(30)
        # self.turtle.forward(20)


    def fenyofa(self):
        self.turtle.right(120)
        self.turtle.forward(40)
        self.turtle.left(90)
        self.turtle.forward(30)
        self.turtle.left(90)
        self.turtle.forward(30)
        self.turtle.left(70)
        self.turtle.forward(34)
        self.turtle.right(210)
        self.turtle.forward(70)
        self.turtle.left(180)
        self.turtle.forward(120)
        self.turtle.left(130)
        self.turtle.forward(30)
        self.turtle.right(240)
        self.turtle.forward(25)
        self.turtle.left(70)
        self.turtle.forward(30)
        self.turtle.left(120)
        self.turtle.forward(25)

    def ellipse(self, x1: float, y1: float, x2: float, y2: float):
        # double t, a, b, tinc, centx, centy;
        a = abs(0.5 * (x2 - x1))
        b = abs(0.5 * (y2 - y1))
        tinc = pi * 2 / (a + b)
        centx = ((x1 + x2) + .5) * .5
        centy = ((y1 + y2) + .5) * .5
        self.turtle.goto(centx + a, centy)
        t = 0
        while t < pi * 2:
            self.turtle.goto(centx + a * cos(t), centy - b * sin(t))
            t = t + tinc
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
    def kocsi(self):
        self.turtle.penup()
        self.turtle.back(85)
        self.turtle.pendown()
        self.turtle.left(90)
        self.turtle.forward(20)
        self.turtle.right(90)
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
        self.turtle.left(90)
        self.turtle.forward(30)
        self.turtle.left(90)
        self.turtle.forward(20)
        self.turtle.right(90)
        self.turtle.forward(15)
        self.turtle.left(90)
        self.turtle.forward(25)
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
    def gyongysor(self):
        self.turtle.penup()
        self.turtle.goto(170, 130)
        self.turtle.setheading(225)
        self.turtle.pendown()
        for i in range(90):
            self.turtle.forward(2)
            self.turtle.right(1)

        self.turtle.fillcolor("red")

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

    def kocsi2(self):
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

