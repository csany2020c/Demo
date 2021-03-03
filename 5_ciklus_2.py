from turtle import Turtle
from turtle import Screen


class TurtleOOP:
    def __init__(self):
        screen = Screen()
        screen.setup(width=640, height=480)
        turtle = Turtle()

        # turtle._delay(0)
        # turtle.speed(0)

        left_bottom_x = -screen.window_width() / 2
        left_bottom_y = -screen.window_height() / 2

        right_bottom_x = screen.window_width() / 2
        right_bottom_y = -screen.window_height() / 2

        left_top_x = -screen.window_width() / 2
        left_top_y = screen.window_height() / 2

        right_top_x = screen.window_width() / 2
        right_top_y = screen.window_height() / 2

        # turtle.goto(left_top_x, left_top_y)
        # turtle.goto(right_bottom_x, right_bottom_y)
        # turtle.goto(0,0)
        # turtle.goto(left_bottom_x, left_bottom_y)
        # turtle.goto(right_top_x, right_top_y)
        # turtle.goto(0,0)

        for y in range(10, 101, 10):
            turtle.penup()

            turtle.goto(left_top_x, left_top_y - y)

            turtle.pendown()
            turtle.goto(right_top_x, right_top_y - y)

        screen.mainloop()


TurtleOOP()