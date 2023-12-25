# from math import sqrt
# while 1:
#     n = int(input("数:"))
#     print('%d=' % n, end="")
#     while 1:
#         for k in range(2, int(sqrt(n) + 1)):
#             if n % k == 0:
#                 print('%d*' % k, end="")
#                 n = int(n / k)
#                 break
#         else:
#             print(n)
#             break

while 1:
    n = int(input(f"数:"))
    print("%d=" % n, end="")
    while 1:
        for k in range(2, int(n + 1)):
            if n % k == 0:
                print("%d*" % k, end="")
                n = int(n / k)
                break
        else:
            print(n)
            break
