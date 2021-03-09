from turtle import Turtle
from turtle import Screen
from random import *


class TurtleOOP:

    turtle = Turtle()
    screen = Screen()
    random = Random()

    def fillrect(self, w: int, h: int, color: str, bg: str):
        self.turtle.color(color)
        self.turtle.fillcolor(bg)
        self.turtle.begin_fill()
        for i in range(2):
            self.turtle.forward(w)
            self.turtle.right(90)
            self.turtle.forward(h)
            self.turtle.right(90)
        self.turtle.end_fill()

    def white(self, w: int):
        self.fillrect(w, w*5, "black", "white")

    def black(self, w: int):
        self.fillrect(w * 0.66, w * 3.33, "black", "black")

    def octave(self, w: int):
        for i in range(7):
            self.white(w)
            self.turtle.forward(w)
        self.turtle.backward(w * 7 - w / 3 * 2)
        for i in range(6):
            if i != 2:
                self.black(w)
            self.turtle.forward(w)
        self.turtle.forward(w / 3)

    def keyboard(self, w:int, oct: int):
        for i in range(oct):
            self.octave(w)

    def __init__(self):
        self.turtle._delay(0)
        self.turtle.speed(0)
        while 1:
            self.turtle.penup()
            self.turtle.goto(self.random.randint(-self.screen.window_width() / 2, self.screen.window_width() / 2), self.random.randint(-self.screen.window_height() / 2, self.screen.window_height() / 2))
            self.turtle.setheading(self.random.randint(0, 359))
            self.turtle.pendown()
            self.keyboard(self.random.randint(10, 40), self.random.randint(2, 7))
        self.screen.mainloop()


t = TurtleOOP()