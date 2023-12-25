# 定义类
# class Car:
#     "这是定义车类"
#
#     def __init__(self, name):  # 定义构造方法
#         self.name = name
#
#     def getName(self):  # 定义方法
#         return self.name
#
#
# # 创造对象
# cl = Car("奔驰")
# print("这辆汽车的品牌:", cl.name)


# 定义类
class Student:
    chinese = 142
    maths = 1
    english = 141

    # 定义构造方法
    def __init__(self, name):
        self.name = name


# 创建对象
s1 = Student("马允")
print(s1.name + "的语文成绩:" + str(s1.chinese))
print(s1.name + "的数学成绩:" + str(Student.maths))
print(s1.name + "的英语成绩:" + str(s1.english))
print(s1.name)
