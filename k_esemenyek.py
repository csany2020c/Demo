from turtle import *
from j_clock import Clock

class Kattintgato:

    scr = Screen()
    t = Turtle()
    c = Clock(scr)


    def klikk(self, x: float, y: float):
        print(x)
        print(y)
        self.t.goto(x, y)

    def up(self):
        print(self.c.leftNumber(self.c.sec()))
        print(self.c.rightNumber(self.c.sec()))
        if self.c.rightNumber(self.c.sec()) == 4:
            print("NÉGY")
        if self.c.rightNumber(self.c.sec()) == 5:
            print("ÖT")

    def __init__(self):
        self.scr.onclick(self.klikk)

        self.scr.onkey(self.up, "Escape")
        self.scr.listen()

        self.c.setOnSecondChangeListener(self.up)

        self.scr.mainloop()


Kattintgato()