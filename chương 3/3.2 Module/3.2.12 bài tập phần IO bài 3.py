# 1. Nhập kích thước ma trận (m hàng, n cột)
m = int(input("nhập số hàng = "))
n = int(input("nhập số cột = "))
a = []

for i in range(0, m):
    a.append([])  # Thêm một hàng rỗng vào ma trận
    for j in range(0, n):
        x = float(input("Nhap pt thu a[%d][%d]: " % (i + 1, j + 1)))
        a[i].append(x)

obj = open("matran.txt", "w")

obj.write("Mang vua nhap la: \n")
for i in range(0, m):
    for j in range(0, n):
        # Chuyển số thực về chuỗi, thêm khoảng trắng giữa các số trên cùng một hàng
        obj.write(str(a[i][j]) + " ")
    obj.write("\n")  
obj.close()