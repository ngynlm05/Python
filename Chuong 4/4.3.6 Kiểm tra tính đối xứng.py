n = int(input())
A = []
for i in range(n):
    row = list(map(int, input().split()))
    A.append(row)

ktra = 1
for i in range(n):
    for j in range(n):
        if A[i][j] != A[j][i]:
            ktra = 0

if(ktra == 1):
    print("YES")
else:
    print("NO")