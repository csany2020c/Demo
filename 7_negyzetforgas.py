from turtle import Turtle
from turtle import Screen
from math import *


class TurtleOOP:
    def __init__(self):
        screen = Screen()
        turtle = Turtle()
        turtle._delay(0)
        turtle.speed(0)

        fw = 600
        rot = 1.9
        for k in range(25):
            turtle.penup()
            turtle.left(180)
            turtle.forward(fw/2)
            turtle.left(90)
            turtle.forward(fw / 2)
            turtle.left(90)
            # turtle.goto(-fw / 2, -fw / 2)

            turtle.pendown()
            for i in range(4):
                turtle.forward(fw)
                turtle.left(90)

            turtle.penup()
            turtle.forward(fw/2)
            turtle.left(90)
            turtle.forward(fw/2)
            turtle.right(90)

            turtle.right(rot)
            fw = (fw - 19)
            rot = rot/0.943


        # turtle.goto(0, 0)
        screen.mainloop()

TurtleOOP()