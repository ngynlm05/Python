class Sach:
    def Nhap(self):
        self.Ten = input("Nhap ten sach: ")
        self.SoTrang = int(input("So trang: "))
        self.GiaTien = int(input("Gia tien: "))

    def GiaTb(self):
        return self.GiaTien / self.SoTrang if self.SoTrang != 0 else 0

    def xuat(self):
        print(
            f"Sach: {self.Ten}, {self.SoTrang} trang, gia {self.GiaTien}d, gia trung binh/trang la {self.GiaTb():.2f}d.")

n = int(input("Nhap so luong sach: "))
DS_Sach = []
for i in range(n):
    sach = Sach()
    sach.Nhap()
    DS_Sach.append(sach)

DS_Sach.sort(key=lambda x: x.GiaTb(), reverse=True)

for sach in DS_Sach:
    sach.xuat()
