# 1
# a = abs(10)+abs(-10)
# print(a)
# b=abs(-10) + -10
# print(b)

import shutil

def copy_file(source, destination):
    try:
        shutil.copy(source, destination)
        print("文件拷贝成功！")
    except FileNotFoundError:
        print("源文件不存在，请检查路径是否正确。")
    except PermissionError:
        print("目标文件无法访问，请检查权限设置。")
    except Exception as e: 
        print("发生了一个错误：", e)

# 源文件路径
source_file = "G:/python/app.py"

# 目标文件路径
destination_file = "G:/数据库"


