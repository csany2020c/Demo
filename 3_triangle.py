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
        turtle.penup()
        turtle.setposition(x=-screen.window_width() / 2 + 20, y=-screen.window_height() / 2 + 20)
        width = screen.window_width() - 60
        for i in range(7):
            turtle.pendown()
            self.triangle(turtle, width)
            turtle.penup()
            width = width / 2
            turtle.forward(width)
            turtle.left(60)
        screen.mainloop()


Triangle()
