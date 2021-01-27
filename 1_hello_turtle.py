from turtle import Turtle
from turtle import Screen


akvarium = Screen()
ametiszt = Turtle()
ametiszt.shape("turtle")
# for i in range(100):
#     ametiszt.forward(20)
#     ametiszt.left(57)
#     ametiszt.forward(40)
#     ametiszt.right(19)

ametiszt.color('red')
ametiszt.circle(100)

for i in range(180):
    ametiszt.forward(2)
    ametiszt.left(2)

akvarium.mainloop()
