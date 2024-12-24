def SHH(n):
    s = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            s += i
    return s == n

def KQ(a, b):
    dem = 0
    for i in range(a, b + 1):
        if i > 0 and SHH(i):
            print(i, end=" ")
            dem += 1
    if dem == 0:
        print("Khong co")


a, b = map(int, input("Nhap a va b: ").split())

if a <= b:
    KQ(a, b)
else:
    KQ(b, a)
