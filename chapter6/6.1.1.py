#爬取数据，解析数据，存储数据
# 爬取数据 urllib.request模块
import urllib.request

url = 'http://p.weather.com.cn'         # 爬取数据的网址
def getHtmlString():                    # 声明一个函数，用于获取html代码
# """ 网络请求返回Html字符串"""
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        data = response.read()
        htmlstr = data.decode(encoding = 'utf-8', errors='ignore')      #注意编码字符集要与网页中<meta charset="utf-8">保持一致，
        return htmlstr

if __name__ == '__main__':
    html = getHtmlString()
    print(html)