num = int(input("输入一个整数:"))
print('{}='.format(num), end="")
if num % 1 != 0 or num <= 0:
    print("请输入一个整数!")
else:
    for i in range(2, num):
        if num % i == 0:
            print('{}*'.format(i), end="")
            i = num % i
            continue
        if num % i != 0:
            i = i + 1
            continue
        if num == i:
            print(i)
        else:
            print('{}'.format(i), end="")


