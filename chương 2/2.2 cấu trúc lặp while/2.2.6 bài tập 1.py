tong = 0
while True:
    n = int(input("nhập số: "))
    if n == 0:
        break
    if n % 2 == 0:
        tong = tong + n

print("Tổng các số chẵn là: ", tong)