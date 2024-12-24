#https://luyencode.net/problem/thpttd_92
print("Loi input")

s = input()
so = []
so_ht = ""

for c in s:
    if c.isdigit():
        so_ht += c
    else:
        if so_ht:
            so.append(int(so_ht))
            so_ht = ""

if so_ht:
    so.append(int(so_ht))

so.sort()

kq = ""
vt = 0

for c in s:
    if c.isdigit():
        if vt < len(so):
            kq += str(so[vt])
            vt += 1
    else:
        kq += c

print(kq)
