def Binary(n):
    nhi_phan = []
    while n != 0:
        nhi_phan.append(n % 2)
        n //= 2
    for bit in reversed(nhi_phan):
        print(bit, end=" ")

def KQ(a, b):
    for i in range(a, b + 1):
        print(f"{i}: ", end="")
        Binary(i)
        print() 

a, b = map(int, input("Nhap a, b: ").split())
if a < b:
    KQ(a, b)
else:
    KQ(b, a)
