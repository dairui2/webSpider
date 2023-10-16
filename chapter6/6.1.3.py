#爬取数据，解析数据，存储数据
# 存储数据  解析html数据通过BeautifulSoup对象实现,对象解析器有4种可用（html.parser, lxml, lxml-xml, html5lib）

import os
import urllib.request
from bs4 import BeautifulSoup

url = 'http://p.weather.com.cn'
def getHtmlString():
# """ 网络请求返回Html字符串"""
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        data = response.read()
        htmlstr = data.decode(encoding = 'utf-8', errors='ignore')      #注意编码字符集要与网页中<meta charset="utf-8">保持一致
        return htmlstr

def find_imageurls(htmlstr):                        # 从html代码中查找匹配的字符串
    sp = BeautifulSoup(htmlstr, 'html.parser')      # 创建BeautifulSoup对象，htmlstr是需要解析的html字符串, 'html.parser'是解析器
    imagelist = sp.find_all('img')                  # 返回所有的image标签元素

    # 从img标签的对象列表中返回对应的src列表,<img  src="https://i.i8tq.com/weather2020/search/rbAd.png"  style="width:100%;">
    srclist = list(map(lambda u: u.get('src'), imagelist))          # map是映射函数，用于将标签对象列表变换为src列表。。

    # 过滤掉非.png和.jpg结尾文件的src字符串；filter是过滤函数，过滤掉不符合条件的元素，该函数详情见ch8_6.py
    filtered_srclist = filter(lambda  u: u.lower().endswith('.png')             # 判断.png字符串结尾
                                      or u.lower().endswith('.jpg'), srclist)
    return filtered_srclist

if __name__ == '__main__':
    html = getHtmlString()
    url_list =find_imageurls(html)      #返回图片列表

    # 遍历图片列表
    for img_url in url_list:
        req = urllib.request.Request(img_url)               #逐个下载图片到本地download文件夹下
        with urllib.request.urlopen(req) as response:       #根据图片网址请求图片数据
            data = response.read()                          #获取图片文件名

            pos = img_url.rfind('/')                        #找到最后一个"/"字符的位置
            filename = img_url[pos + 1:]

            filepath = 'download/' + filename               #获取图片路径

            #判断当前文件夹下是否存在download子文件夹，如果不存在则创建
            if not os.path.exists('download'):
                os.mkdir('download')

            with open(filepath, 'wb') as f:
                f.write(data)
                print('下载图片:{}.'.format(filename))
    print('下载完成')