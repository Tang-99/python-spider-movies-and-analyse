# http://piaofang.maoyan.com/mdb/rank?type=1
# -*- coding: UTF-8 -*-
# 默认编码格式 utf-8 防止读取数据， 输出数据乱码

import requests
import time
import random
from spider.proxy import *
import jsonpath
import json

# 请求头，随机使用一个UA
header = {
    'user-agent': random.choice(UserAgent)
}

# 1.确定url地址
url = 'http://piaofang.maoyan.com/mdb/rank/query?type=1&id=single'
time.sleep(random.random() + 0.2)  # 休眠0.2~1.2秒再发送请求
response = requests.get(url=url, headers=header)
res = response.content.decode()
# print(res)
# 将获取到的数据转为json格式
jsonobj = json.loads(res)


# print(jsonobj)
# 将数据写入json 文件

with open('../影片单日票房榜.json', 'w') as f:
    f.write(json.dumps(jsonobj, ensure_ascii=False, indent=4))
    # 定义json格式 缩进4个字符 因为json.dumps 序列化时对中文默认使用的ascii编码.输出真正的中文需要指定ensure_ascii=False：


url = 'http://piaofang.maoyan.com/mdb/rank/query?type=1&id=release'
time.sleep(random.random() + 0.2)  # 休眠0.2~1.2秒再发送请求
response = requests.get(url=url, headers=header)
res = response.content.decode()
# print(res)
jsonobj = json.loads(res)

# print(jsonobj)

with open('../影片首日票房榜.json', 'w') as f:
    f.write(json.dumps(jsonobj, ensure_ascii=False, indent=4))
