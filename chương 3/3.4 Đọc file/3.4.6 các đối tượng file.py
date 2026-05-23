# Tạo file foo.txt và ghi nội dung
fo = open("foo.txt", "w")
fo.write("python la mot ngon ngu lap trinh tuyet voi \nMinh cung nghi nhu the ! \n")
fo.close()
fo = open("foo.txt", "r")

print("Tên file là: ", fo.name)
print("File đã đóng chưa? ", fo.closed)
print("Chế độ mở file: ", fo.mode)

fo.close()