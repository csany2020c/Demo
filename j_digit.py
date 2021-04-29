from j_segment import *

class Digit:
    _A: Segment
    _B: Segment
    _C: Segment
    _D: Segment
    _E: Segment
    _F: Segment
    _G: Segment

    def __init__(self, x: int, y: int, size: int):
        s = size * 0.80
        b = size / 25
        self._A = Segment(x + b, y + size * 2, 0, s)
        self._B = Segment(x + size, y + size * 2 - b, 270, s)
        self._C = Segment(x + size, y + b, 90, s)
        self._D = Segment(x + b, y, 0, s)
        self._E = Segment(x, y + b, 90, s)
        self._F = Segment(x, y + size * 2 - b, 270, s)
        self._G = Segment(x + b, y + size, 0, s)

    def _num0(self):
        self._A.set(True)
        self._B.set(True)
        self._C.set(True)
        self._D.set(True)
        self._E.set(True)
        self._F.set(True)
        self._G.set(False)

    def _num1(self):
        self._A.set(False)
        self._B.set(True)
        self._C.set(True)
        self._D.set(False)
        self._E.set(False)
        self._F.set(False)
        self._G.set(False)

    def _num2(self):
        self._A.set(True)
        self._B.set(True)
        self._C.set(False)
        self._D.set(True)
        self._E.set(True)
        self._F.set(False)
        self._G.set(True)

    def _num3(self):
        self._A.set(True)
        self._B.set(True)
        self._C.set(True)
        self._D.set(True)
        self._E.set(False)
        self._F.set(False)
        self._G.set(True)

    def _num4(self):
        self._A.set(False)
        self._B.set(True)
        self._C.set(True)
        self._D.set(False)
        self._E.set(False)
        self._F.set(True)
        self._G.set(True)

    def _num5(self):
        self._A.set(True)
        self._B.set(False)
        self._C.set(True)
        self._D.set(True)
        self._E.set(False)
        self._F.set(True)
        self._G.set(True)

    def _num6(self):
        self._A.set(True)
        self._B.set(False)
        self._C.set(True)
        self._D.set(True)
        self._E.set(True)
        self._F.set(True)
        self._G.set(True)

    def _num7(self):
        self._A.set(True)
        self._B.set(True)
        self._C.set(True)
        self._D.set(False)
        self._E.set(False)
        self._F.set(False)
        self._G.set(False)

    def _num8(self):
        self._A.set(True)
        self._B.set(True)
        self._C.set(True)
        self._D.set(True)
        self._E.set(True)
        self._F.set(True)
        self._G.set(True)

    def _num9(self):
        self._A.set(True)
        self._B.set(True)
        self._C.set(True)
        self._D.set(True)
        self._E.set(False)
        self._F.set(True)
        self._G.set(True)

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
# d.setNum(2)
# d2 = Digit(x = 100, y = 0, size = 100)
# d2.setNum(7)
# Screen().mainloop()