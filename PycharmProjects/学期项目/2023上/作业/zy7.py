f1 = 1
f2 = 1
for i in range(1, 73):
    print('%d %d' % (f1, f2), end=" ")
    if (i % 3) == 0:
        print('')
    f1 = f1 + f2
    f2 = f1 + f2
