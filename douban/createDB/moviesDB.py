# -*- coding: UTF-8 -*-

import pandas as pd
import pymysql
import csv
import codecs

file_path = "E:/pythonsoft/spider/douban/combine/电影高分排行榜.csv"
data = pd.read_csv(file_path, encoding='utf-8')

file_path1 = "E:/pythonsoft/spider/douban/Top20.csv"
data1 = pd.read_csv(file_path1, encoding='utf-8')

file_path2 = "E:/pythonsoft/spider/douban/Top30.csv"
data2 = pd.read_csv(file_path2, encoding='utf-8')


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
    cursor.execute("DROP TABLE IF EXISTS Movies_Great")
    cursor.execute("DROP TABLE IF EXISTS Movies_T30")
    cursor.execute("DROP TABLE IF EXISTS Movies_Analyse_T30")

    # 创建表
    sql = """CREATE TABLE Movies_Great (
       rankId INT PRIMARY KEY, 
       movieName VARCHAR(100),
       movieType VARCHAR(100),
       director VARCHAR(200),
       actors VARCHAR(100)  ,
       commentNum VARCHAR(100),
       score VARCHAR(100),
       country VARCHAR(100),
       years VARCHAR(100),
       image VARCHAR(200))"""

    sql30 = """CREATE TABLE Movies_T30 (
       rankId INT PRIMARY KEY, 
       movieName VARCHAR(100),
       movieType VARCHAR(100),
       director VARCHAR(100),
       actors VARCHAR(1000)  ,
       score VARCHAR(100),
       publicPraise VARCHAR(200),
       commentNum VARCHAR(100),
       info VARCHAR(1000),
       image VARCHAR(200))"""

    sql30_An = """CREATE TABLE Movies_Analyse_T30 (
       rankId INT PRIMARY KEY, 
       five VARCHAR(50),
       four VARCHAR(50),
       three VARCHAR(50),
       two VARCHAR(50),
       one VARCHAR(50),
       movieName VARCHAR(100),
       rem VARCHAR(100))"""

    try:
        # 执行SQL语句
        cursor.execute(sql)
        cursor.execute(sql30)
        cursor.execute(sql30_An)

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


def read_csv_to_mysql(file_path):
    '''
    csv文件->数据库
    :param file_path:
    :return:
    '''

    with codecs.open(filename=file_path, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        head = next(reader)
        # print(head)
        conn = get_conn()
        cur = conn.cursor()
        sql = 'insert into movies_great values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        for item in reader:
            args = tuple(item)
            # print(args)
            insert(cur, sql=sql, args=args)
        print("数据添加完成")
        conn.commit()
        cur.close()
        conn.close()


def read_csv1_to_mysql(file_path1):
    '''
    csv文件->数据库
    :param file_path:
    :return:
    '''

    with codecs.open(filename=file_path1, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        head = next(reader)
        # print(head)
        conn = get_conn()
        cur = conn.cursor()
        sql = 'insert into movies_t30 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        for item in reader:
            args = tuple(item)
            # print(args)
            insert(cur, sql=sql, args=args)
        print("数据添加完成")
        conn.commit()
        cur.close()
        conn.close()


def read_csv2_to_mysql(file_path2):
    '''
    csv文件->数据库
    :param file_path:
    :return:
    '''

    with codecs.open(filename=file_path2, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        head = next(reader)
        # print(head)
        conn = get_conn()
        cur = conn.cursor()
        sql = 'insert into movies_analyse_t30 values(%s,%s,%s,%s,%s,%s,%s,%s)'
        for item in reader:
            args = tuple(item)
            # print(args)
            insert(cur, sql=sql, args=args)
        print("数据添加完成")
        conn.commit()
        cur.close()
        conn.close()


if __name__ == "__main__":  # 起到一个初始化或者调用函数的作用
    create_table()
    read_csv_to_mysql(file_path)
    read_csv1_to_mysql(file_path1)
    read_csv2_to_mysql(file_path2)
