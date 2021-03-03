from turtle import Turtle
from turtle import Screen
from random import Random


class Jel:
    turtle: Turtle
    screen = Screen()

    def __init__(self, turtle: Turtle):
        self.turtle = turtle

    def hold(self):
        for i in range(128):
            self.turtle.right(1)
            self.turtle.forward(1)
        self.turtle.left(160)
        for i in range(148):
            self.turtle.left(1)
            self.turtle.forward(1)
        self.turtle.end_fill()

    def hajo(self, width: int = 180, height: int = 240):
        self.turtle.speed()
        #self.screen.setup(width=128, height=128)
        self.turtle.penup()
        self.turtle.forward(32)
        #self.turtle.goto(height / 2, width / 2)
        self.turtle.pendown()
        self.trapez()
        self.turtle.penup()
        self.turtle.left(145)
        self.turtle.forward(30)
        self.turtle.pendown()
        self.turtle.right(95)
        self.turtle.forward(50)
        self.turtle.right(120)
        self.turtle.left(182.5)
        self.triangle()
        #self.screen.mainloop()

    def trapez(self):
        self.turtle.left(180)
        self.turtle.forward(50)
        self.turtle.left(150)
        self.turtle.forward(20)
        self.turtle.left(30)
        self.turtle.forward(20)
        self.turtle.left(37)
        self.turtle.forward(20)

    def triangle(self):
        self.turtle.left(90)
        for i in range(3):
            self.turtle.forward(30)
            self.turtle.left(120)

    def vonat(self):
        s = self
        s.turtle.forward(-45)
        s.turtle.forward(128)
        s.turtle.left(90)
        s.turtle.forward(32)
        s.turtle.left(90)
        s.turtle.forward(16)
        s.turtle.right(90)
        s.turtle.forward(32)
        s.turtle.left(90)
        s.turtle.forward(16)
        s.turtle.left(90)
        s.turtle.forward(32)
        s.turtle.right(90)
        s.turtle.forward(64)
        s.turtle.right(90)
        s.turtle.forward(32)
        s.turtle.left(90)
        s.turtle.forward(32)
        s.turtle.left(90)
        s.turtle.forward(64)
        for i in range(180):
            s.turtle.forward(0.3)
            s.turtle.left(1)
        s.turtle.right(90)
        s.turtle.forward(8)
        s.turtle.right(90)
        for i in range(180):
            s.turtle.forward(0.3)
            s.turtle.left(1)
        s.turtle.right(90)
        s.turtle.forward(8)
        s.turtle.right(90)
        for i in range(180):
            s.turtle.forward(0.3)
            s.turtle.left(1)

    def gyertya(self):
        self.turtle.setheading(90)
        self.turtle.penup()
        self.turtle.right(180)
        self.turtle.forward(70)
        self.turtle.right(90)
        self.turtle.forward(15)
        self.turtle.pendown()
        self.turtle.setheading(0)
        self.turtle.left(90)
        self.turtle.fillcolor(1, 1, 1)
        self.turtle.begin_fill()
        for i in range(2):
            self.turtle.forward(90)
            self.turtle.right(90)
            self.turtle.forward(30)
            self.turtle.right(90)
        self.turtle.end_fill()
        self.turtle.penup()
        self.turtle.forward(90)
        self.turtle.right(90)
        self.turtle.forward(15)
        self.turtle.left(90)
        self.turtle.pendown()
        self.turtle.forward(10)
        self.turtle.penup()
        self.turtle.right(90)
        self.turtle.forward(5)
        self.turtle.left(90)
        self.turtle.pendown()
        self.turtle.right(60)
        self.turtle.fillcolor(1, 0.5, 0)
        self.turtle.begin_fill()
        self.turtle.circle(10, -180)
        self.turtle.right(180)
        self.turtle.circle(10, 90)
        self.turtle.right(self.turtle.heading())
        self.turtle.right(180)
        self.turtle.circle(16, -160)
        self.turtle.end_fill()

    def focilabda(self, a: int):
        r = Random()
        for i in range(5):
            self.turtle.forward(10)
            self.turtle.left(70)
        for j in range(5):
            self.turtle.penup()
            #self.turtle.goto(r.randint(-30, 20), r.randint(-30, 20))
            self.turtle.pendown()
        #self.focilabda(r.randint(10, 50))

        self.turtle.penup()
        self.turtle.forward(125)
        self.turtle.left(90)
        self.turtle.forward(150)
        self.turtle.pendown()

        for i in range(360):
            self.turtle.forward(1)
            self.turtle.left(1)

    def domino(self, a:int = 100):
        self.turtle.backward(50)
        for i in range(2):
            self.turtle.forward(a)
            self.turtle.left(90)
            self.turtle.forward(a / 2)
            self.turtle.left(90)
        self.turtle.forward(a / 2)
        self.turtle.left(90)
        self.turtle.forward(a / 2)
        self.turtle.backward(a / 4)
        self.turtle.left(90)
        self.turtle.penup()
        self.turtle.forward(a / 4)
        self.turtle.pendown()
        self.turtle.left(90)
        self.turtle.begin_fill()
        self.turtle.circle(a / 15)
        self.turtle.end_fill()
        self.turtle.left(90)
        self.turtle.penup()
        self.turtle.forward(a / 2)
        self.turtle.left(90)
        self.turtle.pendown()
        self.turtle.begin_fill()
        self.turtle.circle(a / 15)
        self.turtle.end_fill()

    def cseresznye(self):
        self.turtle.setheading(0)
        self.turtle.circle(25, 360, 360)
        self.turtle.penup()
        self.turtle.forward(80)
        self.turtle.pendown()
        self.turtle.circle(25, 540, 360)
        self.turtle.right(60)
        self.turtle.forward(80)
        self.turtle.left(120)
        self.turtle.forward(80)

    def ceruza(self):
        for i in range(2):
            self.turtle.fillcolor(0.8, 0.1, 0)
            self.turtle.begin_fill()
            self.turtle.forward(30)
            self.turtle.left(-90)
            self.turtle.forward(100)
            self.turtle.left(-90)
            self.turtle.forward(30)
            self.turtle.end_fill()
            self.turtle.begin_fill()
        for a in range(1):
            self.turtle.penup()
            self.turtle.end_fill()
            self.turtle.goto(159, 75)
            self.turtle.pendown()
            self.turtle.end_fill()
            self.turtle.begin_fill()
            for b in range(2):
                self.turtle.right(-120)
                self.turtle.forward(60)
            self.turtle.penup()
            self.turtle.goto(130, 125)
            self.turtle.forward(20)
            self.turtle.left(120)
            self.turtle.pendown()

            for g in range(2):
                self.turtle.forward(20 / 2)
            self.turtle.end_fill()

    def letra(self):
        self.turtle.left(90)
        for i in range(7):
            for i in range(4):
                self.turtle.forward(40)
                self.turtle.right(90)
            self.turtle.forward(40)

    def fa(self):
        self.turtle.right(90)
        self.turtle.forward(100)
        self.turtle.left(90)
        self.turtle.forward(50)
        self.turtle.left(90)
        self.turtle.forward(100)
        self.turtle.right(50)
        self.turtle.forward(0)
        for i in range(22):
            self.turtle.right(45)
            self.turtle.circle(20, 60)

    def korte(self, a:int = 10):
        self.turtle.fillcolor(0,0.8, 0.2)
        self.turtle.begin_fill()
        self.turtle.left(90)
        self.turtle.penup()
        self.turtle.forward(60)
        self.turtle.right(90)
        self.turtle.pendown()
        self.turtle.left(270)
        for i in range(8):
            self.turtle.forward(a)
            self.turtle.left(10)
        for i in range(10):
            self.turtle.forward(a-2)
            self.turtle.right(15)
        self.turtle.right(20)
        self.turtle.forward(50)
        self.turtle.forward(50)
        for i in range(10):
            self.turtle.forward(a-2)
            self.turtle.right(15)
        for i in range(8):
            self.turtle.forward(a)
            self.turtle.left(10)
        self.turtle.right(110)
        self.turtle.forward(35)
        self.turtle.end_fill()
        self.turtle.left(180)

    def nap(self):
        for i in range(25):
            self.turtle.forward(128)
            self.turtle.left(165)

    def gomba(self):
        for i in range(4):
            self.turtle.forward(70)
            self.turtle.left(90)
        self.turtle.left(90)
        self.turtle.forward(70)
        self.turtle.left(90)
        self.turtle.forward(70)
        self.turtle.right(180)
        self.turtle.forward(210)
        self.turtle.left(120)
        for k in range(151):
            self.turtle.left(0.8)
            self.turtle.forward(1.7)

    def haziko(self):
        self.turtle.forward(100)
        self.turtle.left(90)
        self.turtle.forward(100)
        self.turtle.left(90)
        self.turtle.forward(100)
        self.turtle.left(90)
        self.turtle.forward(100)
        self.turtle.left(90)
        self.turtle.forward(50)
        self.turtle.left(90)
        self.turtle.forward(25)
        self.turtle.right(90)
        self.turtle.forward(10)
        self.turtle.right(90)
        self.turtle.forward(25)
        self.turtle.left(90)
        self.turtle.forward(20)
        self.turtle.left(90)
        self.turtle.penup()
        self.turtle.forward(40)
        self.turtle.pendown()
        self.turtle.forward(15)
        self.turtle.left(90)
        self.turtle.forward(15)
        self.turtle.left(90)
        self.turtle.forward(15)
        self.turtle.left(90)
        self.turtle.forward(15)
        self.turtle.left(90)
        self.turtle.forward(10)
        self.turtle.left(90)
        self.turtle.forward(15)
        self.turtle.right(90)
        self.turtle.forward(5)
        self.turtle.right(90)
        self.turtle.forward(5)
        self.turtle.right(90)
        self.turtle.forward(15)
        self.turtle.penup()
        self.turtle.forward(40)
        self.turtle.pendown()
        self.turtle.right(90)
        self.turtle.forward(70)
        self.turtle.right(90)
        self.turtle.forward(100)
        self.turtle.right(45)
        self.turtle.forward(75)
        self.turtle.right(95)
        self.turtle.forward(75)
        self.turtle.penup()
        self.turtle.forward(150)
        self.turtle.pendown()

    def tv(self):
        for i in range(4):
            self.turtle.forward(100)
            self.turtle.right(90)
        self.turtle.forward(100)
        self.turtle.left(50)
        self.turtle.forward(60)
        self.turtle.right(140)
        self.turtle.forward(110)
        self.turtle.right(46)
        self.turtle.forward(53)
        self.turtle.penup()
        self.turtle.goto(0, 0)
        self.turtle.pendown()
        self.turtle.right(170)
        self.turtle.forward(56)
        self.turtle.right(54)
        self.turtle.forward(108)
        self.turtle.penup()
        self.turtle.goto(70, 20)
        self.turtle.pendown()
        self.turtle.left(50)
        self.turtle.forward(100)
        self.turtle.penup()
        self.turtle.goto(70, 20)
        self.turtle.pendown()
        self.turtle.left(67)
        self.turtle.forward(100)
        self.turtle.penup()
        self.turtle.goto(11, -21)
        self.turtle.right(117)
        self.turtle.pendown()
        for i in range(4):
            self.turtle.forward(64)
            self.turtle.right(90)
        self.turtle.penup()
        self.turtle.goto(87, -34)
        self.turtle.pendown()
        self.turtle.fillcolor('black')
        self.turtle.begin_fill()
        self.turtle.circle(6)
        self.turtle.end_fill()
        self.turtle.penup()
        self.turtle.goto(87, -82)
        self.turtle.pendown()
        self.turtle.fillcolor('black')
        self.turtle.begin_fill()
        self.turtle.circle(6)
        self.turtle.end_fill()

    def jel(self, tipus: int):
        tipus = tipus % 10
        if tipus == 0:
            self.hold() #Márkus Bence
            return
        if tipus == 1:
            self.hajo() # Csongor
            return
        if tipus == 2:
            self.vonat() # Loránd
            return
        if tipus == 3:
            self.gyertya() #Zsebők Dávid
            return
        if tipus == 4:
            self.focilabda(1) # Németh Csaba Bence
            return
        if tipus == 5:
            self.domino() # Kancsal Máté
            return
        if tipus == 6:
            self.cseresznye() # Horváth Boldizsár
            return
        if tipus == 7:
            self.ceruza() # Fatér László
            return
        if tipus == 8:
            self.korte() # Fellner Milán
            return
        if tipus == 9:
            self.nap() #Troznai Roland
            return
        if tipus == 10:
            self.gomba() # Zsuppán Flórián
            return
        if tipus == 11:
            self.haziko() # Ekler Dániel
            return
        if tipus == 12:
            self.fa() # Kalamár Rajmund
            return
        if tipus == 13:
            self.letra() # Marcon Tamás
            return
        if tipus == 14:
            self.tv() # Oláh Gergő
            return

