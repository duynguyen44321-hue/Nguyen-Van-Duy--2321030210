m = int(input("Nhap m = "))
n = int(input("Nhap n = "))
a = []

for i in range(0, m):
    a.append([])
    for j in range(0, n):
        k = float(input("Nhap ptu thu a[%d][%d]: " % (i + 1, j + 1)))
        a[i].append(k)

print("Mang vua nhap la: ")
for i in range(0, m):
    for j in range(0, n):
        print("%9.2f" % a[i][j], end=" ")
    print()
    print("Duy k68 Dia Tin Hoc")