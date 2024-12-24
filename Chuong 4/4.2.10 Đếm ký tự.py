# https://lqdoj.edu.vn/problem/countchar
print("Time Limit Exceeded")

N, Q = map(int, input().split())
S = input()

for _ in range(Q):
    L, R, C = input().split()
    L, R = int(L), int(R)
    kq = S[L - 1:R].count(C)
    print(kq)