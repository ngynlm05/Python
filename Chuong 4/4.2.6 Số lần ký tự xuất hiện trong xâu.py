s = input().strip()

kq = []
dem = {}

for kyTu in s:
    if kyTu in dem:
        dem[kyTu] += 1
    else:
        dem[kyTu] = 1

for kyTu, count in dem.items():
    kq.append("'{}': {}".format(kyTu, count))

print(", ".join(kq))

