import pymongo  # 用于连接 MongoDB 数据库
import spider63  # 导入自定义的spider模块

if __name__ == '__main__':
    # 从 spider63 模块获取数据
    datas = spider63.getdata(601857)  # 调用spider模块的getdata函数爬取数据并返回数据

    if datas:
        # 连接 MongoDB
        client = pymongo.MongoClient('mongodb://localhost:27017')  # 请替换用户名和密码
        db = client['db1']  # 选择数据库
        collection = db['stock']  # 选择表（集合）

        # 将数据插入 MongoDB
        collection.insert_many(datas)  # 使用 insert_many 方法批量插入数据

        print(f"成功将 {len(datas)} 条数据插入 MongoDB 数据库")
    else:
        print("没有获取到数据，无法插入 MongoDB。")
