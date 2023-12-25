num1 = 2.0
num2 = 1.0
num5 = 0
for i in range(19):
    num1, num2 = num1 + num2, num1
    num4 = num1 / num2
    num5 = num5 + num4
print(num5 + 2)
