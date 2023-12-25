import tkinter as tk
import sqlite3

# 连接数据库，如果不存在则创建
conn = sqlite3.connect('students.db')
c = conn.cursor()

# 删除已存在的表
c.execute("DROP TABLE IF EXISTS students")

# 创建新表
c.execute('''CREATE TABLE students
             (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, state INT)''')

# 初始化学生列表
students = [('hk', 0), ('jk', 0), ('md', 0), ('yk', 0), ('zt', 0)]
c.executemany("INSERT INTO students (name, state) VALUES (?, ?)", students)
conn.commit()


# 从数据库读取所有学生
def get_students():
    c.execute("SELECT name FROM students")
    rows = c.fetchall()
    return [row[0] for row in rows]


# 添加一个学生到数据库
def add_student(name):
    c.execute("INSERT INTO students (name, state) VALUES (?, ?)", (name, 0))
    conn.commit()


# 从数据库中删除一个学生
def delete_student(name):
    c.execute("DELETE FROM students WHERE name=?", (name,))
    conn.commit()


# 设定添加按钮函数
def on_add():
    name = name_entry.get().strip()
    if name:
        add_student(name)
        students_listbox.delete(0, tk.END)
        students = get_students()
        for s in students:
            students_listbox.insert(tk.END, s)


# 设定删除按钮函数
def on_delete():
    name = students_listbox.get(tk.ACTIVE)
    if name:
        delete_student(name)
        students_listbox.delete(tk.ACTIVE)


# 从数据库读取所有学生
students = get_students()

root = tk.Tk()

root.geometry("400x500")
root.title("学生管理系统")

name_label = tk.Label(root, text="请输入学生姓名：")
name_label.pack()

name_entry = tk.Entry(root)
name_entry.pack()

add_button = tk.Button(root, text="添加", command=on_add)
add_button.pack()

delete_button = tk.Button(root, text="删除", command=on_delete)
delete_button.pack()

students_label = tk.Label(root, text="所有学生：")
students_label.pack()

students_listbox = tk.Listbox(root)
for s in students:
    students_listbox.insert(tk.END, s)
students_listbox.pack()

root.mainloop()

# 关闭数据库连接
conn.close()
