from turtle import *

class Segment:
    _t: Turtle
    _size: int
    _isOn: bool = True

    def __init__(self, x:int, y:int, rotate: int, size:int):
        self._t = Turtle()
        self._t.speed(0)
        self._t._delay(0)
        self._size = size
        self._t.hideturtle()
        self._t.penup()
        self._t.goto(x, y)
        self._t.setheading(rotate)
        self._t.pendown()
        self.set(False)

    def _paint(self, r: float, g: float, b: float):
        self._t.clear()
        self._t.fillcolor(r, g, b)
        self._t.begin_fill()
        self._t.left(45)
        self._t.forward(self._size / 5)
        self._t.right(45)
        self._t.forward(self._size - (self._size / 5 / 1.4142135623730950488016887242097))
        self._t.right(45)
        self._t.forward(self._size / 5)
        self._t.right(90)
        self._t.forward(self._size / 5)
        self._t.right(45)
        self._t.forward(self._size - (self._size / 5 / 1.4142135623730950488016887242097))
        self._t.right(45)
        self._t.forward(self._size / 5)
        self._t.right(135)
        self._t.end_fill()

    def set(self, on: bool):
        if self._isOn == on:
            return
        self._isOn = on
        if on:
            self._paint(0, 0.8, 0)
        else:
            self._paint(0, 0.2, 0)

#
# s = Segment(100,0,20,100)
# s.set(False)
# s2 = Segment(130,30,-50,100)
# s2.set(True)
#
# Screen().mainloop()