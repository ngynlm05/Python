T = int(input())
for _ in range(T):
    s = input()
    kq = ''
    dem = 1
    for i in range(1, len(s) + 1):
        if i < len(s) and s[i] == s[i-1]:
            dem += 1
        else:
            kq += s[i - 1] + str(dem)
            dem = 1
    print(kq)

# s = input()
# tong = 0
# so_ht = ""
# for c in s:
#     if c.isdigit():
#         so_ht += c
#     else:
#         if so_ht:
#             tong += int(so_ht)
#             so_ht = ""
#
# if so_ht:
#     tong += int(so_ht)
# print(tong)