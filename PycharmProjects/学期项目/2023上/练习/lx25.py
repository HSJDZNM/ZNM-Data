class People:
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def speak(self):
        print("%s说:我今年%d岁." % (self.name, self.age))


class Speaker:
    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print("我叫%s,是一名科学家,今天演讲的主题是%s." % (self.name, self.topic))


class Scientist(People, Speaker):
    def __init__(self, n, a, t):
        People.__init__(self, n, a)
        Speaker.__init__(self, n, t)


if __name__ == '__main__':
    Hawkin = Scientist("霍金", 50, "<<时间简历>>")
    Hawkin.speak()