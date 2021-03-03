from turtle import Turtle
from turtle import Screen


class Triangle:

    def triangle(self, turtle, width=100):
        for i in range(3):
            turtle.forward(width)
            turtle.left(120)

    def __init__(self):
        screen = Screen()
        turtle = Turtle()
        self.triangle(turtle, 200)
        turtle.forward(100)
        turtle.left(60)
        self.triangle(turtle, 100)
        screen.mainloop()


Triangle()
