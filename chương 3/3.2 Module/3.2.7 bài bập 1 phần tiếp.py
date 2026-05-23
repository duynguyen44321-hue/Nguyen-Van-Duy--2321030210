from tinh import *

chieu_dai = int(input("chieu dai hcn la: "))
chieu_rong = int(input("chieu rong hcn la: "))

print("dien tich hcn la: ", dien_tich_hcn(chieu_dai, chieu_rong))
print("chu vi hcn la: ", chu_vi_hcn(chieu_dai, chieu_rong))

ban_kinh = int(input("ban kinh hinh tron la: "))
print("dien tich hinh tron la: ", dien_tich_hinh_tron(ban_kinh))

canh = int(input("nhap canh hinh vuong: "))
print("dien tich hinh vuong: ", dien_tich_hinh_vuong(canh))