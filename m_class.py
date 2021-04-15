from turtle import *


class Mouse:

    color: str
    name: str
    speed: int
    turtle: Turtle
    live: bool = True

    def __init__(self, name: str, color: str, image: str = "m_jerry.gif"):
        print("Megszületett " + name + ".")
        self.name = name
        self.color = color
        self.turtle = Turtle()
        self.turtle.getscreen().addshape(image)
        self.turtle.shape(image)

    def __str__(self):
        return "My name is " + self.name


class Cat:

    color: str
    mouseCount: int = 0
    name: str
    turtle: Turtle

    def __init__(self, name: str, color: str, image: str = "m_tom.gif"):
        self.name = name
        self.color = color
        self.turtle = Turtle()
        self.turtle.getscreen().addshape(image)
        self.turtle.shape(image)
        self.turtle.speed(1)

    def __str__(self):
        return "My name is " + self.name

    def eat(self, m: Mouse):
        if m.live:
            self.mouseCount = self.mouseCount + 1
            self.turtle.goto(m.turtle.xcor(), m.turtle.ycor())
            m.live = False
        else:
            print(self.name + " nem tudta megenni az egeret.")

Jerry: Mouse
Jerry = Mouse(name="Jerry", color="Brown")
Hg = Mouse(name="Hógolyó", color="white")
Tom = Cat(name="Tom", color="Gray and blue")
Garfield = Cat(name="Garfield", color="Orange", image="m_garfield.gif")

print(Tom)
print(Garfield)
print(Jerry)

Jerry.turtle.goto(300,300)
Hg.turtle.goto(-300,-300)

Tom.eat(Jerry)
Tom.eat(Hg)
Garfield.eat(Jerry)

print(Garfield.mouseCount)

Screen().mainloop()