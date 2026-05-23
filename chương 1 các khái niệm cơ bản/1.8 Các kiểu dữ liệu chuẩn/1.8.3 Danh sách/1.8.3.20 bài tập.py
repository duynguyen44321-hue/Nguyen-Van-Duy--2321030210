# Bai tap Chuong 1 - Duy K68 Dia Tin Hoc
# De bai:
# Nhap vao cac so nguyen cach nhau boi dau cach.
# Chuyen thanh danh sach so nguyen.

S = input("Nhap vao cac so cach nhau boi dau cach: ")
chuoi_tach = S.split()
danh_sach_so = [int(x) for x in chuoi_tach]
print(danh_sach_so)
print("Duy K68 Dia Tin Hoc")