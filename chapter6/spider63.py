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



