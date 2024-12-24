import re

s = input()
so = re.findall(r'\d+', s)

max = 0
if so:
    for n in so:
        num = int(n)
        if num > max:
            max = num

print(max)
