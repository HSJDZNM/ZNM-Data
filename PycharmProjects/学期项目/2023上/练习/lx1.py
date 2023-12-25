sy = [[1, 2, 3, 4], [5, 6, 7, 8]]
print(f"{sy[1][3]}")

del sy[1]
# 无法接收删除信息
print(sy)

o = sy.pop(0)
# 可以接收删除信息
print(sy)
print(f"删掉的东西是：{o}")

sy.insert(1, 666)
# 插入的表格.insert（下标索，内容）
print(sy)

sy.append("我测你码")
# 尾部插入一个新内容（单个
print(sy)

m = ["大家，看我看我", "我宣布个事", "我是SB!!!"]
# 尾部加入一个新表格（多个内容
sy.extend(m)
print(sy)

sy[1] = "算了，不测了"
# 插入：表格【下标索】=内容
sy[2] = "大家别看我"
sy[3] = "不是我宣布事"
sy[4] = "我不是SB!!!"
print(sy)

sy.insert(1, "后面都是刘C说的【doge】")
print(sy)

sy.insert(4, "是刘C宣布的,他是SB!!")
sy.insert(5, "刘C:")
sy.insert(6, 666)

cs = sy.count(666)
print(f"本列表含'666'的元素有{cs}个")
cs2 = len(sy)
print(f"此列表有个{cs2}元素")

print(f"清除列表后,列表为:")
sy.clear()
# 清除表格所有内容
print(sy)

sy.append(54188)
num = sy.index(54188)

print(f"{num}")

sy.remove(54188)
print(sy)
