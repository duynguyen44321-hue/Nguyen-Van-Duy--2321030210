# Hàm tính giai thừa
def tinh_giai_thua(so):
    ket_qua = 1
    for x in range(2, so + 1):
        ket_qua *= x
    return ket_qua

n = int(input("Nhập số cần tính giai thừa: "))
if n < 0:
    print("Không thể tính giai thừa của số âm")
else:
    print(f"Kết quả {n}! =", tinh_giai_thua(n))