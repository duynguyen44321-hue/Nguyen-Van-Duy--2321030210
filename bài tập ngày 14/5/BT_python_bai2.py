# Bai tap Python
# De bai:
# Viet chuong trinh nhap vao mot day so nguyen x1, x2, ..., xn (0 < n < 200),
# tinh tong cac phan tu chan trong day,
# va kiem tra xem tong nay co chia het cho 7
# va nho hon 200 hay khong.

# Nhập số phần tử
n = int(input("Nhap n: "))

tong = 0

for i in range(n):
    x = int(input(f"Nhap x{i+1}: "))
    
    if x % 2 == 0:
        tong += x

print("Tong cac phan tu chan =", tong)

if tong % 7 == 0 and tong < 200:
    print("Tong chia het cho 7 va nho hon 200")
else:
    print("Tong khong thoa man dieu kien")