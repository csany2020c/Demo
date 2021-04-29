from j_segment import *

class Digit:
    A: Segment
    B: Segment
    C: Segment
    D: Segment
    E: Segment
    F: Segment
    G: Segment
    H: Segment

    def __init__(self, x: int, y: int, size: int):
        s = size * 0.80
        b = size / 25
        self.A = Segment(x + b, y + size * 2, 0, s)
        self.B = Segment(x + size, y + size * 2 - b, 270, s)
        self.C = Segment(x + size, y + b, 90, s)
        self.D = Segment(x + b, y, 0, s)
        self.E = Segment(x, y + b, 90, s)
        self.F = Segment(x, y + size * 2 - b, 270, s)
        self.G = Segment(x + b, y + size, 0, s)

    def _num0(self):
        self.A.set(True)
        self.B.set(True)
        self.C.set(True)
        self.D.set(True)
        self.E.set(True)
        self.F.set(True)
        self.G.set(False)

    def _num1(self):
        self.A.set(False)
        self.B.set(True)
        self.C.set(True)
        self.D.set(False)
        self.E.set(False)
        self.F.set(False)
        self.G.set(False)

    def _num2(self):
        self.A.set(True)
        self.B.set(True)
        self.C.set(False)
        self.D.set(True)
        self.E.set(True)
        self.F.set(False)
        self.G.set(True)

    def _num3(self):
        self.A.set(True)
        self.B.set(True)
        self.C.set(True)
        self.D.set(True)
        self.E.set(False)
        self.F.set(False)
        self.G.set(True)

    def _num4(self):
        self.A.set(False)
        self.B.set(True)
        self.C.set(True)
        self.D.set(False)
        self.E.set(False)
        self.F.set(True)
        self.G.set(True)

    def _num5(self):
        self.A.set(True)
        self.B.set(False)
        self.C.set(True)
        self.D.set(True)
        self.E.set(False)
        self.F.set(True)
        self.G.set(True)

    def _num6(self):
        self.A.set(True)
        self.B.set(False)
        self.C.set(True)
        self.D.set(True)
        self.E.set(True)
        self.F.set(True)
        self.G.set(True)

    def _num7(self):
        self.A.set(True)
        self.B.set(True)
        self.C.set(True)
        self.D.set(False)
        self.E.set(False)
        self.F.set(False)
        self.G.set(False)

    def _num8(self):
        self.A.set(True)
        self.B.set(True)
        self.C.set(True)
        self.D.set(True)
        self.E.set(True)
        self.F.set(True)
        self.G.set(True)

    def _num9(self):
        self.A.set(True)
        self.B.set(True)
        self.C.set(True)
        self.D.set(True)
        self.E.set(False)
        self.F.set(True)
        self.G.set(True)

    def setNum(self, num: int):
        if num == 0:
            self._num0()
            return
        if num == 1:
            self._num1()
            return
        if num == 2:
            self._num2()
            return
        if num == 3:
            self._num3()
            return
        if num == 4:
            self._num4()
            return
        if num == 5:
            self._num5()
            return
        if num == 6:
            self._num6()
            return
        if num == 7:
            self._num7()
            return
        if num == 8:
            self._num8()
            return
        if num == 9:
            self._num9()
            return


# d = Digit(x = 0, y = 0, size = 50)
# for i in range(10):
#     d.setNum(i)
# Digit(x = 100, y = 0, size = 60)
# Digit(x = 100, y = 190, size = 60)
# Screen().mainloop()