# file = open(r"datal.txt","rw")
# print("文件名字",file.name)
# print("访问模式",file.mode)
# print("是否已经关闭",file.closed)
# file.close()
# print("是否已关闭",file.closed)

with open(r"datal.txt", "w") as file:
    num = file.write("Go its own way , let others say!")
    print(f"寫入{num}個字符")
