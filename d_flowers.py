from turtle import Turtle
from turtle import Screen
from random import Random

class TurtleOOP:
    turtle = Turtle()
    screen = Screen()

    def flower(self, r: int, count: int):
        self.turtle.begin_fill()
        for i in range(count):
            self.turtle.forward(r)
            self.turtle.left(180 - 180 / count)
        self.turtle.end_fill()

    def flower25(self):
        for i in range(25):
            self.turtle.penup()
            self.turtle.goto((i % 5) * 150 - 400, (i / 5) * 150 - 400)
            self.turtle.pendown()
            self.flower(130, i * 2 + 1)

    def __init__(self):
        self.turtle._delay(0)
        self.turtle.speed(0)
        self.turtle.color("red")
        self.turtle.fillcolor("yellow")

        self.turtle.goto(80, 30)
        self.flower(30, 21)

        self.turtle.goto(-30, 80)
        self.flower(60, 21)

        self.screen.mainloop()


t = TurtleOOP()
