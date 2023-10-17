import csv
import spider63     # 导入自定义的spider模块

if __name__ == '__main__':
    datas = spider63.getdata(601857)        #调用spider模块的getdata函数爬取数据并返回数据

    f = r'/Users/dai/Documents/股票历史交易数据.csv'
    fieldnames = ['Date','Open','Close','High','Low','Volume']      #设置xls表头

    with open(f,'w',newline='',encoding='gbk') as wf:       # 打开csv文件，制定编码字符集gbk，newline=''写入一个新行时行尾的结束字符
        write = csv.DictWriter(wf, fieldnames=fieldnames)   # 获取writer对象，该对象可以将一个字典对象写入csv文件中的一行
        write.writeheader()                                 # 写入电子表格的表头

        for dictrow in datas:                               # 遍历datas列表对象
            write.writerow(dictrow)                         # 通过writer对象的writerow函数逐行写入数据到csv文件中
