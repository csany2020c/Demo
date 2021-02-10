from turtle import Turtle
from turtle import Screen


class TurtleOOP:
    def __init__(self):
        screen = Screen()
        # screen.setup(width=640, height=480)
        turtle = Turtle()
        top = screen.window_height() / 2
        left = -screen.window_width() / 2
        right = screen.window_width() / 2
        turtle._delay(0)
        turtle.speed(0)

        turtle.color("blue")

        count = screen.window_height() / 90

        for i in range(int(count)):
            turtle.width(1)
            turtle.penup()
            turtle.goto(left, 0 - i*90 + top)
            turtle.pendown()
            turtle.goto(right, 0 - i*90 + top)

            turtle.penup()
            turtle.goto(left, -30 - i*90 + top)
            turtle.pendown()
            turtle.goto(right, -30 - i*90 + top)

            turtle.width(3)
            turtle.penup()
            turtle.goto(left, -60 - i*90 + top)
            turtle.pendown()
            turtle.goto(right, -60 - i*90 + top)

        screen.mainloop()


TurtleOOP()