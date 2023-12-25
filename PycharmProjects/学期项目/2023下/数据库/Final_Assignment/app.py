from flask import Flask, render_template
from pymysql import Connection
app = Flask(__name__)

@app.route('/')     # 路由
def Main_page():
    con = Connection(
        host="10.1.92.46",      # 数据库IP
        port=3306,              # 数据库使用端口
        user="root",            # 数据库用户名
        passwd="hk123" ,        # 数据库密码
        database="library",     # 选择使用的数据库
        charset="utf8mb4",      # 设置编码格式
        )
    try:
        cursor = con.cursor()       # 设置游标
        cursor.execute("SELECT * FROM books WHERE tag = '玄幻奇幻';")
        result = cursor.fetchall()      # 获取返回值
        # 查询到每个字段名
        columns = [col[0] for col in cursor.description]
        all_book_list = []
        for one in result:
            # 判断每一行的数据是不是已解码状态
            decoded_list = [element.decode('utf-8') if isinstance(element, bytes) else element for element in one]
            all_book_list.append(dict(zip(columns,decoded_list)))       # 做成列表套字典

    finally:
        con.close()
    # 调用模板，传入参数
    return render_template('Main_page.html',all_book_list=all_book_list)

@app.route('/Other/<tag>')     # 路由，有尖括号代表需要输入一个参数
def Other_novels(tag):
    con = Connection(
        host="10.1.92.46",
        port=3306, 
        user="root",
        passwd="hk123" ,
        database="library",
        charset="utf8mb4",
        )
    try:
        cursor = con.cursor()       # 设置游标
        cursor.execute(f"SELECT * FROM books WHERE tag = '{tag}';")
        result = cursor.fetchall()      # 获取返回值

        # 查询到每个字段名
        columns = [col[0] for col in cursor.description]
        all_book_list = []
        for one in result:
            # 判断每一行的数据是不是已解码状态
            decoded_list = [element.decode('utf-8') if isinstance(element, bytes) else element for element in one]
            all_book_list.append(dict(zip(columns,decoded_list)))       # 做成列表套字典

    finally:
        con.close()
    # 调用模板，传入参数
    return render_template('Main_page.html',all_book_list=all_book_list)

@app.route('/Novel/<book_id>')     # 路由，有尖括号代表需要输入一个参数
def Novel_catalogue(book_id):
    con = Connection(
        host="10.1.92.46",
        port=3306, 
        user="root",
        passwd="hk123" ,
        database="library",
        charset="utf8mb4",
        )
    try:
        cursor = con.cursor()       # 设置游标
        # 获取书名
        cursor.execute(f"SELECT book_name FROM books WHERE book_id = {book_id};")
        book_name = cursor.fetchall()      # 获取返回值
        # 获取章节名
        cursor.execute(f"SELECT title, chapter_id, chapter_num FROM book_content JOIN books ON book_content.book_name=books.book_name WHERE book_id = {book_id} ORDER BY chapter_num ASC;")
        chapter_name = cursor.fetchall()      # 获取返回值
        # 查章节页最大值
        cursor.execute(f"SELECT MAX(chapter_num) FROM book_content JOIN books ON books.book_name = book_content.book_name WHERE book_id = {book_id};")
        max_chapter_num = cursor.fetchall()      # 获取返回值


    finally:
        con.close()
    # 调用模板，传入参数
    return render_template('Novel catalogue.html', book_name=book_name, chapter_name=chapter_name , max_chapter_num=max_chapter_num)

@app.route('/Next/<id>')     # 路由，有尖括号代表需要输入一个参数
def Next_chapter(id):
    con = Connection(
        host="10.1.92.46",
        port=3306, 
        user="root",
        passwd="hk123",
        database="library",
        charset="utf8mb4",
        )
    try:
        # 找到章节名,内容,页数和下个页数
        cursor = con.cursor()       # 设置游标
        cursor.execute(f"SELECT title, content, chapter_num, book_name FROM book_content WHERE chapter_id = '{id}';")
        content_tuple = cursor.fetchall()
        title = content_tuple[0][0]                 # 这一章的标题
        content = content_tuple[0][1]               # 内容
        chapter_num = content_tuple[0][2]           # 找到当前页数
        book_name = content_tuple[0][3]             # 找到书名
        next_chapter_num = int(chapter_num)+1       # 下一章用的

        # 找到下一章的章节号
        cursor.execute(f"SELECT chapter_id FROM book_content WHERE chapter_num = '{next_chapter_num}' AND book_name = '{book_name}';")
        next_chapter_id = cursor.fetchall()

        # 找到书的编号(返回目录用的)
        cursor.execute(f"SELECT book_id FROM books JOIN book_content ON books.book_name = book_content.book_name WHERE chapter_id = {id};")
        book_id = cursor.fetchall()
        
    finally:
        con.close()
    # 调用模板，传入参数
    return render_template('Next chapter.html', title=title, content=content, book_id=book_id, next_chapter_id=next_chapter_id[0][0])

