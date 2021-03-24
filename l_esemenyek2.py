from turtle import *
from random import *
from j_clock import Clock

class Esemeny:

    scr = Screen()
    t1 = Turtle()
    t2 = Turtle()

    c = Clock(scr)

    def t1colorrandom(self):
        self.t1.color(random(), random(), random())
        pass

    def t2colorrandom(self):
        self.t2.color(random(), random(), random())
        pass

    def masodperckiir(self):
        print(self.c.sec())
        print(self.c.leftNumber(self.c.sec()))
        print(self.c.rightNumber(self.c.sec()))
        if self.c.leftNumber(self.c.sec()) == 1:
            print("A teknős most 1-est rajzol")

    def __init__(self):
        self.scr.onclick(self.katt)
        self.scr.onkey(self.t1colorrandom, "1")
        self.scr.onkey(self.t2colorrandom, "2")
        self.scr.listen()
        self.c.setOnSecondChangeListener(self.masodperckiir)
        self.scr.mainloop()

    def katt(self, x: float, y: float):
        print(x)
        print(y)
        print("----")
        self.t1.goto(x, y)
        self.t2.goto(-x, -y)



Esemeny()