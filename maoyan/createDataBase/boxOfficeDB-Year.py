# create year boxoffice database
# -*- coding: UTF-8 -*-
import json
import pymysql


# 读取json数据，并写入数据库
def get_data20():
    with open('../2020票房排行榜.json', 'r') as f:
        res = json.load(f)  # 解析每一行数据
        # print(text_2020)
        res.pop('list')  # 取出json中的list表单
        res['listId'] = 1
        text20 = res
    print('————读取完成————')
    return text20


def get_data19():
    with open('../2019票房排行榜.json', 'r') as f:
        res = json.load(f)  # 解析每一行数据
        res.pop('list')
        res['listId'] = 2
        text19 = res
    print('————读取完成————')
    return text19


def get_data18():
    with open('../2018票房排行榜.json', 'r') as f:
        res = json.load(f)  # 解析每一行数据
        res.pop('list')
        res['listId'] = 3
        text18 = res
    print('————读取完成————')
    return text18


def get_data17():
    with open('../2017票房排行榜.json', 'r') as f:
        res = json.load(f)  # 解析每一行数据
        res.pop('list')
        res['listId'] = 4
        text17 = res
    print('————读取完成————')
    return text17


def get_data16():
    with open('../2016票房排行榜.json', 'r') as f:
        res = json.load(f)  # 解析每一行数据
        res.pop('list')
        res['listId'] = 5
        text16 = res
    print('————读取完成————')
    return text16


def data_insert20(text20):
    db = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='BoxOfficeDB',
                         charset='utf8')
    # 拿到游标
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")

    data = cursor.fetchone()

    print("Database version : '%s' " % data)
    # 结果表明已经连接成功
    cursor.execute("DROP TABLE IF EXISTS Year_Box_Office")

    sql = """CREATE TABLE Year_Box_Office (
    listId INT ,
    majorTitle VARCHAR(100),
    minorTitle VARCHAR(100))"""

    cursor.execute(sql)  # 根据需要创建一个表格


    insert20 = "insert into Year_Box_Office(listId, majorTitle, minorTitle) value('%s', '%s','%s')" % (
        text20['listId'], text20['majorTitle'], text20['minorTitle'])
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

    insert19 = "insert into Year_Box_Office(listId, majorTitle, minorTitle) value('%s','%s','%s')" % (
        text19['listId'], text19['majorTitle'], text19['minorTitle'])
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

    insert18 = "insert into Year_Box_Office(listId, majorTitle, minorTitle) value('%s', '%s','%s')" % (
        text18['listId'], text18['majorTitle'], text18['minorTitle'])
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

    insert17 = "insert into Year_Box_Office(listId, majorTitle, minorTitle) value('%s', '%s','%s')" % (
        text17['listId'], text17['majorTitle'], text17['minorTitle'])
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

    insert16 = "insert into Year_Box_Office(listId, majorTitle, minorTitle) value('%s', '%s','%s')" % (
        text16['listId'], text16['majorTitle'], text16['minorTitle'])
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
