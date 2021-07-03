# create database
import json
import pymysql


# 读取json数据，并写入数据库
def get_data20():
    with open('../2020票房排行榜.json', 'r') as f:
        res = json.load(f)  # 解析每一行数据
        text20 = res.get('list')
        for i in range(len(text20)):
            text20[i]['rankId'] = i
        # print(text20)
    print("————————读取数据完成————")
    return text20


def get_data19():
    with open('../2019票房排行榜.json', 'r') as f:
        res = json.load(f)  # 解析每一行数据
        text19 = res.get('list')
        for i in range(len(text19)):
            text19[i]['rankId'] = i
        # print(text19)
    print("————————读取数据完成————")
    return text19


def get_data18():
    with open('../2018票房排行榜.json', 'r') as f:
        res = json.load(f)  # 解析每一行数据
        text18 = res.get('list')
        for i in range(len(text18)):
            text18[i]['rankId'] = i
        # print(text18)
    print("————————读取数据完成————")
    return text18


def get_data17():
    with open('../2017票房排行榜.json', 'r') as f:
        res = json.load(f)  # 解析每一行数据
        text17 = res.get('list')
        for i in range(len(text17)):
            text17[i]['rankId'] = i
        # print(text17)
    print("————————读取数据完成————")
    return text17


def get_data16():
    with open('../2016票房排行榜.json', 'r') as f:
        res = json.load(f)  # 解析每一行数据
        text16 = res.get('list')
        for i in range(len(text16)):
            text16[i]['rankId'] = i
        # print(text16)
    print("————————读取数据完成————")
    return text16


def data_insert20(text20):
    db = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='BoxOfficeDB',
                         charset='utf8')
    # 拿到游标
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")

    data = cursor.fetchone()

    # print("Database version : '%s' " % data)
    # 结果表明已经连接成功
    cursor.execute("DROP TABLE IF EXISTS Box_Office_2020")

    sql = """CREATE TABLE Box_Office_2020 (
    rankId INT ,
    avgShowViewDesc VARCHAR(100),
    avgViewBoxDesc VARCHAR(100),
    boxDesc VARCHAR(100),
    movieId VARCHAR(100)  ,
    movieName VARCHAR(100),
    releaseInfo VARCHAR(100))"""

    cursor.execute(sql)  # 根据需要创建一个表格

    for i in range(len(text20)):
        insert20 = "insert into Box_Office_2020(rankId, avgShowViewDesc, avgViewBoxDesc, boxDesc, movieId, movieName, releaseInfo) value('%s', '%s','%s','%s','%s','%s','%s')" % (
            text20[i]['rankId'], text20[i]['avgShowViewDesc'], text20[i]['avgViewBoxDesc'], text20[i]['boxDesc'],
            text20[i]['movieId'], text20[i]['movieName'], text20[i]['releaseInfo'])
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


def data_insert19(text19):
    db = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='BoxOfficeDB',
                         charset='utf8')
    # 拿到游标
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")

    data = cursor.fetchone()

    # print("Database version : '%s' " % data)
    # 结果表明已经连接成功
    cursor.execute("DROP TABLE IF EXISTS Box_Office_2019")

    sql = """CREATE TABLE Box_Office_2019 (
    rankId INT ,
    avgShowViewDesc VARCHAR(100),
    avgViewBoxDesc VARCHAR(100),
    boxDesc VARCHAR(100),
    movieId VARCHAR(100)  ,
    movieName VARCHAR(100),
    releaseInfo VARCHAR(100))"""

    cursor.execute(sql)  # 根据需要创建一个表格

    for i in range(len(text19)):
        insert19 = "insert into Box_Office_2019(rankId, avgShowViewDesc, avgViewBoxDesc, boxDesc, movieId, movieName, releaseInfo) value('%s', '%s','%s','%s','%s','%s','%s')" % (
            text19[i]['rankId'], text19[i]['avgShowViewDesc'], text19[i]['avgViewBoxDesc'], text19[i]['boxDesc'],
            text19[i]['movieId'], text19[i]['movieName'], text19[i]['releaseInfo'])
        # print(insert19)
        cursor.execute(insert19)

    print("————————存入数据库完成————")
    cursor.close()
    db.commit()
    db.close()
    '''except Exception as e:
        db.rollback()
        print(str(e))
        break'''


