import re

s = input()
numbers = re.findall(r'\d+', s)

tong = 0
if numbers:
    for num in numbers:
        tong += int(num)

print(tong)
