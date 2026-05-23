m = int(input("Nhap m (so nguyen duong): "))
while m <= 0:
    m = int(input("Nhap m (phai la so nguyen duong): "))

n = int(input("Nhap n (so nguyen duong): "))
while n <= 0:
    n = int(input("Nhap n (phai la so nguyen duong): "))

# Tinh tong cac chu so cua n bang cach dung phep chia va lay du
tong = 0
tmp = n
while tmp > 0:
    tong += tmp % 10
    tmp //= 10

print("Tong cac chu so cua n =", tong)

if m % tong == 0:
    print(m, "chia het cho", tong)
else:
    print(m, "khong chia het cho", tong)