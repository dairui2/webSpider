import spider63     # 导入自定义的spider模块

if __name__ == '__main__':
    datas = spider63.getdata(601857)        # 爬取股票代号为601857的股票数据，调用spider模块的getdata函数爬取数据并返回数据
    print(datas)                            # 爬取的数据