import requests
import re
from bs4 import BeautifulSoup
import os
import queue
import threading


class PC:
    def __init__(self, root_url):
        self.root_url = root_url
        self.book_list = []
        self.book_tow_list = []
        self.h3_list = []
        self.book_queue = queue.Queue()
        self.book_chapter_queue = queue.Queue()

    def get_html(self, url, headers):
        while True:
            try:
                res = requests.get(url, headers=headers)
                if res.status_code == 200:
                    res.encoding = res.apparent_encoding
                    print("页面获取成功")
                    return res.text
                else:
                    print("页面获取异常!" + str(res.status_code))
            except:
                print("网页获取异常")

    def mk_top_dir(self):
        if not os.path.exists("盗版小子!"):
            os.mkdir("盗版小子!")

    def get_home_title(self):
        headers = {
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, '
                          'like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36 Edg/113.0.1774.42 '
        }
        res = self.get_html(self.root_url, headers)
        soup = BeautifulSoup(res, 'html.parser')
        h3_tags = soup.find_all('h3')
        self.h3_list = []
        for h3 in h3_tags:
            h3_content = h3.text
            self.h3_list.append(h3_content)
            if len(self.h3_list) >= 6:
                break
        print(self.h3_list)

    def mk_home_title_dir(self):
        dir_path = r"C:\Users\13538\PycharmProjects\test\练习\盗版小子!"
        os.chdir(dir_path)
        for h3 in self.h3_list:
            if not os.path.exists(h3):
                os.mkdir(h3)

    def get_book(self):

        for i in range(1, 2):
            root_url_two = self.root_url + f"fenlei/{i}_1/"
            print('root_url_tow=' + root_url_two)
            root_res = requests.get(root_url_two).text
            soup = BeautifulSoup(root_res, 'html.parser')
            a_tag = soup.find('a', class_='last')  # 获取最后一个
            print('num_options=' + str(a_tag.text))
            print()
            # for a in range(50000):
            #     if a == 0:
            #         continue
            #     elif a > int(a_tag.text):
            #         break
            #     else:
            #         root_url_three = self.root_url + f"fenlei/{i}_{a}/"
            #         print('root_url_three = ' + root_url_three)
            headers = {
                'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, '
                              'like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36 Edg/113.0.1774.42 '
            }
            res = self.get_html(root_url_two, headers)
            soup = BeautifulSoup(res, 'html.parser')
            a_tags = soup.find_all('a')  # 进行获取所有a标签
            print(a_tags)
            for a in a_tags:
                href = a.get('href')
                title = a.get('title')
                if href[:29] == 'https://www.bbiquge.net/book/':
                    href_tow = re.findall(r'https://www.bbiquge.net/book/\d+/$', str(href))  # 二级筛选,选出是书本对应的a标签
                    if href_tow:
                        book_tuple = [self.h3_list[i - 1], href, title]
                        data = self.book_queue.get()
                        if book_tuple in data:
                            continue
                        elif book_tuple not in data:
                            self.book_queue.put(book_tuple)
                            # self.book_list.append(book_tuple)
                            queue_length = self.book_queue.qsize()
                            if queue_length > 1:  # 调试用的,让每一页只爬一本书
                                break
        # print('self.book_list = ' + str(self.book_list))
        self.book_queue.put(None)

    def get_tow_book(self):
        self.book_queue.get()
        data = self.book_queue.get()
        print(data)
        # headers = {
        #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
        #                   'Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57 '
        # }
        # while True:
        #     self.book_queue.get()
        #     data = self.book_queue.get()
        #     print(data)
        #     # book_list = self.book_list[0]
        #     book_home = data[0]
        #     book_url = data[1]
        #     book_name = data[2]
        #     book_str = ''.join(book_url)
        #     res = self.get_html(book_str, headers=headers)
        #     soup = BeautifulSoup(res, 'html.parser')
        #     option_tags = soup.find_all('option')
        #     num_options = len(option_tags)
        #     dd_tags = soup.find_all('dd')
        #     unfinished_url_list = re.findall('<dd><a href="(.*?)">(.*?)</a></dd>', str(dd_tags))
        #     print(f'unfinished_url_list1=' + str(unfinished_url_list))
        #     # for i in range(1000):  # 循环1000次
        #     #     if i == 0 or i == 1:
        #     #         continue
        #     #     elif i > num_options:  # 如果i大于小说的最大章数时,就跳出这个循环
        #     #         break
        #     #     else:
        #     #         new_book_str = book_str + f"index_{i}.html"                           # 这是爬取完整的整本小说用到的,注释解掉就能用
        #     #         res = self.get_html(new_book_str, headers=headers)
        #     #         soup = BeautifulSoup(res, 'html.parser')
        #     #         dd_tags = soup.find_all('dd')
        #     #         unfinished_url_list = re.findall('<dd><a href="(.*?)">(.*?)</a></dd>', str(dd_tags))
        #     #         print(f'unfinished_url_list2=' + str(unfinished_url_list))
        #     for book_tow in unfinished_url_list:
        #         book_tow_list = []
        #         book_tow_name = book_tow[1]
        #         book_tow_url = book_url + book_tow[0]
        #         book_tow_list.append(book_home)
        #         book_tow_list.append(book_url)
        #         book_tow_list.append(book_name)
        #         book_tow_list.append(book_tow_name)
        #         book_tow_list.append(book_tow_url)
        #         print(book_tow_list)
        #         self.book_chapter_queue.put(book_tow_list)
        #
        #
        #     #     self.book_tow_list.append(book_tow_list)
        #     # print(self.book_tow_list)
        #     if data is None:  # 判断数据是否生产结束
        #         break

    def main(self):
        self.mk_top_dir()
        self.get_home_title()
        self.mk_home_title_dir()
        self.get_book()
        self.get_tow_book()


if __name__ == '__main__':
    pc = PC("https://www.bbiquge.net/")
    pc.main()
