from turtle import Turtle
from turtle import Screen


class TurtleOOP:
    def __init__(self):
        screen = Screen()
        turtle = Turtle()

        turtle.goto(200, 200)
        turtle.penup()
        turtle.goto(-200, 200)
        turtle.pendown()
        turtle.goto(200, 10)

        screen.mainloop()

        # width = 10
        # for b in range(100):
        #     for a in range(2):
        #         turtle.forward(width)
        #         turtle.left(90)
        #     width = width + 10
        # screen.mainloop()


TurtleOOP()