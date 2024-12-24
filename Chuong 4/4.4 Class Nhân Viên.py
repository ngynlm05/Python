class NhanVien:
    def Nhap(self):
        thongtin = list(map(str, input().split()))
        self.MaSo = int(thongtin[0])
        self.Ten = thongtin[1]
        self.HeSoLuong = float(thongtin[2])
        self.PhuCap = int(thongtin[3])

    def Luong(self):
        return self.HeSoLuong * 2000000 + self.PhuCap

    def xuat(self):
        print(f"{self.MaSo} {self.Ten} {self.HeSoLuong:.2f} {self.PhuCap} {self.Luong():.0f}")

n = int(input("Nhap so luong nhan vien: "))
DS_NhanVien = []
for i in range(n):
    nhanvien = NhanVien()
    nhanvien.Nhap()
    DS_NhanVien.append(nhanvien)

DS_NhanVien.sort(key=lambda x: x.Luong(), reverse=True)

print("Nhan vien co luong thap nhat:")
DS_NhanVien[-1].xuat()

print("Danh sach nhan vien da sap xep (luong thang giam dan):")
for nhanvien in DS_NhanVien:
    nhanvien.xuat()