@app.route('/Two/<id>')     # 路由，有尖括号代表需要输入一个参数
def Two_chapters(id):
    con = Connection(
        host="10.1.92.46",
        port=3306, 
        user="root",
        passwd="hk123" ,
        database="library",
        charset="utf8mb4",
        )
    try:
        # 找到章节名,内容,页数和下个页数
        cursor = con.cursor()
        cursor.execute(f"SELECT title, content, chapter_num, book_name FROM book_content WHERE chapter_id = '{id}';")
        content_tuple = cursor.fetchall()
        title = content_tuple[0][0]                 # 这一章的标题
        content = content_tuple[0][1]               # 内容
        chapter_num = content_tuple[0][2]           # 找到当前页数
        book_name = content_tuple[0][3]             # 找到书名
        next_chapter_num = int(chapter_num)+1       # 下一章用的
        previous_chapter = int(chapter_num)-1       # 上一章用的

        # 找到下一章的章节号
        cursor.execute(f"SELECT chapter_id FROM book_content WHERE chapter_num = '{next_chapter_num}' AND book_name = '{book_name}';")
        next_chapter_id = cursor.fetchall()[0][0]

        # 找到上一章的章节号
        cursor.execute(f"SELECT chapter_id FROM book_content WHERE chapter_num = '{previous_chapter}' AND book_name = '{book_name}';")
        previous_chapter_id = cursor.fetchall()[0][0]

        # 找到书的编号(返回目录用的)
        cursor.execute(f"SELECT book_id FROM books JOIN book_content ON books.book_name = book_content.book_name WHERE chapter_id = {id};")
        book_id = cursor.fetchall()[0][0]

        # 找到章节号最大值
        cursor.execute(f"SELECT MAX(chapter_num) FROM book_content JOIN books ON books.book_name=book_content.book_name WHERE books.book_name = '{book_name}';")
        max_chapter_num = cursor.fetchall()[0][0]
        
    finally:
        con.close()
    # 调用模板，传入参数
    return render_template('Two chapters.html', title=title, content=content, book_id=book_id, next_chapter_id=next_chapter_id, chapter_num=chapter_num, previous_chapter_id=previous_chapter_id, max_chapter_num=int(max_chapter_num)-1)

@app.route('/Last/<id>')     # 路由，有尖括号代表需要输入一个参数
def Last_chapter(id):
    con = Connection(
        host="10.1.92.46",
        port=3306, 
        user="root",
        passwd="hk123",
        database="library",
        charset="utf8mb4",
        )
    try:
        # 找到章节名,内容,页数和下个页数
        cursor = con.cursor()       # 设置游标
        cursor.execute(f"SELECT title, content, chapter_num, book_name FROM book_content WHERE chapter_id = '{id}';")
        content_tuple = cursor.fetchall()
        title = content_tuple[0][0]                 # 这一章的标题
        content = content_tuple[0][1]               # 内容
        chapter_num = content_tuple[0][2]           # 找到当前页数
        book_name = content_tuple[0][3]             # 找到书名
        previous_chapter = int(chapter_num)-1       # 上一章用的

        # 找到下一章的章节号
        cursor.execute(f"SELECT chapter_id FROM book_content WHERE chapter_num = '{previous_chapter}' AND book_name = '{book_name}';")
        previous_chapter_id = cursor.fetchall()

        # 找到书的编号(返回目录用的)
        cursor.execute(f"SELECT book_id FROM books JOIN book_content ON books.book_name = book_content.book_name WHERE chapter_id = {id};")
        book_id = cursor.fetchall()
        
    finally:
        con.close()
    # 调用模板，传入参数
    return render_template('Last chapter.html', title=title, content=content, book_id=book_id, previous_chapter_id=previous_chapter_id[0][0])


if __name__ == '__main__':
    # 设置网站IP和开放端口
    app.run(host='10.1.92.46', port=5000, debug=True)