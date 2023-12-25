s = int(input('一个值:'))
d = int(input('几位数:'))
on = 0
while d:
    on = on + s
    s = s * 10
    print(on)
