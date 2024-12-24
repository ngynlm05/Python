class Sach:
    def __init__(self, ten, so_trang, gia_tien):
        self.Ten = ten
        self.SoTrang = so_trang
        self.GiaTien = gia_tien

    def xuat(self):
        return f"{self.Ten} {self.SoTrang} {self.GiaTien}"

ds_sach = []
with open("sach.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        thongtin = line.strip().split()
        ten = thongtin[0]
        so_trang = int(thongtin[1])
        gia_tien = int(thongtin[2])
        sach = Sach(ten, so_trang, gia_tien)
        ds_sach.append(sach)

with open("ketqua.txt", "w") as f:
    for sach in ds_sach:
        if sach.GiaTien > 100000 and sach.SoTrang < 200:
            f.write(f"{sach.xuat()}\n")

print("Da ghi du lieu vao ketqua.txt.")
