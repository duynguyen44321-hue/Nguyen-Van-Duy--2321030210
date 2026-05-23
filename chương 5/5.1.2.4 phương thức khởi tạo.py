import math
class circle:
    def __init__(self, radius=0):
        self.bk = radius
    def Dientich(self):
        return math.pi * self.bk * self.bk
c = circle()
c.Nhap()
print("Dtich của htron la : ", c.Dientich())