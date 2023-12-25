# import requests
# from bs4 import BeautifulSoup
# import os
# import re
#
# ###
# root_url="http://10.1.88.252:7000"
#
# def get_url(url):
#     while True:
#         try:
#             res=requests.get(url)
#             if res.status_code==200:
#                 res.encoding=res.apparent_encoding
#                 print("页面获取成功")
#                 return res.text
#             else:
#                 print("页面返回异常!",res.status_code)
#         except:
#             print("网页获取异常")
# res = get_url(root_url)
# print(res)
#
# ###
# book_list = re.findall('<a class="name" href="(.*?)">', res)
#
# book_list = [root_url + i for i in book_list]
#
# book_list.remove('http://10.1.88.252:7000/庆余年')
#
# print(book_list)
#
#
# ###
# url_list=[]
# for book in book_list:
#     res=get_url(book)
#     a_list = re.findall('<a class="chapter" href="(.*?)">(.*?)\n?</a>',res)
#     for a in a_list:
#         url_list.append(a)
# print(url_list,len(url_list))
#
#
# ###
# for chapter in url_list:
#     url = root_url + chapter[0]
#     print(url)
#
#     book_name = chapter[0].split("/")[1]
#     print(book_name)
#
#     if not os.path.exists(book_name):
#         os.mkdir(book_name)
#
#     res = get_url(url)
#     html = BeautifulSoup(res, "html.parser")
#     content = html.find("div", {"id": "content"}).text
#     print(content)
#
#     path = os.path.join(book_name, chapter[1])
#     with open(path, "w", encoding="utf-8") as f:
#         f.write(content)

import requests
from bs4 import BeautifulSoup
import os
import re


class NovelCrawler:
    def __init__(self, root_url):
        self.root_url = root_url
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

    def crawl_book_list(self):
        res = self.get_url(self.root_url)
        book_list = re.findall('<a class="name" href="(.*?)">', res)
        book_list = [self.root_url + i for i in book_list]
        book_list.remove('http://10.1.88.252:7000/庆余年')
        return book_list

    def crawl_chapters(self, book_list):
        url_list = []
        for book in book_list:
            res = self.get_url(book)
            a_list = re.findall('<a class="chapter" href="(.*?)">(.*?)\n?</a>', res)
            for a in a_list:
                url_list.append(a)
        return url_list

    def crawl_contents(self, url_list):
        for chapter in url_list:
            url = self.root_url + chapter[0]
            print(url)

            book_name = chapter[0].split("/")[1]
            print(book_name)

            if not os.path.exists(book_name):
                os.mkdir(book_name)

            res = self.get_url(url)
            html = BeautifulSoup(res, "html.parser")
            content = html.find("div", {"id": "content"}).text
            print(content)

            path = os.path.join(book_name, chapter[1])
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)


root_url = "http://10.1.88.252:7000"
novel_crawler = NovelCrawler(root_url)
book_list = novel_crawler.crawl_book_list()
url_list = novel_crawler.crawl_chapters(book_list)
novel_crawler.crawl_contents(url_list)

