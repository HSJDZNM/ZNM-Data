import re
import requests
from bs4 import BeautifulSoup

wz = requests.get("http://10.1.88.252:7000/")
name = re.findall('<a class="name" href="(.*?)">', wz.text)
book = ["http://10.1.88.252:7000" + n for n in name]
print(book)
for b in book:
    int = 0
    a = requests.get("b")
    name_book = re.findall('<a class="chapter" href="(.*?)">', a.text, )
    book_links = ["http://10.1.88.252:7000" + n for n in name_book]
    book_links.remove('http://10.1.88.252:7000/庆余年')

    for nr in book_links:
        a = requests.get(nr)
        b = a.text
        soup = BeautifulSoup(b, 'html.parser')
        neirong = soup.find_all('p')
        neirong_2 = soup.find_all('h1')

        re = ""
        ra = ""
        for p_2 in neirong_2:
            ra += p_2.text + "\n\n"
        for p in neirong:
            re += p.text + "\n\n"
        print(neirong)
        with open(f"C:/Users/LL/Desktop/爬/第{int}回.txt", "w", encoding="utf-8") as f:
            with open(f"C:/Users/LL/Desktop/爬{name}/第{int}回.txt", "w", encoding="utf-8") as f2:
                f2.write(ra)
                f2.write(re)
                int+=1