def data_insert18(text18):
    db = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='BoxOfficeDB',
                         charset='utf8')
    # 拿到游标
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")

    data = cursor.fetchone()

    # print("Database version : '%s' " % data)
    # 结果表明已经连接成功
    cursor.execute("DROP TABLE IF EXISTS Box_Office_2018")

    sql = """CREATE TABLE Box_Office_2018 (
    rankId INT ,
    avgShowViewDesc VARCHAR(100),
    avgViewBoxDesc VARCHAR(100),
    boxDesc VARCHAR(100),
    movieId VARCHAR(100)  ,
    movieName VARCHAR(100),
    releaseInfo VARCHAR(100))"""

    cursor.execute(sql)  # 根据需要创建一个表格

    for i in range(len(text18)):
        insert18 = "insert into Box_Office_2018(rankId, avgShowViewDesc, avgViewBoxDesc, boxDesc, movieId, movieName, releaseInfo) value('%s', '%s','%s','%s','%s','%s','%s')" % (
            text18[i]['rankId'], text18[i]['avgShowViewDesc'], text18[i]['avgViewBoxDesc'], text18[i]['boxDesc'],
            text18[i]['movieId'], text18[i]['movieName'], text18[i]['releaseInfo'])
        # print(insert18)
        cursor.execute(insert18)

    print("————————存入数据库完成————")
    cursor.close()
    db.commit()
    db.close()
    '''except Exception as e:
        db.rollback()
        print(str(e))
        break'''


def data_insert17(text17):
    db = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='BoxOfficeDB',
                         charset='utf8')
    # 拿到游标
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")

    data = cursor.fetchone()

    # print("Database version : '%s' " % data)
    # 结果表明已经连接成功
    cursor.execute("DROP TABLE IF EXISTS Box_Office_2017")

    sql = """CREATE TABLE Box_Office_2017 (
    rankId INT ,
    avgShowViewDesc VARCHAR(100),
    avgViewBoxDesc VARCHAR(100),
    boxDesc VARCHAR(100),
    movieId VARCHAR(100)  ,
    movieName VARCHAR(100),
    releaseInfo VARCHAR(100))"""

    cursor.execute(sql)  # 根据需要创建一个表格

    for i in range(len(text17)):
        insert17 = "insert into Box_Office_2017(rankId, avgShowViewDesc, avgViewBoxDesc, boxDesc, movieId, movieName, releaseInfo) value('%s', '%s','%s','%s','%s','%s','%s')" % (
            text17[i]['rankId'], text17[i]['avgShowViewDesc'], text17[i]['avgViewBoxDesc'], text17[i]['boxDesc'],
            text17[i]['movieId'], text17[i]['movieName'], text17[i]['releaseInfo'])
        # print(insert17)
        cursor.execute(insert17)

    print("————————存入数据库完成————")
    cursor.close()
    db.commit()
    db.close()
    '''except Exception as e:
        db.rollback()
        print(str(e))
        break'''


def data_insert16(text16):
    db = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='BoxOfficeDB',
                         charset='utf8')
    # 拿到游标
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")

    data = cursor.fetchone()

    # print("Database version : '%s' " % data)
    # 结果表明已经连接成功
    cursor.execute("DROP TABLE IF EXISTS Box_Office_2016")

    sql = """CREATE TABLE Box_Office_2016 (
    rankId INT ,
    avgShowViewDesc VARCHAR(100),
    avgViewBoxDesc VARCHAR(100),
    boxDesc VARCHAR(100),
    movieId VARCHAR(100)  ,
    movieName VARCHAR(100),
    releaseInfo VARCHAR(100))"""

    cursor.execute(sql)  # 根据需要创建一个表格

    for i in range(len(text16)):
        insert16 = "insert into Box_Office_2016(rankId, avgShowViewDesc, avgViewBoxDesc, boxDesc, movieId, movieName, releaseInfo) value('%s', '%s','%s','%s','%s','%s','%s')" % (
            text16[i]['rankId'], text16[i]['avgShowViewDesc'], text16[i]['avgViewBoxDesc'], text16[i]['boxDesc'],
            text16[i]['movieId'], text16[i]['movieName'], text16[i]['releaseInfo'])
        # print(insert16)
        cursor.execute(insert16)

    print("————————存入数据库完成————")
    cursor.close()
    db.commit()
    db.close()
    '''except Exception as e:
        db.rollback()
        print(str(e))
        break'''


if __name__ == "__main__":  # 起到一个初始化或者调用函数的作用
    a = get_data20()
    b = get_data19()
    c = get_data18()
    d = get_data17()
    e = get_data16()
    data_insert20(a)
    data_insert19(b)
    data_insert18(c)
    data_insert17(d)
    data_insert16(e)
