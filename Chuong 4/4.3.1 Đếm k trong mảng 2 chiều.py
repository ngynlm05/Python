m, n, k = map(int, input().split())
dem = 0
for i in range(m):
    hang = list(map(int, input().split()))
    dem += hang.count(k)
print(dem)