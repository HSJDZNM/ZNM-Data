a = ("周杰伦", 11, ["football", "music"])
b = a.index(11)
print(b)

b = a[0]
print(b)

del a[2][0]
print(a)

a.insert(2, "coding")
print(a)
