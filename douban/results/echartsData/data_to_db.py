# create day boxoffice database
# -*- coding: UTF-8 -*-
import json
import pymysql


# 流行电影类型
def get_pop_type():
    with open('E:/pythonsoft/spider/douban/results/echartsData/movie_type_data.json', 'r') as f:
        res = json.load(f)  # 解析每一行数据
        pop_type = res.get('data')
        # fday = firstday.get('list')
        # # 添加序号
        # for i in range(len(pop_type)):
        #     pop_type[i]['rankId'] = i
        # # print(pop_type)
    print("————————读取数据完成————")
    return pop_type


# 流行电影地图展示
def get_movie_map():
    with open('E:/pythonsoft/spider/douban/results/echartsData/movie_map_data.json', 'r') as f:
        res = json.load(f)  # 解析每一行数据
        movie_map = res.get('data')
        # fday = firstday.get('list')
        # # 添加序号
        # for i in range(len(movie_map)):
        #     movie_map[i]['rankId'] = i
        # # print(movie_map)
    print("————————读取数据完成————")
    return movie_map


def get_movie_actor():
    with open('E:/pythonsoft/spider/douban/results/echartsData/movie_actor_data.json', 'r', encoding='utf-8') as f:
        res = json.load(f)  # 解析每一行数据
        movie_actor = res.get('data')
        # fday = firstday.get('list')
        # # 添加序号
        # for i in range(len(movie_actor)):
        #     movie_actor[i]['rankId'] = i
        # # print(movie_actor)
    print("————————读取数据完成————")
    return movie_actor


def get_movie_country():
    with open('E:/pythonsoft/spider/douban/results/echartsData/movie_country_data.json', 'r', encoding='utf-8') as f:
        res = json.load(f)  # 解析每一行数据
        movie_country = res.get('data')
        # fday = firstday.get('list')
        # # 添加序号
        # for i in range(len(movie_actor)):
        #     movie_actor[i]['rankId'] = i
        # # print(movie_actor)
    print("————————读取数据完成————")
    return movie_country


def get_movie30_actor():
    with open('E:/pythonsoft/spider/douban/results/echartsData/movie30_actor_data.json', 'r', encoding='utf-8') as f:
        res = json.load(f)  # 解析每一行数据
        movie30_actor = res.get('data')
        # fday = firstday.get('list')
        # # 添加序号
        # for i in range(len(movie_actor)):
        #     movie_actor[i]['rankId'] = i
        # # print(movie_actor)
    print("————————读取数据完成————")
    return movie30_actor


def data_insert_pop_type(pop_type):
    db = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='BoxOfficeDB',
                         charset='utf8')
    # 拿到游标
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")

    data = cursor.fetchone()

    # print("Database version : '%s' " % data)
    # 结果表明已经连接成功
    cursor.execute("DROP TABLE IF EXISTS pop_type_movie")

    # rankId VARCHAR(100),
    sql = """CREATE TABLE pop_type_movie (
    name VARCHAR(100),
    value VARCHAR(100))"""

    cursor.execute(sql)  # 根据需要创建一个表格

    for i in range(len(pop_type)):
        insert20 = "insert into pop_type_movie( name, value) value( '%s','%s')" % (
            pop_type[i]['name'], pop_type[i]['value'])
        # print(insert20)
        # pop_type[i]['rankId'],
        cursor.execute(insert20)

    print("————————存入数据库完成————")
    cursor.close()
    db.commit()
    db.close()
    '''except Exception as e:
        db.rollback()
        print(str(e))
        break'''


def data_insert_movie_map(movie_map):
    db = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='BoxOfficeDB',
                         charset='utf8')
    # 拿到游标
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")

    data = cursor.fetchone()

    # print("Database version : '%s' " % data)
    # 结果表明已经连接成功
    cursor.execute("DROP TABLE IF EXISTS movie_map_table")

    sql = """CREATE TABLE movie_map_table (
    name VARCHAR(100),
    value VARCHAR(100))"""

    cursor.execute(sql)  # 根据需要创建一个表格

    for i in range(len(movie_map)):
        insert20 = "insert into movie_map_table( name, value) value('%s', '%s')" % (
            movie_map[i]['name'], movie_map[i]['value'])
        # print(insert20)
        cursor.execute(insert20)

    print("————————存入数据库完成————")
    cursor.close()
    db.commit()
    db.close()
    '''except Exception as e:
        db.rollback()
        print(str(e))
        break'''


def data_insert_movie_actor(movie_actor):
    db = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='BoxOfficeDB',
                         charset='utf8')
    # 拿到游标
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")

    data = cursor.fetchone()

    # print("Database version : '%s' " % data)
    # 结果表明已经连接成功
    cursor.execute("DROP TABLE IF EXISTS movie_actor_table")

    sql = """CREATE TABLE movie_actor_table (
    name VARCHAR(100),
    value VARCHAR(100))"""

    cursor.execute(sql)  # 根据需要创建一个表格

    for i in range(len(movie_actor)):
        insert20 = "insert into movie_actor_table( name, value) value( '%s', '%s')" % (
            movie_actor[i]['name'], movie_actor[i]['value'])
        # print(insert20)
        cursor.execute(insert20)

    print("————————存入数据库完成————")
    cursor.close()
    db.commit()
    db.close()
    '''except Exception as e:
        db.rollback()
        print(str(e))
        break'''


def data_insert_movie_country(movie_country):
    db = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='BoxOfficeDB',
                         charset='utf8')
    # 拿到游标
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")

    data = cursor.fetchone()

    # print("Database version : '%s' " % data)
    # 结果表明已经连接成功
    cursor.execute("DROP TABLE IF EXISTS movie_country_table")

    sql = """CREATE TABLE movie_country_table (
    name VARCHAR(100),
    value VARCHAR(100))"""

    cursor.execute(sql)  # 根据需要创建一个表格

    for i in range(len(movie_country)):
        insert20 = "insert into movie_country_table( name, value) value( '%s', '%s')" % (
            movie_country[i]['name'], movie_country[i]['value'])
        # print(insert20)
        cursor.execute(insert20)

    print("————————存入数据库完成————")
    cursor.close()
    db.commit()
    db.close()
    '''except Exception as e:
        db.rollback()
        print(str(e))
        break'''


def data_insert_movie30_actor(movie30_actor):
    db = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='BoxOfficeDB',
                         charset='utf8')
    # 拿到游标
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")

    data = cursor.fetchone()

    # print("Database version : '%s' " % data)
    # 结果表明已经连接成功
    cursor.execute("DROP TABLE IF EXISTS movie30_actor_table")

    sql = """CREATE TABLE movie30_actor_table (
    name VARCHAR(100),
    value VARCHAR(100))"""

    cursor.execute(sql)  # 根据需要创建一个表格

    for i in range(len(movie30_actor)):
        insert20 = "insert into movie30_actor_table( name, value) value( '%s', '%s')" % (
            movie30_actor[i]['name'], movie30_actor[i]['value'])
        # print(insert20)
        cursor.execute(insert20)

    print("————————存入数据库完成————")
    cursor.close()
    db.commit()
    db.close()
    '''except Exception as e:
        db.rollback()
        print(str(e))
        break'''


if __name__ == "__main__":  # 起到一个初始化或者调用函数的作用

    a = get_pop_type()
    b = get_movie_map()
    c = get_movie_actor()
    d = get_movie_country()
    e = get_movie30_actor()
    data_insert_pop_type(a)
    data_insert_movie_map(b)
    data_insert_movie_actor(c)
    data_insert_movie_country(d)
    data_insert_movie30_actor(e)
