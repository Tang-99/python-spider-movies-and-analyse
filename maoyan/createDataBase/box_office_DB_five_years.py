# create database
# -*- coding: UTF-8 -*-
import json
import pandas as pd
import pymysql
import csv
import codecs


# load通过json.load(open(’*.json’))这样的格式，从文件句柄中打开文件，加载到Python的变量中，并以字典的格式转换。
# loads必须对于Python内存中的序列化对象转换成字符串。
# 因此，load和loads都是实现“反序列化”,load针对文件,loads针对数据
# 读取json数据，并写入数据库
def get_data20():
    with open('../2020票房排行榜.json', 'r') as f:
        res = json.load(f)  # 解析每一行数据
        text20 = res.get('list')
        for i in range(len(text20)):
            # text20[i]['rankId'] = i
            text20[i]['times'] = 2020
    # print(text20)
    print("————————读取数据完成————")
    return text20


def get_data19():
    with open('../2019票房排行榜.json', 'r') as f:
        res = json.load(f)  # 解析每一行数据
        text19 = res.get('list')
        for i in range(len(text19)):
            # text19[i]['rankId'] = i
            text19[i]['times'] = 2019
        # print(text19)
    print("————————读取数据完成————")
    return text19


def get_data18():
    with open('../2018票房排行榜.json', 'r') as f:
        res = json.load(f)  # 解析每一行数据
        text18 = res.get('list')
        for i in range(len(text18)):
            # text18[i]['rankId'] = i
            text18[i]['times'] = 2018
        # print(text18)
    print("————————读取数据完成————")
    return text18


def get_data17():
    with open('../2017票房排行榜.json', 'r') as f:
        res = json.load(f)  # 解析每一行数据
        text17 = res.get('list')
        for i in range(len(text17)):
            # text17[i]['rankId'] = i
            text17[i]['times'] = 2017
        # print(text17)
    print("————————读取数据完成————")
    return text17


def get_data16():
    with open('../2016票房排行榜.json', 'r') as f:
        res = json.load(f)  # 解析每一行数据
        text16 = res.get('list')
        for i in range(len(text16)):
            # text16[i]['rankId'] = i
            text16[i]['times'] = 2016
        # print(text16)
    print("————————读取数据完成————")
    return text16


def get_five_years(text20, text19, text18, text17, text16):
    text_years = text20 + text19 + text18 + text17 + text16
    for i in range(len(text_years)):
        text_years[i]['rankId'] = i

    print(text_years)

    db = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='BoxOfficeDB',
                         charset='utf8')
    # 拿到游标
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")

    data = cursor.fetchone()

    # print("Database version : '%s' " % data)
    # 结果表明已经连接成功
    cursor.execute("DROP TABLE IF EXISTS Box_Office_Five_years")

    sql = """CREATE TABLE Box_Office_Five_years (
      rankId INT(50) primary key ,
      avgShowViewDesc VARCHAR(100),
      avgViewBoxDesc VARCHAR(100),
      boxDesc VARCHAR(100),
      movieId VARCHAR(100)  ,
      movieName VARCHAR(100),
      releaseInfo VARCHAR(100),
      times VARCHAR(100))"""

    cursor.execute(sql)  # 根据需要创建一个表格

    for i in range(len(text_years)):
        insertsql = "insert into Box_Office_Five_years(rankId, avgShowViewDesc, avgViewBoxDesc, boxDesc, movieId, movieName, releaseInfo, times) value('%s', '%s','%s','%s','%s','%s','%s', '%s')" % (
            text_years[i]['rankId'], text_years[i]['avgShowViewDesc'], text_years[i]['avgViewBoxDesc'],
            text_years[i]['boxDesc'],
            text_years[i]['movieId'], text_years[i]['movieName'], text_years[i]['releaseInfo'], text_years[i]['times'])
        # print(insert16)
        cursor.execute(insertsql)

    print("————————存入数据库完成————")
    cursor.close()
    db.commit()
    db.close()
    '''except Exception as e:
        db.rollback()
        print(str(e))
        break'''


file_path_100 = "E:/pythonsoft/spider/maoyan/rankList/猫眼电影排行榜.csv"
data = pd.read_csv(file_path_100, encoding='utf-8')


def get_conn():
    db = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='BoxOfficeDB',
                         charset='utf8')
    return db


def create_table():
    # 连接本地数据库
    conn = get_conn()

    # 创建游标
    cursor = conn.cursor()
    # 如果存在表，则删除
    cursor.execute("DROP TABLE IF EXISTS Maoyan_Top100")

    # 创建表
    sql = """CREATE TABLE Maoyan_Top100 (
       rankId INT PRIMARY KEY, 
       movieName VARCHAR(100),
       years VARCHAR(100),
       score VARCHAR(100),
       actors VARCHAR(100),
       image VARCHAR(200))"""


    try:
        # 执行SQL语句
        cursor.execute(sql)

        print("创建数据库成功")
    except Exception as e:
        print("创建数据库失败：case%s" % e)
    finally:
        # 关闭游标连接
        cursor.close()
        # 关闭数据库连接
        conn.close()


def insert(cur, sql, args):
    # 数据插入模块
    try:
        cur.execute(sql, args)
    except Exception as e:
        print(e)


def read_csv_to_mysql(file_path_100):
    '''
    csv文件->数据库
    :param file_path:
    :return:
    '''

    with codecs.open(filename=file_path_100, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        head = next(reader)
        # print(head)
        conn = get_conn()
        cur = conn.cursor()
        sql = 'insert into Maoyan_Top100 values(%s,%s,%s,%s,%s,%s)'
        for item in reader:
            args = tuple(item)
            # print(args)
            insert(cur, sql=sql, args=args)
        print("数据添加完成")
        conn.commit()
        cur.close()
        conn.close()


if __name__ == "__main__":  # 起到一个初始化或者调用函数的作用
    a = get_data20()
    b = get_data19()
    c = get_data18()
    d = get_data17()
    e = get_data16()
    get_five_years(a, b, c, d, e)
    create_table()
    read_csv_to_mysql(file_path_100)
