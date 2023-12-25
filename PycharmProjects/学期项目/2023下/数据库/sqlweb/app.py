from flask import Flask, render_template
import pymysql
app = Flask(__name__)

@app.route('/')
def home():
    # 替换以下信息为你的数据库连接信息
    db_config = {
        'host': '10.1.78.81',
        'user': 'root',
        'password': '123456',
        'database': 'novel_website',
    }

    # 建立数据库连接
    connection = pymysql.connect(**db_config)

    try:
        # 创建一个游标对象
        with connection.cursor() as cursor:
            # 执行 SQL 查询
            sql = "SELECT * FROM Books inner join Authors on Books.AuthorID=Authors.AuthorID"
            cursor.execute(sql)

            # 获取查询结果
            result = cursor.fetchall()

            # 将结果转换成列表套字典的形式
            columns = [col[0] for col in cursor.description]
            data = [dict(zip(columns, row)) for row in result]

    finally:
        # 关闭数据库连接
        connection.close()
    return render_template("home.html", books=data)

@app.route('/author/<int:AuthorID>/')
def author(AuthorID):
    # 替换以下信息为你的数据库连接信息
    db_config = {
        'host': '10.1.78.81',
        'user': 'root',
        'password': '123456',
        'database': 'novel_website',
    }

    # 建立数据库连接
    connection = pymysql.connect(**db_config)

    try:
        # 创建一个游标对象
        with connection.cursor() as cursor:
            # 执行 SQL 查询
            sql = "SELECT * FROM Authors where AuthorID=%s" % AuthorID
            cursor.execute(sql)

            # 获取查询结果
            result = cursor.fetchall()
            result = result[0]
            author_name=result[1]
            author_description=result[2]

    finally:
        # 关闭数据库连接
        connection.close()    
    return render_template("author.html", author_name=author_name, author_description=author_description)

@app.route('/book/16/')
def stop():
    return render_template("stop.html")

@app.route('/book/<int:BookID>/')
def book(BookID):
    # 替换以下信息为你的数据库连接信息
    db_config = {
        'host': '10.1.78.81',
        'user': 'root',
        'password': '123456',
        'database': 'novel_website',
    }

    # 建立数据库连接
    connection = pymysql.connect(**db_config)

    try:
        # 创建一个游标对象
        with connection.cursor() as cursor:
            # 执行 SQL 查询
            sql = "SELECT BookTitle FROM Books where BookID=%s" % BookID
            cursor.execute(sql)
            result2 = cursor.fetchall()
            result2 = result2[0][0]
            sql = "SELECT ChapterID,ChapterTitle FROM Chapters where BookID=%s" % BookID
            cursor.execute(sql)
            result1 = cursor.fetchall()
            # 将结果转换成列表套字典的形式
            columns = [col[0] for col in cursor.description]
            data = [dict(zip(columns, row)) for row in result1]
    finally:
        # 关闭数据库连接
        connection.close()
    return render_template("catalogue.html", BookTitle=result2, chapters=data) 
    #return render_template("catalogue.html", BookTitle="原神", chapters=[{"ChapterID":"1", "ChapterTitle":"原神启动"}])

@app.route('/read/<int:ChapterID>/')
def read(ChapterID):
    # 替换以下信息为你的数据库连接信息
    db_config = {
        'host': '10.1.78.81',
        'user': 'root',
        'password': '123456',
        'database': 'novel_website',
    }

    # 建立数据库连接
    connection = pymysql.connect(**db_config)

    try:
        # 创建一个游标对象
        with connection.cursor() as cursor:
            sql = "SELECT ChapterTitle,content FROM Chapters where ChapterID=%s" % ChapterID
            cursor.execute(sql)
            result1 = cursor.fetchall()
            ChapterTitle=result1[0][0]
            content=result1[0][1]

    finally:
        # 关闭数据库连接
        connection.close()
    return render_template("read.html", ChapterTitle=ChapterTitle, content=content)


if __name__ == "__main__":
    app.run(debug=True) 

