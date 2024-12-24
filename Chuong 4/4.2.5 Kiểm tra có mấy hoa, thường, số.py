s = input().strip()

VietHoa = 0
VietThuong = 0
So = 0

for char in s:
    if char.isupper():
        VietHoa += 1
    elif char.islower():
        VietThuong += 1
    elif char.isdigit():
        So += 1

print(f"Viet hoa: {VietHoa}")
print(f"Viet thuong: {VietThuong}")
print(f"So: {So}")
