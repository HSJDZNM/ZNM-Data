import numpy as np
import matplotlib.pyplot as plt


# 函数f(x0,x1)=xo**2+x1**2
def fun2(x):
    return x[0] ** 2 + x[1] ** 2


# 该函数对NumPy数组x的各个元素求数值微分。
def numerical_gradient(f, x):
    h = 1e-4
    # grad初始化为0的array
    grad = np.zeros_like(x)
    for idx in range(x.size):
        # 获得输入array的值
        tmp_val = x[idx]
        # f(x+h)的计算
        x[idx] = tmp_val + h
        # 加0.0001后的x带入上面的fun2得到的值eg：25.00060001
        fxh1 = f(x)
        # f(x-h)的计算
        x[idx] = tmp_val - h
        fxh2 = f(x)
        # 计算分别两个值的微分，合起来(全部变量)就是grad[]向量就是梯度了
        grad[idx] = (fxh1 - fxh2) / (2 * h)
        x[idx] = tmp_val  # 还原值,因为前面-h，不然由于for循环保留了前一个的值，会影响结果的
    return grad


print(numerical_gradient(fun2, np.array([3.0, 4.0])))
print(numerical_gradient(fun2, np.array([0.0, 2.0])))

# import numpy as np
# import matplotlib.pyplot as plt
#
#
# def numerical_diff(f, x):
#     h = 1e-4
#     return (f(x + h) - f(x - h)) / (2 * h)
#
#
# def fun1(b):
#     return 0.01 * b ** 2 + 0.1 * b
#
#
# def tangent_line(f, x):
#     # d就是调用numerical_diff求得在x点的导数
#     d = numerical_diff(f, x)
#     # 这里直接y=kx+b求截距的，简单粗暴,y就是截距
#     y = f(x) - d * x
#     # 使用lambda匿名函数，t是形参，“：”后是要执行的函数表达式
#     return lambda t: d * t + y
#
#
# x = np.arange(0.0, 20.0, 0.1)
# y = fun1(x)
# plt.xlabel("x")
# plt.ylabel("f(x)")
# # 把函数作为形参时i，传入实参函数时，只要函数名即可，不用()
# tf = tangent_line(fun1, 10)
# # 因为tf返回的是lambda函数，所有要多调一次函数
# y2 = tf(x)
# plt.plot(x, y)
# plt.plot(x, y2)
# plt.show()
