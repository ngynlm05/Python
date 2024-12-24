def Check(num) :
    if num <= 1 :
        return False
    for i in range (2, int(num**0.5) +1):
        if num % i == 0:
            return False 
    return True
def SNT(n):
    snt = []
    for i in range(2, n + 1):
        if Check(i):
            snt.append(i)
    return snt 

n = int(input("Nhap n: "))
kq = SNT(n)
print(f"Cac so nguyen to trong khoang (1, {n}): {kq}")

