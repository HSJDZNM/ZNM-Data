import traceback
import requests
from bs4 import BeautifulSoup
import os
import re
import concurrent.futures
import multiprocessing
import time

class PC:
    def __init__(self, root_url, dir_num):
        self.root_url = root_url
        self.book_list = []
        self.url_list_tow = []
        self.home_page = []
        self.dir_num = dir_num

    def get_url(self, url, headers):
        while True:
            try:
                res = requests.get(url, headers=headers)
                if res.status_code == 200:
                    res.encoding = res.apparent_encoding
                    print("页面获取成功")
                    return res.text
                else:
                    print("页面返回异常!", res.status_code)
            except:
                print("网页获取异常")

    def get_book(self):  # 获取书名和url
        headers = {
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, '
                          'like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36 Edg/113.0.1774.42 '
        }
        res = self.get_url(self.root_url, headers)
        self.home_page = re.findall(r'<a href="/fenlei/.*?/">(.*?)</a>', res)  # 获取页面下的大分类,例如玄幻小说,修真小说等
        print('self.home_page = ' + str(self.home_page))
        soup = BeautifulSoup(res, 'html.parser')
        a_tags = soup.find_all('a')  # 进行获取所有a标签
        print(a_tags)
        try:  # 检测一个文件夹里是否有这个文件,如果没有就写入,有就退出
            dir_position = r'C:\Users\13538\PycharmProjects\test\练习'
            dir_path = dir_position + "\盗版小子!" + f'\{self.home_page[self.dir_num]}'
            print('dir_path = ' + dir_path)
            items = os.listdir(dir_path)  # 把这个文件夹里的所有文件名获取出来,存在items里
            for a in a_tags:
                href = a.get('href')  # 获取a标签的href值
                title = a.get('title') # 获取a标签的title值
                if href[:29] == 'https://www.bbiquge.net/book/':
                    href_tow = re.findall(r'https://www.bbiquge.net/book/\d+/$', str(href))  # 二级筛选,选出是书本对应的a标签
                    if href_tow:
                        for item in items:
                            if os.path.isdir(item) and item == title:  # 进行判断如果有这个小说名,那么就是已经爬过了,然后就跳过
                                continue
                            else:  # 没有就写入self.book.list列表中,以元组的形式
                                book_tuple = (href, title)
                                self.book_list.append(book_tuple)
                                if len(self.book_list) > 1:
                                    break
        except:  # 上面如果没有这个文件夹或这个文件夹是空的,就会报错
            for a in a_tags:
                href = a.get('href')
                title = a.get('title')
                if href[:29] == 'https://www.bbiquge.net/book/':
                    href_tow = re.findall(r'https://www.bbiquge.net/book/\d+/$', str(href))  # 二级筛选,选出是书本对应的a标签
                    if href_tow:
                        book_tuple = (href, title)
                        if book_tuple in self.book_list:
                            continue
                        elif book_tuple not in self.book_list:
                            self.book_list.append(book_tuple)
                            if len(self.book_list) > 1:  # 调试用的,让每一页只爬一本书
                                break
        print('self.book_list = ' + str(self.book_list))

    def get_book_tow(self):  # 获取小说的章节名和url
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57 '
        }
        dir_position = r'C:\Users\13538\PycharmProjects\test\练习\盗版小子!'
        os.chdir(dir_position)  # 定位到dir_position的文件地址上
        if not os.path.exists(self.home_page[self.dir_num]):  # 如果没有这个文件夹就创建
            os.mkdir(self.home_page[self.dir_num])
        book_tuple = self.book_list[0]  # 获取self.book.list的第一个值,拿出来后是个元组
        print('book_tuple=' + str(book_tuple))
        url_list = []
        book_url = book_tuple[0]  # 获取book_tuple的第一个值,因为元组的形式是(url, name)
        book_str = ''.join(book_url)  # 将获取到的url连接为一个没有分隔符的字符串,以免后面报错
        print(book_str)
        res = self.get_url(book_str, headers=headers)
        soup = BeautifulSoup(res, 'html.parser')
        option_tags = soup.find_all('option')  # 找到所有option标签
        num_options = len(option_tags)  # 获取出小说总页数
        dd_tags = soup.find_all('dd')  # 找到所有dd标签
        unfinished_url_list = re.findall('<dd><a href="(.*?)">(.*?)</a></dd>', str(dd_tags))  # 使用正则表达式获取到小说名和href值
        print('unfinished_url_list_第一张=' + str(unfinished_url_list))
        print("num_options:" + str(num_options))
        for a in unfinished_url_list:
            if len(url_list) >= 1:  # 调试用的,只爬取一章
                break
            url_list.append(a)  # 将title和href添加到url-list里
            # for i in range(1000):  # 循环1000次
            #     if i == 0 or i == 1:
            #         continue
            #     elif i > num_options:  # 如果i大于小说的最大章数时,就跳出这个循环
            #         break
            #     else:
            #         new_book_str = book_str + f"index_{i}.html"                           # 这是爬取完整的整本小说用到的,注释解掉就能用
            #         res = self.get_url(new_book_str, headers=headers)
            #         soup = BeautifulSoup(res, 'html.parser')
            #         dd_tags = soup.find_all('dd')
            #         unfinished_url_list = re.findall('<dd><a href="(.*?)">(.*?)</a></dd>', str(dd_tags))
            #         print(f'unfinished_url_list=' + str(unfinished_url_list))
            #         for b in unfinished_url_list:
            #             url_list.append(b)
        self.url_list_tow.append(url_list)  # 将元组形式的url_list添加到self.url_list_tow
        self.get_content()  # 使用self.get_content函数获取小说章节的内容
        self.url_list_tow.remove(url_list)  # 获取完后将url_list删掉,减少内存占用
        self.book_list.remove(book_tuple)  # 获取完后将book_tuple删掉,减少内存占用

    def get_content(self):
        def check_file_size(file_path, min_size):  # 检查文件是否完整的爬下来了的函数
            size = os.path.getsize(file_path)  # 获取文件大小
            if size < min_size:
                return True
            return False

        def write(chapter):  # 获取到章节内的小说内容,并写入文件
            print(chapter)
            dir_position = r'C:\Users\13538\PycharmProjects\test\练习\盗版小子!'
            chapter_title = '(' + str(a) + ')' + re.sub(r'[<>"/|?*]', ' ', chapter[1])  # 修正章节标题中的非法字符
            print('chapter_title=' + chapter_title)
            print('book_url + str(chapter[0])=' + book_url + str(chapter[0]))
            chapter_res = self.get_url(book_url + str(chapter[0]), headers=headers)
            chapter_html = BeautifulSoup(chapter_res, "html.parser")
            content_div = chapter_html.find("div", {"id": "content"})  # 找到id=content的div
            content = content_div.get_text(separator='\n')  # 将里面的换行符改成"\n"
            path1 = os.path.join(dir_position, self.home_page[self.dir_num], book_name, chapter_title + ".txt")  # 拼接变量让他成为一个完整的文件地址
            print('path1 = ' + path1)
            path2 = f"{path1}'.txt"
            new_path = re.sub(r'[<>"/|?*]', ' ', path2)
            print('new_path = ' + new_path)
            with open(new_path, 'w', encoding="utf-8") as f:  # 将获取的内容写入txt文件里
                f.write(content)
            return new_path

        a = 0
        min_size = 0.15 * 1024  # 限定最小大小不少于0.15kb（有些引子就三行
        print('self.book_list=' + str(self.book_list))
        book_tuple = self.book_list[0]
        print('book_tuple=' + str(book_tuple))
        book_url = book_tuple[0]  # 将元组内的值取出来
        book_name = book_tuple[1]
        print('book_url=' + book_url)
        print('book_name=' + book_name)
        dir_position = r'C:\Users\13538\PycharmProjects\test\练习\盗版小子!'
        os.chdir(dir_position + f'\{self.home_page[self.dir_num]}')  # 定位到应该在的文件夹里
        print(
            "dir_position + f'\{self.home_page[self.dir_num]}'2=" + dir_position + f'\{self.home_page[self.dir_num]}')
        if not os.path.exists(book_name):  # 如果没有就创建文件
            os.mkdir(book_name)

        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57 '
        }
        print('self.url_list_tow3=' + str(self.url_list_tow))
        for list_tow in self.url_list_tow:
            for chapter in list_tow:
                try:
                    new_path = write(chapter)  # 对文件进行检测
                    if check_file_size(new_path, min_size):  # 如果文件小于最小值就重新爬取
                        while check_file_size(new_path, min_size):
                            print('爬取失败,文件小于2kb,while循环重新爬取中')
                            write(chapter)
                    print()
                    a += 1

                except Exception as e:
                    print(f"获取章节内容失败: {str(e)}")
                    traceback.print_exc()
                    continue

    def get_one_page(self):  # 执行类内部应执行函数
        self.get_book()
        self.get_book_tow()
        self.book_list = []


