import re

s = input()
so = re.findall(r'\d+', s)

tong = 0
if so:
    for n in so:
        tong += int(n)

print(tong)
