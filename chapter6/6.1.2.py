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
        print(img_url)                 #打印图片url列表