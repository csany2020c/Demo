from turtle import Turtle
from turtle import Screen


akvarium = Screen()
ametiszt = Turtle()
ametiszt.shape("turtle")
for i in range(100):
    ametiszt.forward(20)
    ametiszt.left(57)
    ametiszt.forward(40)
    ametiszt.right(19)

akvarium.mainloop()
