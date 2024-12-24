def IntSum(n):
    s = 0
    dem = 0
    while n != 0:
        s += n % 10
        dem += 1
        n //= 10
    print(f"{dem} {s}")
n = int(input("Nhap n: "))
if n < 0:
    print("DL sai.")
else:
    IntSum(n)
