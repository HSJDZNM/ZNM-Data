i = 0
h = 100.0
for fre in range(10):
    i = i + h
    h = h/2
    i = i + h
print("第十次反弹:" + str(h))
print("共经过:" + str(i))