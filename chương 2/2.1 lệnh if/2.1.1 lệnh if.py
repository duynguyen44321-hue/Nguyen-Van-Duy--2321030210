a = float(input("Nhập số thứ nhất = "))
b = float(input("Nhập số thứ hai = "))
c = float(input("Nhập số thứ ba = "))

max = a

if (b > max):
    max = b

if (c > max):
    max = c

print("So lon nhat trong ba so %f, %f va %f la %f" % (a, b, c, max))