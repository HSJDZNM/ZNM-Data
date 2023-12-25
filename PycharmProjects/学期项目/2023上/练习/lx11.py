a = input("请输入一个数字:")
f = 0
for b in range(1, int(a) + 1):
    global f
    f += 1
    print(int(a) + int(f))
