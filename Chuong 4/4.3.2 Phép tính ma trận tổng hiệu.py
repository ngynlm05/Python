m, n = map(int, input().split())

A = []
for i in range(m):
    A.append(list(map(int, input().split())))

B = []
for i in range(m):
    B.append(list(map(int, input().split())))

C = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(A[i][j] + B[i][j])
    C.append(row)

D = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(A[i][j] - B[i][j])
    D.append(row)

for row in C:
    print(' '.join(map(str, row)))

for row in D:
    print(' '.join(map(str, row)))
