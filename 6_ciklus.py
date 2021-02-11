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


        turtle.penup()
        turtle.goto(0,30)
        turtle.setheading(90)
        turtle.pendown()
        for i in range(90):
            turtle.forward(1)
            turtle.left(4)
        turtle.setheading(-90)
        turtle.forward(30)
        for i in range(45):
            turtle.forward(1)
            turtle.right(4)

        turtle.penup()
        turtle.goto(7, -10)
        turtle.setheading(90)
        turtle.pendown()
        for i in range(36):
            turtle.forward(1)
            turtle.right(10)

        turtle.penup()
        turtle.goto(50, -10)
        turtle.setheading(225)
        turtle.pendown()
        for i in range(75):
            turtle.forward(1)
            turtle.right(4)

        turtle.penup()
        turtle.goto(500, -100)


        screen.mainloop()


TurtleOOP()