from turtle import Turtle
from turtle import Screen


class TurtleOOP:
    def __init__(self):
        screen = Screen()
        turtle = Turtle()
        turtle._delay(0)
        turtle.speed(0)

        length = 2

        for a in range(256):
            turtle.forward(length)
            turtle.left(90)
            turtle.forward(length)
            turtle.left(90)
            length = length + 2

        screen.mainloop()


TurtleOOP()