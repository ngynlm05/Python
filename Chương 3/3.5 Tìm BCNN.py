a, b = map(int, input("Nhap a, b: ").split())
if a <= 0 or b <= 0:
    print("Du lieu sai")
else:
    LCM = a if a > b else b
    while True:
        if LCM % a == 0 and LCM % b == 0:
            break
        LCM += 1
    print(LCM)
