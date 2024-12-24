def GCD(a, b):
    while a != b:
        if a < b:
            b -= a
        else:
            a -= b
    return a


x, y, z = map(int, input("Nhap x, y, z ").split())
if x > 0 and y > 0 and z > 0:
    print(GCD(x, GCD(y, z)))
else:
    print("DL sai.")
