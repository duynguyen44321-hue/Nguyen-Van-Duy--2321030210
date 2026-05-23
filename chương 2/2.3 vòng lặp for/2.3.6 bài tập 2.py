
n = int(input("nhập số phần tử của dãy số: "))

a = []

for i in range(1, n + 1):
    k = int(input("nhập phần tử thứ " + str(i) + ": "))
    a.append(k)

print("Lũy thừa 2 của các phần tử trong dãy là:")
for i in a:
    luy_thua_2 = i ** 2  # Trong Python, toán tử ** dùng để tính lũy thừa
    print(luy_thua_2)