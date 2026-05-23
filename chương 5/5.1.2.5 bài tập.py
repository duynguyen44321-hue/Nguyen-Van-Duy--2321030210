
n = int(input("nhập số phần tử n: "))
while n <= 0 or n >= 100:
    n = int(input("Nhập lại n (0 < n < 100): "))

tong = 0
dem = 0
for i in range(n):
    x = float(input(f"Nhập ptu thu {i + 1}: "))
    if -1000 < x < -10:
        tong += x
        dem += 1
if dem > 0:
    tbc = tong / dem
    print("TBC cac ptu t/m la: ", tbc)
else:
    print("Khong co ptu nao t/m")