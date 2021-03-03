
from turtle import Turtle
from turtle import Screen
class TurtleOOP:

    def __init__(self):
        screen = Screen()
        turtle = Turtle()
        a = 45
        turtle.width(3)
        for i in range(4):
            turtle.forward(250)
            turtle.left(a)
            turtle.forward(88)
            turtle.backward(88)
            turtle.right(a)
            a = a - 90
            turtle.left(90)
        turtle.goto(62.5, 62.5)
        for u in range(4):
            turtle.forward(250)
            turtle.left(90)
        screen.mainloop()

TurtleOOP()