import os
import requests
from bs4 import BeautifulSoup
from PIL import Image

# 设置搜索关键字
search_word = '真猫图片'

# 创建目录
if not os.path.exists(search_word):
    os.makedirs(search_word)

# 设置基础URL和查询参数
base_url = 'https://cn.bing.com/images/search?'
query_params = {'q': search_word, 'form': 'HDRSC2', 'first': '1'}

# 记录已经下载的图片数量
downloaded_count = 0

# 爬取图片
while downloaded_count < 2000:
    # 构造请求URL
    query_params['first'] = downloaded_count + 1
    query_str = '&'.join([f'{k}={v}' for k, v in query_params.items()])
    url = base_url + query_str

    # 发送请求
    response = requests.get(url)

    # 解析HTML页面
    soup = BeautifulSoup(response.content, 'html.parser')

    # 提取所有图片链接
    for img in soup.select('img'):
        src = img.get('src')
        if src and src.startswith('http'):
            # 下载图片并保存到指定目录
            response = requests.get(src)
            image = Image.open(response.content)
            if image.format == 'JPEG' and image.size == (900, 900):
                file_name = os.path.join(search_word, f'{search_word}_{downloaded_count}.jpg')
                with open(file_name, 'wb') as f:
                    f.write(response.content)
                downloaded_count += 1

            # 如果已经下载了足够数量的图片，则退出循环
            if downloaded_count >= 2000:
                break

    # 如果已经没有更多图片，则退出循环
    if not soup.select('img'):
        break
