# 1. Nhập vào một số nguyên n
n = int(input("n = "))
s = 0

for i in range(1, n):
    if n % i == 0:
        s = s + i  # Cộng dồn ước số vào tổng s
if s == n:
    print(n, "là số hoàn hảo")
else:
    print(n, "không là số hoàn hảo")