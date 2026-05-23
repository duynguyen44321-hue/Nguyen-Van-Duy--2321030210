#Nhập vào một ma trận số nguyên kích thước 4 × 3 dưới dạng tuple, sau đó hiển thị ma trận theo từng hàng.((1,2,5),(4,5,6),(7,8,9),(10,11,12))
matrix = eval(input("Nhập ma trận 4x3 dưới dạng tuple: "))

print(*matrix[0])
print(*matrix[1])
print(*matrix[2])
print(*matrix[3])