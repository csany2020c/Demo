from turtle import *
from j_clock import *


class SampleClock:

    scr = Screen()
    clk = Clock(scr)

    secturtle = Turtle(shape="turtle")
    minturtle = Turtle(shape="turtle")
    hourturtle = Turtle(shape="turtle")

    def __init__(self):

        self.secturtle._delay(0)
        self.secturtle.speed(0)
        self.minturtle._delay(0)
        self.minturtle.speed(0)
        self.hourturtle._delay(0)
        self.hourturtle.speed(0)

        self.clk.setOnSecondChangeListener(self.writeSec)
        self.clk.setOnMinuteChangeListener(self.writeMin)
        self.clk.setOnHourChangeListener(self.writeHour)

        self.scr.mainloop()

    def printToConsole(self):
        print("Hour: " + str(self.clk.leftNumber(self.clk.hour24())) + "_" + str(self.clk.rightNumber(self.clk.hour24())))
        print("Minute: " + str(self.clk.leftNumber(self.clk.min())) + "_" + str(self.clk.rightNumber(self.clk.min())))
        print("Second: " + str(self.clk.leftNumber(self.clk.sec())) + "_" + str(self.clk.rightNumber(self.clk.sec())))
        return

    def writeSec(self):
        self.printToConsole()
        self.secturtle.clear()
        self.secturtle.reset()
        self.secturtle.penup()
        self.secturtle.setheading(90)
        self.secturtle.forward(200)
        self.secturtle.right(90 + 3)
        self.secturtle.pendown()
        for i in range(self.clk.sec()):
            self.secturtle.forward(20.943951023931954923084289221863)
            self.secturtle.right(6)
        self.secturtle.penup()

    def writeMin(self):
        self.minturtle.clear()
        self.minturtle.reset()
        self.minturtle.penup()
        self.minturtle.setheading(90)
        self.minturtle.forward(180)
        self.minturtle.right(90 + 3)
        self.minturtle.pendown()
        for i in range(self.clk.min()):
            self.minturtle.forward(18.849555921538759430775860299677)
            self.minturtle.right(6)
        self.minturtle.penup()

    def writeHour(self):
        self.hourturtle.clear()
        self.hourturtle.reset()
        self.hourturtle.penup()
        self.hourturtle.setheading(90)
        self.hourturtle.forward(160)
        self.hourturtle.right(90 + 3)
        self.hourturtle.pendown()
        for i in range(self.clk.hour12() * 6):
            self.hourturtle.forward(83.775804095727819692337156887453 / 6)
            self.hourturtle.right(30 / 6)
        self.hourturtle.penup()
