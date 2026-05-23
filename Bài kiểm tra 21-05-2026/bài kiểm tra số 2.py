n = abs(int(input("Nhap n: ")))

tong = sum(int(chu_so) for chu_so in str(n))
print("Tong cac chu so =", tong)
print("Tong chia het cho 3" if tong % 3 == 0 else "Tong khong chia het cho 3") 