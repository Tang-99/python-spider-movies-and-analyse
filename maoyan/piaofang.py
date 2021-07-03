# http://piaofang.maoyan.com/mdb/rank

import requests
import time
import random
from spider.proxy import *
import jsonpath
import json
import pymysql
import os
import pandas as pd

# 请求头，随机使用一个UA
header = {
    'user-agent': random.choice(UserAgent)
}


# # for 循环2016 2017 2018 2019 2020
for year in range(2016, 2021):
    # 1.确定url地址 设置搜索链接页面url
    url = f'http://piaofang.maoyan.com/mdb/rank/query?type=0&id={year}'
    time.sleep(random.random() + 0.2)  # 休眠0.2~1.2秒再发送请求
    response = requests.get(url=url, headers=header, verify=False)  # 将对url进行请求后的返回值赋予response
    res = response.content.decode()  # 对response进行编码处理
    print(res)
    jsonobj = json.loads(res)

    # movieId = jsonpath.jsonpath(jsonobj, '$.data.list[*].movieId')
    # avgShowViewDesc = jsonpath.jsonpath(jsonobj, '$.data.list[*].avgShowViewDesc')
    # avgViewBoxDesc = jsonpath.jsonpath(jsonobj, '$.data.list[*].avgViewBoxDesc')
    # boxDesc = jsonpath.jsonpath(jsonobj, '$.data.list[*].boxDesc')
    # movieName = jsonpath.jsonpath(jsonobj, '$.data.list[*].movieName')
    # releaseInfo = jsonpath.jsonpath(jsonobj, '$.data.list[*].releaseInfo')

    print(jsonobj)

    # 将获取到的结果转换为py 的json格式进行数据存储
    if year == 2016:
        with open('2016票房排行榜.json', 'w') as f:
            data = jsonobj.get('data')
            # listarr = data.get('list')
            f.write(json.dumps(data, ensure_ascii=False, indent=4))
    elif year == 2017:
        with open('2017票房排行榜.json', 'w') as f:
            data = jsonobj.get('data')
            # listarr = data.get('list')
            f.write(json.dumps(data, ensure_ascii=False, indent=4))
    elif year == 2018:
        with open('2018票房排行榜.json', 'w') as f:
            data = jsonobj.get('data')
            # listarr = data.get('list')
            f.write(json.dumps(data, ensure_ascii=False, indent=4))
    elif year == 2019:
        with open('2019票房排行榜.json', 'w') as f:
            data = jsonobj.get('data')
            # listarr = data.get('list')
            f.write(json.dumps(data, ensure_ascii=False, indent=4))
    elif year == 2020:
        with open('2020票房排行榜.json', 'w') as f:
            data = jsonobj.get('data')
            # listarr = data.get('list')
            f.write(json.dumps(data, ensure_ascii=False, indent=4))
