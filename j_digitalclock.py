from j_clock import *
from j_digit import *
class Digitalclock:
    screen = Screen()
    clk: Clock
    hl: Digit
    hr: Digit
    ml: Digit
    mr: Digit
    sl: Digit
    sr: Digit

    def __init__(self, x: int, y: int, size: int):
        self.clk = Clock(self.screen)
        s = size * 1.4
        self.hl = Digit(x, y, size)
        self.hr = Digit(x  + s, y, size)
        self.ml = Digit(x + s * 2 + size / 2, y, size)
        self.mr = Digit(x + s * 3 + size / 2, y, size)
        self.sl = Digit(x + s * 4 + size, y, size)
        self.sr = Digit(x + s * 5 + size, y, size)
        self.clk.setOnSecondChangeListener(self._change)

    def _change(self):
        self.sr.setNum(self.clk.rightNumber(self.clk.sec()))
        self.sl.setNum(self.clk.leftNumber(self.clk.sec()))
        self.mr.setNum(self.clk.rightNumber(self.clk.min()))
        self.ml.setNum(self.clk.leftNumber(self.clk.min()))
        self.hr.setNum(self.clk.rightNumber(self.clk.hour24()))
        self.hl.setNum(self.clk.leftNumber(self.clk.hour24()))


# Digitalclock(0,0,50)
# Screen().mainloop()