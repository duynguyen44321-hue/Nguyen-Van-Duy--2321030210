a = []
n = int(input("nhập số phần tử của dãy số: "))

for i in range(1, n + 1):
    k = int(input("Nhập phần tử thứ " + str(i) + ": "))
    a.append(k)

# Mở file ở ổ đĩa E để ghi
obj = open("E:/dulieu.txt", "w")
for i in a:
    obj.write(str(i) + " ")
obj.close()