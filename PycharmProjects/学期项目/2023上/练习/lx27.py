import tkinter as tk
from random import choice

# 读取文件中的名字
with open("C:/Users/LL/Desktop/名字/未点.txt", "r", encoding="utf-8") as f:
    names = f.read()
n_list = names.split(",")
noroll_call = [name for name in n_list if name.strip()]  # 未点名名单，去除空值
with open("C:/Users/LL/Desktop/名字/已点.txt", "r", encoding="utf-8") as f:
    names = f.read()
n_list = names.split(",")
roll_call = [name for name in n_list if name.strip()]   # 已点名名单，去除空值


# 设定按钮函数
def onClick():
    global noroll_call
    global roll_call
    global name_lab
    if not noroll_call:  # 当未点名列表为空时，将未点名列表和已点名列表互换
        noroll_call, roll_call = roll_call, noroll_call
        if not noroll_call:  # 如果已点名列表也为空，则不进行操作
            return
    n = choice(noroll_call)
    noroll_call.remove(n)
    roll_call.append(n)
    name_lab["text"] = n  # 更新name_lab中文字内容
    # 保存已点名名单到文件
    with open("C:/Users/LL/Desktop/名字/已点.txt", "w", encoding="utf-8") as f:
        f.write(",".join(roll_call))
    # 保存未点名名单到文件
    with open("C:/Users/LL/Desktop/名字/未点.txt", "w", encoding="utf-8") as f:
        f.write(",".join(noroll_call))


root = tk.Tk()

root.geometry("840x580")
root.title("随机点名器")

name_lab = tk.Label(root, text="name", font=("微软雅黑", 100), pady=60)
name_lab.pack(side=tk.TOP)
roll_name = tk.Button(root, text="随机点名", font=("微软雅黑", 40), command=onClick)
roll_name.pack(side=tk.TOP)

root.mainloop()
