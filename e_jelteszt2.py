from e_szekreny import *
from e_jelek2 import *


turtle = Turtle()
screen = Screen()
# turtle._delay(0)
# turtle.speed(0)
s = Szekreny(turtle)
# s.polc()

s.polc()
j = Jel(turtle)
# j.mintajel()
j.ellipse(10,20,300,100)
j.mintajel()
s.polc()
j.kocsi()


# turtle.left(270)
# turtle.forward(200)
# s.polc()
screen.mainloop()