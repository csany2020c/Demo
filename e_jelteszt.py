from e_jelek import *


turtle = Turtle()
screen = Screen()
turtle._delay(0)
turtle.speed(0)
j = Jel(turtle)
s = Szekreny(turtle)
s.polc()
turtle.penup()
turtle.left(180)
turtle.forward(55)
turtle.left(90)
turtle.forward(60)
turtle.left(90)

turtle.pendown()
j.haziko()
screen.mainloop()