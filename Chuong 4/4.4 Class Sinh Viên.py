class SinhVien:
    def Nhap(self):
        ThongTin = list(map(str, input().split()))
        self.Ten = ThongTin[0]
        self.Ma = int(ThongTin[1])
        self.Toan = float(ThongTin[2])
        self.Triet = float(ThongTin[3])
        self.Ltrc = float(ThongTin[4])

    def DiemTb(self):
        return (self.Toan + self.Triet + self.Ltrc) / 3

    def xuat(self):
        print(f"{self.Ma} {self.Ten} {self.Toan:.2f} {self.Triet:.2f} {self.Ltrc:.2f} {self.DiemTb():.2f}")

n = int(input("Nhap so luong sinh vien: "))
DS_SinhVien = []
for i in range(n):
    sinhvien = SinhVien()
    sinhvien.Nhap()
    DS_SinhVien.append(sinhvien)

print("Danh sach sinh vien hoc lai")
count = 0
for sinhvien in DS_SinhVien:
    check = 0
    if sinhvien.Toan < 4:
        check += 1
    if sinhvien.Triet < 4:
        check += 1
    if sinhvien.Ltrc < 4:
        check += 1
    if check >= 2:
        sinhvien.xuat()
        count += 1
print(f"Danh sach nay co {count} sinh vien phai hoc lai")
