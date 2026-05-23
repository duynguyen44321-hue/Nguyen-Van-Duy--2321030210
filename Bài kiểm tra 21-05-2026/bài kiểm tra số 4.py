a = int(input("Nhap a: "))
b = int(input("Nhap b: "))

tong = a + b

print("Tong =", tong)

max = 0

for i in range(len(str(tong))):
    so = int(str(tong)[i])
    
    if so > max:
        maxx = so

print("Chu so lon nhat =", max)