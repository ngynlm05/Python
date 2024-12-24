m, n, p = map(int, input("Nhap kich thuoc m, n, p: ").split())
# m x n, n x p
print("Nhap ma tran A:")
A = []
for i in range(m):
    row = list(map(int, input().split()))
    A.append(row)

print("Nhap ma tran B:")
B = []
for i in range(n):
    row = list(map(int, input().split()))
    B.append(row)

C = []
for i in range(m):
    row = []
    for j in range(p):
        row.append(0)
    C.append(row)

for i in range(m):
    for j in range(p):
        for k in range(n):
            C[i][j] += A[i][k] * B[k][j]

print("Ket qua nhan ma tran A x B la:")
for row in C:
    print(*row)
