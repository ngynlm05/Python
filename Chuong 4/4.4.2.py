class Sach:
    def Nhap(self):
        thongtin = list(map(str, input().split()))
        self.Ten = thongtin[0]
        self.SoTrang = int(thongtin[1])
        self.GiaTien = int(thongtin[2])

    def GiaTb(self):
        return self.GiaTien / self.SoTrang if self.SoTrang != 0 else 0

    def xuat(self):
        print(f"{self.Ten} {self.SoTrang} {self.GiaTien} {self.GiaTb():.2f}")

n = int(input("Nhap so luong sach: "))
ds_sach = []
for i in range(n):
    sach = Sach()
    sach.Nhap()
    ds_sach.append(sach)

ds_sach.sort(key=lambda x: (x.GiaTb(), x.Ten))

with open("sach.txt", "w") as f:
    for sach in ds_sach:
        f.write(f"{sach.Ten} {sach.SoTrang} {sach.GiaTien} {sach.GiaTb():.2f}\n")

print("Da ghi du lieu vao sach.txt.")
