T = int(input())
for _ in range(T):
    s = input()
    result = ''
    count = 1
    for i in range(1, len(s) + 1):
        if i < len(s) and s[i] == s[i-1]:
            count += 1
        else:
            result += s[i-1] + str(count)
            count = 1
    print(result)

# s = input()
# total = 0
# current_num = ""
# for char in s:
#     if char.isdigit():
#         current_num += char
#     else:
#         if current_num:
#             total += int(current_num)
#             current_num = ""
#
# if current_num:
#     total += int(current_num)
# print(total)