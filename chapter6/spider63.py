# Selenium模拟web浏览器爬取数据
# selenium需要操作本地浏览器，默认是Firefox,因此推荐安装Firefox,要求是55以上版本。由于版本兼容的问题，还需要下载浏览器引擎GeckoDriver
# Selenium操作浏览器是通过WebDriver对象实现的，WebDriver对象提供了操作浏览器和访问HTML源码中数据的函数

# find_element_by_id                # 通过元素的id查找符合条件的第一个元素
# find_elements_by_id               # 通过元素的id查找符合条件的所有元素
# find_element_by_name(name)        # 通过元素的名称查找符合条件的第一个元素
# find_elements_by_name(name)
# find_element_by_tag(name)         # 通过元素的标签名查找符合条件的第一个元素
# find_elements_by_tag(name)
# find_element_by_xpath(name)       # 通过xpath查找符合条件的第一个元素
# find_elements_by_xpath(name)

# find_element_by_link_text(link_text)          # 通过连接文本查找符合条件的第一个元素
# find_elements_by_link_text(link_text)
# find_element_by_class_name(name)              # 通过CSS中class属性查找符合条件的第一个元素
# find_elements_by_class_name(name)
# find_element_by_css_selector(css_selector)    # 通过CSS中的选择器查找符合条件的第一个元素
# find_elements_by_css_selector(css_selector)

from selenium import webdriver

def getdata(stockcode):                 # stockcode参数表示股票代号
    driver = webdriver.Firefox()        # 使用selenium爬取数据
    # driver = webdriver.Safari()
    # driver = webdriver.Chrome()

    url = 'https://q.stock.sohu.com/cn/{0}/lshq.shtml'
    strURL = url.format(stockcode)      # 传递股票代号参数，获取最终的URL网址
    print('请求的URL',strURL)

    driver.get(strURL)                  # 发送请求

    tableElement = driver.find_element_by_id('BIZ_hq_historySearch')        # 通过页面CSS id找到表格标签对象
    trList = tableElement.find_elements_by_tag_name('tr')       # 通过标签名找出表格中所有tr元素

    # 保存数据列表
    datas = []
    for index, tr in enumerate(trList):         # enumerate枚举
        if index < 4:                           # 跳过表格的前4行数据
            continue
        tds = tr.find_elements_by_tag_name('td')    # 查找tr下面的所有td元素

        row = dict()                                # 保存一行数据的字典对象
        row['Date'] = tds[0].text                   # 日期
        row['Open'] = float(tds[1].text)            # 开盘价
        row['Close'] = float(tds[2].text)           # 收盘价
        row['High'] = float(tds[5].text)            # 最高价
        row['Low'] = float(tds[6].text)             # 最低价
        row['Volume'] = float(tds[7].text)          # 成交量
        datas.append(row)

    driver.quit()           # 退出浏览器
    return datas            # 返回数据



