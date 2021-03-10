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
        tipus = tipus % 13

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
        if tipus == 6:
            self.fagyi() # Kis Kornél
            return
        if tipus == 7:
            self.kocsi2() # Tóth Ákos
            return
        if tipus == 8:
            self.labda() # Vizdák Máté
            return
        if tipus == 9:
            self.fenyoag() # Rigó Donát
            return
        if tipus == 10:
            self.szivecske() # Dóra Márton
            return
        if tipus == 11:
            self.sziv() # Cziráki Leila
            return
        if tipus == 12:
            self.szivecske() # Dóra Márton
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
        self.turtle.forward(55)
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
        self.turtle.forward(123)
        self.turtle.penup()
        self.turtle.backward(25)
        self.turtle.left(90)
        self.turtle.forward(15)
        self.turtle.pendown()
        self.turtle.fillcolor("black")
        self.turtle.begin_fill()
        self.turtle.circle(10, 360)
        self.turtle.end_fill()
        self.turtle.penup()
        self.turtle.backward(30)
        self.turtle.pendown()
        self.turtle.fillcolor("black")
        self.turtle.begin_fill()
        self.turtle.circle(10, 360)
        self.turtle.end_fill()
        self.turtle.penup()
        self.turtle.forward(15)
        self.turtle.left(90)
        self.turtle.forward(30)
        self.turtle.right(90)
        self.turtle.forward(22.5)
        self.turtle.pendown()
        self.turtle.fillcolor("black")
        self.turtle.begin_fill()
        self.turtle.circle(10, 360)
        self.turtle.end_fill()
        self.turtle.penup()
        self.turtle.backward(45)
        self.turtle.pendown()
        self.turtle.fillcolor("black")
        self.turtle.begin_fill()
        self.turtle.circle(10, 360)
        self.turtle.end_fill()
        self.turtle.penup()
        self.turtle.forward(22.5)
        self.turtle.pendown()
        self.turtle.fillcolor("black")
        self.turtle.begin_fill()
        self.turtle.circle(10, 360)
        self.turtle.end_fill()
        self.turtle.penup()
        self.turtle.left(90)
        self.turtle.forward(30)
        self.turtle.right(90)
        self.turtle.forward(15)
        self.turtle.pendown()
        self.turtle.fillcolor("black")
        self.turtle.begin_fill()
        self.turtle.circle(10, 360)
        self.turtle.end_fill()
        self.turtle.penup()
        self.turtle.backward(30)
        self.turtle.pendown()
        self.turtle.fillcolor("black")
        self.turtle.begin_fill()
        self.turtle.circle(10, 360)
        self.turtle.end_fill()
        self.turtle.penup()
        self.turtle.forward(15)
        self.turtle.left(90)
        self.turtle.forward(32)
        self.turtle.right(90)
        self.turtle.forward(18)
        self.turtle.left(45)
        self.turtle.circle(10, 90)
        self.turtle.right(90)
        self.turtle.pendown()
        self.turtle.forward(15)
        self.turtle.right(45)
        self.turtle.forward(15)
        self.turtle.penup()
        self.turtle.backward(15)
        self.turtle.left(45)
        self.turtle.backward(15)
        self.turtle.left(90)
        self.turtle.circle(25, 90)
        self.turtle.right(90)
        self.turtle.pendown()
        self.turtle.forward(15)
        self.turtle.left(45)
        self.turtle.forward(15)
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
        self.turtle.pensize(2)
        self.turtle.forward(80)
        self.turtle.setheading(225)
        self.turtle.pendown()
        for i in range(90):
            self.turtle.forward(2)
            self.turtle.right(1)

        self.turtle.fillcolor("red")

        self.turtle.penup()
        self.turtle.right(180)
        self.turtle.forward(120)
        self.turtle.left(90)
        self.turtle.forward(75)
        self.turtle.begin_fill()
        self.turtle.pendown()
        self.turtle.circle(13)
        self.turtle.end_fill()

        self.turtle.fillcolor("blue")

        self.turtle.penup()
        self.turtle.left(100)
        self.turtle.forward(30)
        self.turtle.left(90)
        self.turtle.forward(20)
        self.turtle.right(90)
        self.turtle.forward(30)
        self.turtle.begin_fill()
        self.turtle.pendown()
        self.turtle.circle(13)
        self.turtle.end_fill()

        self.turtle.fillcolor("yellow")

        self.turtle.penup()
        self.turtle.left(180)
        self.turtle.forward(20)
        self.turtle.right(90)
        self.turtle.forward(20)
        self.turtle.right(90)
        self.turtle.forward(60)
        self.turtle.begin_fill()
        self.turtle.pendown()
        self.turtle.circle(13)
        self.turtle.end_fill()

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

    def labda(self):
        self.turtle.begin_fill()
        self.turtle.circle(70,400)
        self.turtle.color('red')
        self.turtle.end_fill()

        self.turtle.penup()
        self.turtle.begin_fill()
        self.turtle.color('white')
        self.turtle.goto(100, 150)
        self.turtle.end_fill()
        self.turtle.pendown()
        self.turtle.circle(10, 400)
        self.turtle.penup()
        self.turtle.goto(70, 220)
        self.turtle.pendown()
        self.turtle.circle(10, 400)
        self.turtle.penup()
        self.turtle.goto(130, 190)
        self.turtle.pendown()
        self.turtle.circle(10, 400)
        self.turtle.penup()
        self.turtle.goto(120, 240)
        self.turtle.pendown()
        self.turtle.circle(10, 400)
        self.turtle.penup()
        self.turtle.goto(60, 180)
        self.turtle.pendown()
        self.turtle.circle(10, 400)

    def szivecske(self):
        self.turtle.fillcolor('red')
        self.turtle.begin_fill()
        self.turtle.right(90)
        self.turtle.penup()
        self.turtle.forward(50)
        self.turtle.right(135)
        self.turtle.pendown()
        self.turtle.forward(55)
        for i in range(90):
            self.turtle.forward(1)
            self.turtle.right(2)
        self.turtle.left(90)
        for i in range(90):
            self.turtle.forward(1)
            self.turtle.right(2)
        self.turtle.forward(60)
        self.turtle.end_fill()

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

    def sziv(self):
        self.turtle.begin_fill()
        self.turtle.left(45)
        self.turtle.forward(105)
        self.turtle.left(45)
        for a in range(10):
            self.turtle.left(15)
            self.turtle.forward(length)
        self.turtle.right(135)
        for a in range(10):
            self.turtle.left(15)
            self.turtle.forward(length)
        self.turtle.left(60)
        self.turtle.forward(105)
        self.turtle.end_fill()