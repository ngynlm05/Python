import re

s = input().strip()
c = input().strip()

kq = re.sub(c, '', s)

print(kq)
