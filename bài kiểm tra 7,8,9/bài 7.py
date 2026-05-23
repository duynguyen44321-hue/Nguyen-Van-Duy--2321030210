# Hàm kiểm tra số nguyên tố
def kiem_tra_so_nt(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


n = int(input("Nhap n: "))

tong = 0

for i in range(n):
    x = int(input("Nhap so thu " + str(i + 1) + ": "))

    if kiem_tra_so_nt(x) == True:
        tong = tong + x

print("Tong cac so nguyen to =", tong)

if tong > 50 and tong % 2 != 0:
    print("Tong la so le va lon hon 50")
else:
    print("Tong khong thoa man dieu kien")