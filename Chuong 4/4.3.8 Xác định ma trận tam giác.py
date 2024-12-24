n = int(input())
A = []
for i in range(n):
    row = list(map(int, input().split()))
    A.append(row)

is_upper = True
for i in range(n):
    for j in range(i):
        if A[i][j] != 0:
            is_upper = False
            break
        if not is_upper:
            break

is_lower = True
for i in range(n):
    for j in range(i+1, n):
        if A[i][j] != 0:
            is_lower = False
            break
        if not is_lower:
            break

if is_upper:
    print("UPPER TRIANGLE")
elif is_lower:
    print("LOWER TRIANGLE")
else:
    print("NONE")