num2 = 0
num3 = 7.0
for i in range(1, 1000):
    num = 1.0 / float(num3)
    num2 = num2 + num
    num3 = num3 * 7
print(num2 + 1)
