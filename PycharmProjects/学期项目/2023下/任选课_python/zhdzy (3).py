from flask import Flask, render_template
import pymysql

db = pymysql.connect(
    host='localhost',
    user='root',
    password='Mt25821682',
    database='novel_website'
)

cursor = db.cursor()
cursor.execute("SELECT * FROM novels")
other_data = cursor.fetchall()
other_results = []
for row in other_data:
        # 处理第二个表的数据，并添加到结果列表中
        # 示例代码：
        other_result = {
            'id': row[0],
            'name': row[1],
        }
        other_results.append(other_result)
print(type(other_result['id']))


