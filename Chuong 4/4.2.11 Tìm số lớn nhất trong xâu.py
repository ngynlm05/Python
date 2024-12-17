import re

s = input()
numbers = re.findall(r'\d+', s)

max_num = 0
if numbers:
    for num in numbers:
        int_num = int(num)
        if int_num > max_num:
            max_num = int_num

print(max_num)
