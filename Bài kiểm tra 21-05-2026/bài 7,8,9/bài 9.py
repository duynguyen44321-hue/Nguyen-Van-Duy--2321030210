a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
c = int(input("Nhap c: "))

tong = a + b + c

print("Tong =", tong)

tong_str = str(tong)
dem = 0

for i in range(len(tong_str)):
    chu_so = int(tong_str[i])

    if chu_so % 2 == 0:
        dem = dem + 1

print("So chu so chan trong tong =", dem)