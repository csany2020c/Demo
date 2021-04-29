from turtle import *

class Segment:
    t: Turtle
    size: int
    isOn: bool = True

    def __init__(self, x:int, y:int, rotate: int, size:int):
        self.t = Turtle()
        self.t.speed(0)
        self.t._delay(0)
        self.size = size
        self.t.hideturtle()
        self.t.penup()
        self.t.goto(x,y)
        self.t.setheading(rotate)
        self.t.pendown()
        self.set(False)

    def _paint(self, r: float, g: float, b: float):
        self.t.clear()
        self.t.fillcolor(r, g, b)
        self.t.begin_fill()
        self.t.left(45)
        self.t.forward(self.size / 5)
        self.t.right(45)
        self.t.forward(self.size - (self.size / 5 / 1.4142135623730950488016887242097))
        self.t.right(45)
        self.t.forward(self.size / 5)
        self.t.right(90)
        self.t.forward(self.size / 5)
        self.t.right(45)
        self.t.forward(self.size - (self.size / 5 / 1.4142135623730950488016887242097))
        self.t.right(45)
        self.t.forward(self.size / 5)
        self.t.right(135)
        self.t.end_fill()

    def set(self, on: bool):
        if self.isOn == on:
            return
        self.isOn = on
        if on:
            self._paint(0, 0.8, 0)
        else:
            self._paint(0, 0.2, 0)

# Segment(0,0,0,100)
# Screen().mainloop()