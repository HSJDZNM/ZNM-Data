strs = "itheima itcast boxuequ"
cs = strs.count("it")
print(cs)
new_strs = strs.replace(" ", "|")
print(new_strs)
new_strs_list = new_strs.split("|")
print(new_strs_list)

dsb="sb沈佳锴 sb刘灿 sb王卓 sb王湘东"
index = 0
while index <= len(dsb):
    print(dsb[index])
    index += 1