class Circle:
    def __init__(self, ban_kinh=0.0):
        self.bk = ban_kinh
    def nhap(self):
        self.bk = float(input("Nhập bán kính: "))
    def dien_tich(self):
        return 3.141592 * self.bk * self.bk
c1 = Circle(5.5)
print("Diện tích c1 là: ", c1.dien_tich())
c2 = Circle()
c2.nhap()
print("Diện tích c2 là: ", c2.dien_tich())