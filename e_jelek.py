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

    def hajo(self):
        self.turtle.speed()
        #self.screen.setup(width=128, height=128)
        self.turtle.penup()
        self.turtle.goto(23, -20)
        self.turtle.pendown()
        self.trapez()
        self.turtle.penup()
        self.turtle.goto(3, -10)
        self.turtle.pendown()
        self.turtle.left(-125)
        self.turtle.penup()
        self.turtle.goto(-2, 30)
        self.turtle.pendown()
        self.turtle.forward(50)
        self.turtle.penup()
        self.turtle.goto(-16, 7)
        self.turtle.pendown()
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

    def letra(self):
        self.turtle._delay(0)
        self.turtle.speed(0)
        self.turtle.left(90)
        self.turtle.goto(0, -180)
        for i in range(7):
            for i in range(4):
                self.turtle.forward(40)
                self.turtle.right(90)
            self.turtle.forward(40)

    def triangle(self):
        self.turtle.left(90)
        for i in range(3):
            self.turtle.forward(30)
            self.turtle.left(120)

    def vonat(self):
        s = self
        s.turtle.forward(-55)
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
        self.turtle.forward(50)
        self.turtle.right(90)
        self.turtle.forward(30)
        self.turtle.setheading(0)
        self.turtle.left(90)
        for i in range(2):
            self.turtle.forward(90)
            self.turtle.right(90)
            self.turtle.forward(30)
            self.turtle.right(90)
        self.turtle.penup()
        self.turtle.forward(90)
        self.turtle.right(90)
        self.turtle.forward(15)
        self.turtle.left(90)
        self.turtle.pendown()
        self.turtle.forward(20)
        self.turtle.penup()
        self.turtle.right(90)
        self.turtle.forward(5)
        self.turtle.left(90)
        self.turtle.pendown()
        self.turtle.right(60)
        self.turtle.circle(10, -180)
        self.turtle.right(180)
        self.turtle.circle(10, 90)
        self.turtle.right(self.turtle.heading())
        self.turtle.right(180)
        self.turtle.circle(16, -160)

    def focilabda(self, a: int):
        r = Random()
        for i in range(5):
            self.turtle.forward(10)
            self.turtle.left(70)
        for j in range(5):
            self.turtle.penup()
            self.turtle.goto(r.randint(-30, 20), r.randint(-30, 20))
            self.turtle.pendown()
        #self.focilabda(r.randint(10, 50))

        self.turtle.penup()
        self.turtle.goto(-50, -25)
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

    def ceruza(self, width: int = 180, height: int = 240):
        self.turtle.goto(height / 2, width / 2)
        for i in range(2):
            self.turtle.forward(30)
            self.turtle.left(90)
            self.turtle.forward(150)
            self.turtle.left(90)
            self.turtle.forward(30)
        for a in range(1):
            self.turtle.penup()
            self.turtle.goto(30, 150)
            self.turtle.pendown()
            for b in range(2):
                self.turtle.right(-120)
                self.turtle.forward(60)
            self.turtle.penup()
            self.turtle.goto(0, 200)
            self.turtle.forward(20)
            self.turtle.left(120)
            self.turtle.pendown()

            for g in range(2):
                self.turtle.forward(20 / 2)

        j = Jel
        s = Szekreny
        turtle = Turtle
        screen = Screen
        s.polc(turtle)
        j.ceruza()


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
        for i in range(1):
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

    def jel(self, tipus: int):
        tipus = tipus % 10
        if tipus == 0:
            self.hold()
            return
        if tipus == 1:
            self.hajo()
            return
        if tipus == 2:
            self.vonat()
            return
        if tipus == 3:
            self.gyertya()
            return
        if tipus == 4:
            self.focilabda(1)
            return
        if tipus == 5:
            self.domino()
            return
        if tipus == 6:
            self.cseresznye()
            return
        if tipus == 7:
            self.ceruza()
            return
        if tipus == 8:
            self.korte()
            return
        if tipus == 9:
            self.nap()
            return
        if tipus == 10:
            self.gomba()
            return
        if tipus == 11:
            self.haziko()
            return

class Szekreny:
    turtle: Turtle

    def color(self, r: float, g: float, b: float):
        self.turtle.color((r, g, b))
        self.turtle.fillcolor((r, g, b))

    def __init__(self, turtle: Turtle):
        self.turtle = turtle

    def polc(self, width: int = 180, height: int = 240, depth: int = 40):
        self.color(0.6, 0.6, 0.6)
        self.turtle.begin_fill()
        self.turtle.pendown()
        for i in range(2):
            self.turtle.forward(width)
            self.turtle.left(90)
            self.turtle.forward(height)
            self.turtle.left(90)
        self.turtle.end_fill()
        self.turtle.penup()

        self.color(0.8, 0.8, 0.8)
        self.turtle.left(90)
        self.turtle.forward(height)
        self.turtle.right(45)
        self.turtle.pendown()
        self.turtle.begin_fill()
        self.turtle.forward(depth)
        self.turtle.right(45)
        self.turtle.forward(width)
        self.turtle.right(135)
        self.turtle.forward(depth)
        self.turtle.right(45)
        self.turtle.forward(width)
        self.turtle.end_fill()

        self.turtle.penup()
        self.color(0.5, 0.5, 0.5)
        self.turtle.right(180)
        self.turtle.forward(width)
        self.turtle.pendown()
        self.turtle.left(45)
        self.turtle.begin_fill()
        self.turtle.forward(depth)
        self.turtle.right(135)
        self.turtle.forward(height)
        self.turtle.right(45)
        self.turtle.forward(depth)
        self.turtle.right(135)
        self.turtle.forward(height)
        self.turtle.end_fill()
        self.turtle.penup()

        self.color(0, 0, 0)
        self.turtle.penup()
        self.turtle.left(90)
        self.turtle.forward(width / 2)
        self.turtle.left(90)
        self.turtle.forward(height / 2)
        self.turtle.left(90)
        self.turtle.pendown()

    def szekreny(self, countx: int = 8, county: int = 2, width: int = 180, height: int = 240, depth: int = 20):
        startx = self.turtle.xcor()
        starty = self.turtle.ycor()
        jelrajzolo = Jel(self.turtle)
        i = 0
        for x in range(countx):
            for y in range(county):
                self.turtle.penup()
                self.turtle.goto(startx + x * (width + 10), starty + y * (height + 2))
                self.turtle.setheading(0)
                self.polc(width, height, depth)
                jelrajzolo.jel(i)
                i = i + 1


class TurtleOOP:

    turtle = Turtle()
    screen = Screen()

    left = -screen.window_width() / 2
    right = screen.window_width() / 2
    top = screen.window_height() / 2
    bottom = -screen.window_height() / 2

    def __init__(self):

        self.turtle.speed(0)
        self.turtle.penup()
        sz = Szekreny(self.turtle)

        # self.turtle.goto(self.left, self.bottom)
        # sz.szekreny(5, 3)

        sz.polc()
        j = Jel(self.turtle)
        j.ceruza()

        self.screen.mainloop()


#t = TurtleOOP()

