import requests
from bs4 import BeautifulSoup
import os
import re


class PC:
    def __init__(self, root_url):
        self.root_url = root_url
        self.book_list = []
        self.url_list = []

    def get_url(self, url):
        while True:
            try:
                res = requests.get(url)
                if res.status_code == 200:
                    res.encoding = res.apparent_encoding
                    print("页面获取成功")
                    return res.text
                else:
                    print("页面返回异常!", res.status_code)
            except:
                print("网页获取异常")

    def mk_bl(self):
        res = self.get_url(self.root_url)
        self.book_list = re.findall('<a class="name" href="(.*?)">', res)
        self.book_list = [self.root_url + i for i in self.book_list]
        self.book_list.remove('http://10.1.88.252:7000/庆余年')
        print(self.book_list)

    def mk_ul(self):
        for book in self.book_list:
            res = self.get_url(book)
            a_list = re.findall('<a class="chapter" href="(.*?)">(.*?)\n?</a>', res)
            for a in a_list:
                self.url_list.append(a)
        print(self.url_list)

    def get_nr(self):
        for chapter in self.url_list:
            url = self.root_url + chapter[0]
            print(url)

            book_name = chapter[0].split("/")[1]
            print(book_name)

            # if not os.path.exists(book_name):
            #     os.mkdir(book_name)
            #
            # res = self.get_url(url)
            # html = BeautifulSoup(res, "html.parser")
            # content = html.find("div", {"id": "content"}).text
            # print(content)
            #
            # path = os.path.join(book_name, chapter[1])
            # with open(path, "w", encoding="utf-8") as f:
            #     f.write(content)

    def main(self):
        self.mk_bl()
        self.mk_ul()
        self.get_nr()


pc = PC("http://10.1.88.252:7000")
pc.main()
