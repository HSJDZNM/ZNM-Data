from sys import stdout
for j in range(2, 1001):
    list = []
    s = j
    n = -1
    for num in range(1, j):
        if j % num == 0:
            s -= num
            n += 1
            list.append(num)
    if s == 0:
        print(j)
        for i in range(n):
            stdout.write(str(list[i]))
            stdout.write(" ")
        print(list[n])
