from turtle import Turtle
from turtle import Screen
from random import Random

class TurtleOOP:
    turtle = Turtle()
    screen = Screen()

    def hold(self):
        self.turtle.speed(200)
        self.turtle.penup()
        self.turtle.goto(-200, 20)
        self.turtle.left(200)
        self.turtle.pendown()
        self.turtle.begin_fill()
        for i in range(180):
            self.turtle.right(1)
            self.turtle.forward(1)
        self.turtle.left(160)
        for i in range(200):
            self.turtle.left(1)
            self.turtle.forward(1)
        self.turtle.end_fill()

    def bg(self):
        for k in range(40):
            self.turtle.goto(-self.screen.window_width()/2, self.screen.window_height()/2 - self.screen.window_height() / 40.0 * k)
            self.turtle.settiltangle(90)
            self.turtle.color((0, 0, 0.5 - k / 80))
            self.turtle.fillcolor((0, 0, 0.5 - k / 80))
            self.turtle.begin_fill()
            for i in range(2):
                self.turtle.forward(self.screen.window_width())
                self.turtle.right(90)
                self.turtle.forward(self.screen.window_height() / 40)
                self.turtle.right(90)
            self.turtle.end_fill()

    def star(self, a: int):
        self.turtle.begin_fill()
        for i in range(5):
            self.turtle.forward(a)
            self.turtle.left(144)
        self.turtle.end_fill()

    def __init__(self):
        self.turtle._delay(0)
        self.turtle.speed(0)
        r = Random()

        x = r.randint(2, 9)
        print(x)

        self.bg()

        self.turtle.fillcolor((1, 1, 0))
        self.turtle.color((1, 1, 0))
        for i in range(50):
            self.turtle.penup()
            self.turtle.goto(r.randint(0, self.screen.window_width())-self.screen.window_width()/2, r.randint(0, self.screen.window_height())-self.screen.window_height()/2)
            self.turtle.pendown()
            self.star(r.randint(5, 50))

        self.hold()
        self.screen.mainloop()


t = TurtleOOP()