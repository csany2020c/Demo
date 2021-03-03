from e_szekreny import *
from e_jelek2 import *

class Szekreny1(Szekreny):

    def szekreny(self, countx: int = 8, county: int = 2, width: int = 180, height: int = 240, depth: int = 20):
        startx = self.turtle.xcor()
        starty = self.turtle.ycor()
        jelrajzolo = Jel(self.turtle)
        i = 0
        for x in range(countx):
            for y in range(county):
                self.turtle.penup()
                self.turtle.goto(startx + x * (width + 10), starty + y * (height + 2))
                self.turtle.setheading(0)
                self.polc(width, height, depth)
                jelrajzolo.jel(i)
                i = i + 1
