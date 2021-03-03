from turtle import Turtle
from turtle import Screen
from random import Random

class TurtleOOP:
    # turtle = Turtle()
    #screen = Screen()

    def __init__(self):
        r = Random()
        for i in range(200):
            # print(r.randint(1, 10))
            print(r.random() * 10 + 1)

t = TurtleOOP()
