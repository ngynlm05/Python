s = input().strip()

kyTu = s.split()

chuan_hoa = []

for word in kyTu:
    tu = word.capitalize()
    chuan_hoa.append(tu)

kq = ' '.join(chuan_hoa)
print(kq)
