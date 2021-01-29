from turtle import Turtle
from turtle import Screen


class TurtleOOP:

    def square(self, turtle):
        for i in range(4):
            print(i)
            turtle.forward(100)
            turtle.left(90)

    def __init__(self):
        screen = Screen()
        screen.setup(width=640, height=480)
        turtle = Turtle()
        turtle.shape("turtle")

        self.square(turtle)

        turtle.penup()
        turtle.forward(200)
        turtle.pendown()

        for i in range(36):
            self.square(turtle)
            turtle.left(10)

        screen.mainloop()


TurtleOOP()
