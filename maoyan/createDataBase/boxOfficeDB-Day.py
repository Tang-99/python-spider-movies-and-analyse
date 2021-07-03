# create day boxoffice database
# -*- coding: UTF-8 -*-
import json
import pymysql


def get_firstday():
    with open('/spider/影片首日票房榜.json', 'r') as f:
        res = json.load(f)  # 解析每一行数据
        firstday = res.get('data')
        fday = firstday.get('list')
        # 添加序号
        for i in range(len(fday)):
            fday[i]['rankId'] = i
        # print(firstday)
    print("————————读取数据完成————")
    return fday


def get_oneday():
    with open('/spider/影片单日票房榜.json', 'r') as f:
        res = json.load(f)  # 解析每一行数据
        one = res.get('data')
        oneday = one.get('list')
        for i in range(len(oneday)):
            oneday[i]['rankId'] = i
        # print(firstday)
    print("————————读取数据完成————")
    return oneday


def data_insertfirst(fday):
    db = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='BoxOfficeDB',
                         charset='utf8')
    # 拿到游标
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")

    data = cursor.fetchone()

    # print("Database version : '%s' " % data)
    # 结果表明已经连接成功
    cursor.execute("DROP TABLE IF EXISTS Box_Office_First_Day")

    sql = """CREATE TABLE Box_Office_First_Day (
    rankId INT ,
    movieId VARCHAR(100),
    movieName VARCHAR(100),
    weekDayInfo VARCHAR(100),
    boxDesc VARCHAR(100),
    releaseInfo VARCHAR(100))"""

    cursor.execute(sql)  # 根据需要创建一个表格

    for i in range(len(fday)):
        insert20 = "insert into Box_Office_First_Day(rankId, movieId, movieName, weekDayInfo, boxDesc, releaseInfo) value('%s','%s','%s','%s','%s','%s')" % (
            fday[i]['rankId'], fday[i]['movieId'], fday[i]['movieName'], fday[i]['weekDayInfo'],
            fday[i]['boxDesc'], fday[i]['releaseInfo'])
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


def data_insertone(oneday):
    db = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='BoxOfficeDB',
                         charset='utf8')
    # 拿到游标
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")

    data = cursor.fetchone()

    # print("Database version : '%s' " % data)
    # 结果表明已经连接成功
    cursor.execute("DROP TABLE IF EXISTS Box_Office_One_Day")

    sql = """CREATE TABLE Box_Office_One_Day (
    rankId INT ,
    movieId VARCHAR(100),
    movieName VARCHAR(100),
    weekDayInfo VARCHAR(100),
    boxDesc VARCHAR(100),
    releaseDays VARCHAR(100),
    releaseInfo VARCHAR(100))"""

    cursor.execute(sql)  # 根据需要创建一个表格

    for i in range(len(oneday)):
        insert20 = "insert into Box_Office_One_Day(rankId, movieId, movieName, weekDayInfo, boxDesc, releaseDays, releaseInfo) value('%s','%s','%s','%s','%s','%s','%s')" % (
            oneday[i]['rankId'], oneday[i]['movieId'], oneday[i]['movieName'], oneday[i]['weekDayInfo'],
            oneday[i]['boxDesc'], oneday[i]['releaseDays'], oneday[i]['releaseInfo'])
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
    a = get_firstday()
    b = get_oneday()
    data_insertfirst(a)
    data_insertone(b)
