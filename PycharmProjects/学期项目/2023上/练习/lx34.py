import requests
from bs4 import BeautifulSoup
import os


class PC:
    def __init__(self, root_url):
        self.root_url = root_url
        self.second_level = []
        self.tp_url_list = []

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

    def get_second_level(self):
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57'
        }
        res = self.get_url(self.root_url, headers=headers)
        soup = BeautifulSoup(res, 'html.parser')
        url = soup.find_all('a', class_='topicurl listbook', target='_blank')
        print(url)
        for a in url:
            href = a.get('href')
            title = a.get('title')
            tp_list = []
            if href[:10] == '/dcbbs/d15':
                url = 'https://bbs.zol.com.cn' + href
                tp_list.append(url)
                tp_list.append(title)
                self.second_level.append(tp_list)
            else:
                continue

        print(self.second_level)

    def get_tp_url(self):
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57'
        }
        for second_lv in self.second_level:
            url_list = []
            print('second_lv[0]=' + second_lv[0])
            print('second_lv[1]=' + second_lv[1])
            res = self.get_url(second_lv[0], headers=headers)
            soup = BeautifulSoup(res, 'html.parser')
            url = soup.find_all('img', class_='lazy')
            title = soup.h1.text
            url_list.append(title)
            for a in url:
                data_original = a.get('data-original')
                print(data_original)
                url_list.append(data_original)
            self.tp_url_list.append(url_list)
            print(second_lv[1] + "完成")
            print()
        print('self.tp_url_list=' + str(self.tp_url_list))

    def save_tp(self):
        if not os.path.exists("图片集"):
            os.mkdir("图片集")
        for one_tp_list in self.tp_url_list:
            i = 0
            os.chdir('C:/Users/13538/PycharmProjects/test/练习/图片集')
            if not os.path.exists(one_tp_list[0]):
                os.mkdir(one_tp_list[0])
            for url in one_tp_list:
                try:
                    headers = {
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57'
                    }
                    path = "C:/Users/13538/PycharmProjects/test/练习/图片集/" + one_tp_list[0]
                    print(path)
                    set_path = f'{path}/{i}.jpg'
                    res = requests.get(url, headers=headers)
                    f = open(set_path, 'wb')
                    f.write(res.content)
                    print(f"保存了第{i}张图")
                    print()
                    i += 1
                except Exception as e:
                    print('Exception=' + str(e))
                    continue

    def main(self):
        self.get_second_level()
        self.get_tp_url()
        self.save_tp()


pc = PC("https://bbs.zol.com.cn/dcbbs/d15.html")
pc.main()
