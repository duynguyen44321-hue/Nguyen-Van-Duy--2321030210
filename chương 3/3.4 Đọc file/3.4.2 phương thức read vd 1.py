# Mở file để đọc (chế độ "r")
f = open("E:/dulieu.txt", "r")
s = f.read()
f.close() 

s = s.strip()       # Sửa từ 'ship' thành 'strip' để xóa khoảng trắng thừa ở đầu/cuối
a = s.split(" ")    # Cắt chuỗi thành danh sách dựa trên khoảng trắng
t = 0

print("Dãy số đọc được là: ", a)
for i in a:
    if i:  
        t = t + int(i)

print("Tổng của dãy số là: ", t)