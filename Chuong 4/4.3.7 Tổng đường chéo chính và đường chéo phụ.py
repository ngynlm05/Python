n = int(input())
A = []
for i in range(n):
    row = list(map(int, input().split()))
    A.append(row)
DCC = 0
DCP = 0
for i in range(n):
    DCC += A[i][i]
    DCP += A[i][n - i - 1]

print("DCC= {}, DCP= {}".format(DCC, DCP))