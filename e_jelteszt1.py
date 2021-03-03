from e_szekreny import *
from e_jelek1 import *


turtle = Turtle()
screen = Screen()
turtle._delay(0)
turtle.speed(0)
j = Jel(turtle)
s = Szekreny(turtle)
s.polc()
j.focilabda()
screen.mainloop()