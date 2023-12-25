zhi = input("输入字符串:")
astr = 0
anum = 0
akong = 0
afuhao = 0
for i in range(len(zhi)):
    if zhi.isdigit():
        anum += 1
    if zhi.isalpha():
        astr += 1
    if zhi.split():
        akong += 1
    else:
        afuhao += 1
print("数字有:"+str(anum)+"字符串有:"+str(astr)+"空格有:" + str(akong) + "符号有:"+str(afuhao))
