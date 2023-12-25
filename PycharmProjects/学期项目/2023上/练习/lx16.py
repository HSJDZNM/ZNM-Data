a = int(input("数:"))
b = a
i = int(input("次数:"))
num = 0
for x in range(i):
    num = a + num
    a = a * 10 + b

print(num)