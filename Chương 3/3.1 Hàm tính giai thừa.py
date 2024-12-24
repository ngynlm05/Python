def giai_thua(n):
    if n < 0:
        return
    elif n == 0 or n == 1:
        return 1
    else:
        gt = 1
        for i in range(2, n + 1):  
            gt *= i
        return gt

n = input("Nhap n: ")

if n.isdigit():
    n = int(n)
    ket_qua = giai_thua(n)
    print(f"Giai thua cua {n} la: {ket_qua}")
else:
    print("Loi, nhap lai")
