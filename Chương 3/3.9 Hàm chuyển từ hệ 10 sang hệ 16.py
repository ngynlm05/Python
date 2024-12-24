def dectohex(n):
    if n == 0:
        return "0"
    char = "0123456789ABCDEF"
    hex = ""
    while n > 0:
        hex = char[n % 16] + hex
        n = n // 16
    return hex

n = int(input())
print(dectohex(n))

# def dectohex(n):
#     if n == 0:
#         return "0x0"
#     char = "0123456789ABCDEF"
#     hex = ""
#     while n > 0:
#         hex = char[n % 16] + hex
#         n //= 16
#     return "0x" + hex
#
# n = int(input("Nhap so he 10: "))
# print(dectohex(n))
