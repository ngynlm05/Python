m, n = map(int, input().split())

A = []
for i in range(m):
    row = list(map(int, input().split()))
    A.append(row)

B = 0
for i in range(m):
    for j in range(n):
        B += A[i][j]

TBC = round(B / (m * n), 2)
print(TBC)

for i in range(m):
    for j in range(n):
        if A[i][j] > TBC:
            print("{} {} {}".format(A[i][j], i + 1, j + 1))
