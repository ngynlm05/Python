m, n = map(int, input().split())

A = []
for i in range(m):
    row = list(map(int, input().split()))
    A.append(row)

B = []
for i in range(m):
    row = list(map(int, input().split()))
    B.append(row)

C = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(A[i][j] + B[i][j])
    C.append(row)

for i in range(m):
    for j in range(n):
        print("{}".format(C[i][j]), end=" ")
    print("")
