from turtle import Turtle
from turtle import Screen


class TurtleOOP:
    def __init__(self):
        screen = Screen()
        screen.setup(width=640, height=480)
        turtle = Turtle()

        turtle.goto(-100, -50)
        turtle.penup()
        turtle.goto(20, 50)
        turtle.pendown()
        turtle.goto(screen.window_width() / 2, screen.window_height()/2)

        screen.mainloop()


TurtleOOP()