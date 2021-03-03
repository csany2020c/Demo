from turtle import Turtle
from turtle import Screen


class TurtleOOP:
    def __init__(self):
        print("Hello world")
        screen = Screen()
        screen.setup(width=640, height=480)
        screen.bgcolor("pink")
        turtle = Turtle()
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(100)
        # https://www.calculat.org/hu/terulet-kerulet/derekszogu-haromszog.html
        turtle.left(90 + 26.5651)
        turtle.forward(223.60679774997896964091736687313)

        screen.mainloop()


TurtleOOP()
