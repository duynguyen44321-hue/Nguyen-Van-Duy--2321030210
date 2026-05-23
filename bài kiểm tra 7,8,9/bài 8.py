x = int(input("Nhap x: "))
y = int(input("Nhap y: "))
z = int(input("Nhap z: "))

tich = x * y * z

print("Tich =", tich)

tich_str = str(tich)

so_chu_so = len(tich_str)

max_digit = tich_str[0]

for ch in tich_str:
    if ch > max_digit:
        max_digit = ch

print("So chu so cua tich =", so_chu_so)
print("Chu so lon nhat =", max_digit)