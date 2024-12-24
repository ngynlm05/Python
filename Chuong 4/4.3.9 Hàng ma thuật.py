m, n = map(int, input().split())
A = []
for i in range(m):
    row = list(map(int, input().split()))
    A.append(row)

Hang_ma_thuat = []
for i in range(m):
    row_sum = sum(A[i])
    if row_sum % 7 == 0:
        Hang_ma_thuat.append(i + 1)

if Hang_ma_thuat:
    for row in Hang_ma_thuat:
        print(row)
else:
    print("NO")