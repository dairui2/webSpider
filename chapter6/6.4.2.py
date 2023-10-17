import spider63     # 导入自定义的spider模块
import pymysql

if __name__ == '__main__':
    datas = spider63.getdata(601857)        #调用spider模块的getdata函数爬取数据并返回数据

     # 连接 MySQL 数据库
    connection = pymysql.connect(host="localhost", user="root", password="123456", database="test")
    cursor = connection.cursor()

    # Define the SQL query to insert data
    insert_query = "INSERT INTO gupiao (Date, Open, Close, High, Low, Volume) VALUES (%s, %s, %s, %s, %s, %s)"

    # Loop through the data list and insert each dictionary into the database
    for entry in datas:
        values = (entry["Date"], entry["Open"], entry["Close"], entry["High"], entry["Low"], entry["Volume"])
        cursor.execute(insert_query, values)

    # Commit the changes to the database
    connection.commit()

    # Close the cursor and the connection
    cursor.close()
    connection.close()