def get_all_page(i, root_url):  # 将上面的类当成一个方法,使用在每一页上,从而获取整个网站的小说
    try:
        if not os.path.exists("盗版小子!"):
            os.mkdir("盗版小子!")
        root_url_two = root_url + f"fenlei/{i}_1/"
        print('root_url_tow=' + root_url_two)
        root_res = requests.get(root_url_two).text
        soup = BeautifulSoup(root_res, 'html.parser')
        a_tag = soup.find('a', class_='last')  # 获取最后一个
        print('num_options=' + str(a_tag.text))
        print()
        for a in range(50000):
            if a == 0:
                continue
            elif a > int(a_tag.text):
                break
            else:
                root_url_three = root_url + f"fenlei/{i}_{a}/"
                print('root_url_three = ' + root_url_three)
                pc = PC(root_url_three, i - 1)
                pc.get_one_page()
    except Exception as e:
        print("get_all_page出现错误 = " + str(e))
        traceback.print_exc()


def multiprocess(root_url, i):
    process = multiprocessing.Process(target=get_all_page, args=(i, root_url))
    process.start()
    process.join()


def multithreading(root_url):
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
        for i in range(1, 7):
            executor.submit(multiprocess, root_url, i)
            time.sleep(0.2)


root_url = "https://www.bbiquge.net/"
multithreading(root_url)
