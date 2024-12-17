s = input().strip()

tachSo = s.split(',')
chuSo = []

for So in tachSo:
    chuSo.append(int(So))

for So in chuSo:
    if So % 2 != 0:
        print(So)
