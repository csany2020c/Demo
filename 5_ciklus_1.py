from turtle import Turtle
from turtle import Screen


class TurtleOOP:
    def __init__(self):
        screen = Screen()
        screen.setup(width=640, height=480)
        turtle = Turtle()

        left_bottom_x = -screen.window_width() / 2
        left_bottom_y = -screen.window_height() / 2

        right_bottom_x = screen.window_width() / 2
        right_bottom_y = -screen.window_height() / 2

        left_top_x = -screen.window_width() / 2
        left_top_y = screen.window_height() / 2

        right_top_x = screen.window_width() / 2
        right_top_y = screen.window_height() / 2

        print(left_bottom_x)
        print(left_bottom_y)

        turtle.goto(left_top_x, left_top_y)

        screen.mainloop()


TurtleOOP()