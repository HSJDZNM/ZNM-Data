class Model:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def left_foot_forward(self):
        print('左脚向前')

    def right_foot_forward(self):
        print('右脚向前')

    def left_foot_backward(self):
        print('左脚向后')

    def right_foot_backward(self):
        print('右脚向后')


class Giraffes(Model):
    def find_food(self):
        self.left_foot_forward()    # 左脚向前移动
        self.left_foot_forward()    # 再次左脚向前移动
        self.right_foot_forward()   # 右脚向前移动
        self.left_foot_backward()   # 左脚向后移动
        self.right_foot_forward()   # 右脚向前移动


giraffe = Giraffes('Gerald', 18)   # 创建一个名为'Gerald'、身高为18的长颈鹿对象
giraffe.find_food()                # 调用长颈鹿对象的find_food方法
