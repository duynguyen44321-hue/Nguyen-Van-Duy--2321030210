# Mở file chứa ma trận để đọc
f = open("E:/matran.txt", "r")
ma = [dong.split() for dong in f]
f.close()

print("Ma trận đọc được là: ", ma)

s = 0
for subma in ma:
    for j in subma:
        s = s + float(j)

print("Tong cua ma tran la: ", s)