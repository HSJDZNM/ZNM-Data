import tkinter as tk
import sqlite3
from random import choice

# 连接数据库
conn = sqlite3.connect('students.db')
c = conn.cursor()

# 从数据库读取名字
c.execute("SELECT name FROM students WHERE state=0")
rows = c.fetchall()
noroll_call = [row[0] for row in rows if row[0].strip()]  # 未点名名单，去除空值
students = [(row[0], 0) for row in rows]  # 学生列表

root = tk.Tk()

root.geometry("840x580")
root.title("随机点名器")

name_lab = tk.Label(root, text="name", font=("微软雅黑", 100), pady=60)
name_lab.pack(side=tk.TOP)

leftover_lab = tk.Label(root, text=", ".join(noroll_call), font=("微软雅黑", 20))
leftover_lab.pack(side=tk.TOP)

roll_call = []  # 已点名名单，初始为空


def onClick():
    global students
    global noroll_call
    global roll_call
    global name_lab
    global leftover_lab

    # 检查是否所有学生都已经点过名了，是则将所有state重置为0重新开始
    if all([s[1] for s in students]):
        students = [(s[0], 0) for s in students]

    # 从未点名学生中随机一个并将其state更新为1
    n = None
    while not n:
        s = choice(students)
        if s[1] == 0:
            n = s[0]
            students = [(s[0], s[1] if s[0] != n else 1) for s in students]

    # 更新界面显示
    name_lab["text"] = n
    roll_call.append(n)
    noroll_call = [s[0] for s in students if s[1] == 0]
    leftover_lab["text"] = ", ".join(noroll_call)


roll_name = tk.Button(root, text="随机点名", font=("微软雅黑", 40), command=onClick)
roll_name.pack(side=tk.TOP)

root.mainloop()

# 关闭数据库连接
conn.close()
