x = input()
i = 0
s = 0
k = 0
q = 0
for a in x:
    if a.isdigit():
        i += 1
    elif a.isalpha():
        s += 1
    elif a.isspace():
        k += 1
    else:
        q += 1
print(f"字符串:{s}_数字:{i}_空格{k}_符号{q}")