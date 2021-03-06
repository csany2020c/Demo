from turtle import Turtle
from turtle import Screen


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
        self.turtle.penup()
        self.turtle.forward(32)
        self.turtle.pendown()
        self.turtle.color("brown")
        self.turtle.begin_fill()
        self.trapez()
        self.turtle.end_fill()
        self.turtle.penup()
        self.turtle.left(145)
        self.turtle.forward(30)
        self.turtle.pendown()
        self.turtle.right(95)
        self.turtle.forward(50)
        self.turtle.right(120)
        self.turtle.left(182.5)
        self.turtle.color("white")
        self.turtle.begin_fill()
        self.triangle()
        self.turtle.end_fill()
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
        s.turtle.begin_fill()
        s.turtle.fillcolor("lightblue")
        s.turtle.forward(-60)
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
        s.turtle.end_fill()
        s.turtle.fillcolor("black")
        s.turtle.begin_fill()
        for i in range(180):
            s.turtle.forward(0.3)
            s.turtle.left(1)
        s.turtle.end_fill()
        s.turtle.right(90)
        s.turtle.forward(8)
        s.turtle.right(90)
        s.turtle.begin_fill()
        for i in range(180):
            s.turtle.forward(0.3)
            s.turtle.left(1)
        s.turtle.end_fill()
        s.turtle.end_fill()
        s.turtle.right(90)
        s.turtle.forward(8)
        s.turtle.right(90)
        s.turtle.begin_fill()
        for i in range(180):
            s.turtle.forward(0.3)
            s.turtle.left(1)
        s.turtle.end_fill()
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

    def focilabda(self):
        self.turtle.penup()
        self.turtle.right(90)
        self.turtle.forward(50)
        self.turtle.left(90)
        self.turtle.pendown()
        self.turtle.begin_fill()
        self.turtle.color('white')
        for i in range(360):
            self.turtle.forward(1)
            self.turtle.left(1)
        self.turtle.end_fill()
        self.turtle.left(135)
        self.turtle.penup()
        self.turtle.forward(10)
        self.turtle.pendown()
        self.turtle.begin_fill()
        self.turtle.color('red')
        for i in range(5):
            self.turtle.forward(13)
            self.turtle.right(75)
        self.turtle.end_fill()
        self.turtle.penup()
        self.turtle.forward(50)
        self.turtle.pendown()
        self.turtle.begin_fill()
        for i in range(5):
            self.turtle.forward(13)
            self.turtle.right(75)
        self.turtle.end_fill()
        self.turtle.penup()
        self.turtle.right(90)
        self.turtle.forward(30)
        self.turtle.pendown()
        self.turtle.begin_fill()
        for i in range(5):
            self.turtle.forward(13)
            self.turtle.right(75)
        self.turtle.end_fill()
        self.turtle.penup()
        self.turtle.right(45)
        self.turtle.forward(30)
        self.turtle.pendown()
        self.turtle.begin_fill()
        for i in range(5):
            self.turtle.forward(13)
            self.turtle.right(75)
        self.turtle.end_fill()
        self.turtle.penup()
        self.turtle.right(180)
        self.turtle.forward(50)
        self.turtle.pendown()
        self.turtle.begin_fill()
        for i in range(5):
            self.turtle.forward(13)
            self.turtle.right(75)
        self.turtle.end_fill()
        self.turtle.penup()
        self.turtle.right(125)
        self.turtle.forward(35)
        self.turtle.pendown()
        self.turtle.begin_fill()
        for i in range(5):
            self.turtle.forward(13)
            self.turtle.right(75)
        self.turtle.end_fill()

    def domino(self, a:int = 99):
        self.turtle.backward(50)
        for i in range(2):
            self.turtle.color("black")
            self.turtle.begin_fill()
            self.turtle.forward(a)
            self.turtle.left(90)
            self.turtle.forward(a / 2)
            self.turtle.left(90)
            self.turtle.end_fill()
        self.turtle.forward(a / 2)
        self.turtle.left(90)
        self.turtle.forward(a / 2)
        self.turtle.backward(a / 4)
        self.turtle.left(90)
        self.turtle.penup()
        self.turtle.forward(a / 4)
        self.turtle.pendown()
        self.turtle.left(90)
        self.turtle.color("white")
        self.turtle.begin_fill()
        self.turtle.circle(a / 15)
        self.turtle.end_fill()
        self.turtle.left(90)
        self.turtle.penup()
        self.turtle.forward(a / 2)
        self.turtle.left(90)
        self.turtle.pendown()
        self.turtle.color("white")
        self.turtle.begin_fill()
        self.turtle.circle(a / 15)
        self.turtle.end_fill()

    def cseresznye(self):
        self.turtle.penup()
        self.turtle.backward(40)
        self.turtle.right(90)
        self.turtle.forward(60)
        self.turtle.setheading(0)
        self.turtle.pendown()
        self.turtle.setheading(0)
        self.turtle.fillcolor(1, 0, 0)
        self.turtle.begin_fill()
        self.turtle.circle(25, 360, 360)
        self.turtle.end_fill()
        self.turtle.penup()
        self.turtle.forward(80)
        self.turtle.pendown()
        self.turtle.begin_fill()
        self.turtle.circle(25, 540, 360)
        self.turtle.end_fill()
        self.turtle.color(0, 1, 0)
        self.turtle.right(60)
        self.turtle.forward(80)
        self.turtle.left(120)
        self.turtle.forward(80)

    def ceruza(self):
        self.turtle.fillcolor(0.8, 0.1, 0)
        for i in range(4):
            self.turtle.begin_fill()
            self.turtle.forward(30 / 2)
            self.turtle.right(90)
            self.turtle.forward(55)
            self.turtle.forward(30 / 2)
            self.turtle.right(90)
            self.turtle.forward(35)
            self.turtle.end_fill()

        for h in range(1):
            self.turtle.begin_fill()
            self.turtle.forward(15)
            self.turtle.left(120)
            self.turtle.end_fill()
            self.turtle.begin_fill()
            self.turtle.forward(50)
            self.turtle.left(120)
            self.turtle.forward(50)
            self.turtle.backward(25)
            self.turtle.left(120)
            self.turtle.forward(25)
            self.turtle.end_fill()





    def letra(self):
        self.turtle.left(90)
        self.turtle.color("saddlebrown")
        self.turtle.back(100)
        for i in range(7):
            for i in range(4):
                self.turtle.forward(30)
                self.turtle.right(90)
            self.turtle.forward(30)


    def fa(self, a: int = 10):
            self.turtle.pendown()
            self.turtle.begin_fill()
            self.turtle.fillcolor(0.86, 0.56, 0.41)
            self.turtle.right(90)
            self.turtle.forward(80)
            self.turtle.left(90)
            self.turtle.forward(30)
            self.turtle.left(90)
            self.turtle.forward(80)
            self.turtle.right(50)
            self.turtle.forward(0)
            self.turtle.end_fill()
            self.turtle.begin_fill()
            self.turtle.color(0, 0.8, 0)
            for i in range(20):
                self.turtle.right(50)
                self.turtle.circle(20, 80)
            self.turtle.end_fill()

    def hagyma(self, a:int = 10):
        self.turtle.fillcolor(0.4,0.1, 0.25)
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
        self.turtle.backward(64)
        self.turtle.color('yellow')
        for i in range(25):
            self.turtle.forward(128)
            self.turtle.left(165)
        self.turtle.color('black')

    def gomba(self):
        self.turtle.penup()
        self.turtle.left(180)
        self.turtle.forward(20)
        self.turtle.right(90)
        self.turtle.forward(-50)
        self.turtle.right(90)
        self.turtle.forward(-10)
        self.turtle.pendown()
        self.turtle.begin_fill()
        self.turtle.fillcolor(1, 1, 1)
        for i in range(4):
            self.turtle.forward(70)
            self.turtle.left(90)
        self.turtle.end_fill()
        self.turtle.left(90)
        self.turtle.forward(70)
        self.turtle.left(90)
        self.turtle.forward(35)
        self.turtle.right(180)
        self.turtle.begin_fill()
        self.turtle.fillcolor(0.8, 0.1, 0)
        self.turtle.forward(140)
        self.turtle.left(120)
        for k in range(172):
            self.turtle.left(0.7)
            self.turtle.forward(1)
        self.turtle.end_fill()

    def haziko(self):
        self.turtle.begin_fill()
        self.turtle.fillcolor('yellow')
        self.turtle.forward(100)
        self.turtle.left(90)
        self.turtle.forward(100)
        self.turtle.left(90)
        self.turtle.forward(100)
        self.turtle.left(90)
        self.turtle.forward(100)
        self.turtle.left(90)
        self.turtle.forward(50)
        self.turtle.end_fill()
        self.turtle.begin_fill()
        self.turtle.fillcolor('brown')
        self.turtle.left(90)
        self.turtle.forward(25)
        self.turtle.right(90)
        self.turtle.forward(10)
        self.turtle.right(90)
        self.turtle.forward(25)
        self.turtle.end_fill()
        self.turtle.left(90)
        self.turtle.forward(20)
        self.turtle.left(90)
        self.turtle.penup()
        self.turtle.forward(40)
        self.turtle.begin_fill()
        self.turtle.fillcolor('cyan')
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
        self.turtle.end_fill()
        self.turtle.penup()
        self.turtle.forward(40)
        self.turtle.pendown()
        self.turtle.right(90)
        self.turtle.forward(70)
        self.turtle.right(90)

        self.turtle.forward(100)
        self.turtle.right(45)
        self.turtle.begin_fill()
        self.turtle.fillcolor('red')
        self.turtle.forward(75)
        self.turtle.right(95)
        self.turtle.forward(75)
        self.turtle.end_fill()
        self.turtle.penup()
        self.turtle.forward(150)
        self.turtle.pendown()
    def tv(self):
        self.turtle.forward(-66)
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
        self.turtle.right(89)
        self.turtle.forward(142)
        self.turtle.right(84)
        self.turtle.pendown()
        self.turtle.forward(60)
        self.turtle.right(51)
        self.turtle.forward(102)
        self.turtle.penup()
        self.turtle.forward(-133)
        self.turtle.right(90)
        self.turtle.forward(64)
        self.turtle.pendown()
        for i in range(4):
            self.turtle.forward(70)
            self.turtle.left(90)
        self.turtle.penup()
        self.turtle.left(90)
        self.turtle.forward(60)
        self.turtle.left(90)
        self.turtle.forward(43)
        self.turtle.pendown()
        self.turtle.right(29)
        self.turtle.forward(100)
        self.turtle.penup()
        self.turtle.left(100)
        self.turtle.forward(100)
        self.turtle.left(130)
        self.turtle.forward(40)
        self.turtle.pendown()
        self.turtle.forward(90)
        self.turtle.penup()
        self.turtle.right(21)
        self.turtle.forward(110)
        self.turtle.left(90)
        self.turtle.forward(18)
        self.turtle.pendown()
        self.turtle.begin_fill()
        self.turtle.circle(5)
        self.turtle.end_fill()
        self.turtle.penup()
        self.turtle.left(87)
        self.turtle.forward(60)
        self.turtle.begin_fill()
        self.turtle.circle(5)
        self.turtle.end_fill()

    def jel(self, tipus: int):
        tipus = tipus % 15
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
            self.focilabda() # Németh Csaba Bence
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
            self.hagyma() # Fellner Milán
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



