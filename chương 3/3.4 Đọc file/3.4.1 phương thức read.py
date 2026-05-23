# Mở file abcd.txt ở chế độ đọc ("r")
obj1 = open("abcd.txt", "r")
s1 = obj1.read()
print(s1)

obj1.close()