from turtle import Turtle
from turtle import Screen


class Kotta:

    def line(self, x1: int, y1: int, x2: int, y2: int, turtle: Turtle):
        turtle.penup()
        turtle.goto(x1,y1)
        turtle.pendown()
        turtle.goto(x2, y2)

    def otvonal(self, y: int, turtle: Turtle, screen: Screen):
        left = -screen.window_width() / 2
        right = screen.window_width() / 2
        for i in range(5):
            self.line(right, y - i * 10, left,  y - i * 10, turtle)
            print(i)


    def __init__(self):
        screen = Screen()
        screen.setup(width=740, height=480)
        turtle = Turtle()
        turtle._delay(0)
        turtle.speed(0)

        # for i in range(41):
        #     print(200 - i * 10)
        #     self.line(-200, 200 - i * 10, -200 + i * 10, -200, turtle)

        for i in range(5):
            self.otvonal(200 - i * 70, turtle, screen)

        screen.mainloop()


Kotta()