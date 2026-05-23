n = int(input("Nhap n: "))
tong = 0
dem = 0
for i in range(n):
    x = float(input("Nhap x: "))
    
    if x > 0 and x < 1000:
        tong = tong + x
        dem = dem + 1
if dem > 0:
    tbc = tong / dem
    print("Trung binh cong =", tbc)
else:
    print("Khong co so thoa man")