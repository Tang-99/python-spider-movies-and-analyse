# -*- coding: UTF-8 -*-
# 默认编码格式 utf-8 防止读取数据， 输出数据乱码

import requests
import bs4
import pandas as pd
from spider.proxy import *
import random
import time


def get_one_page(url):
    headers = {
        'User-Agent': random.choice(UserAgent)
    }
    time.sleep(random.random() + 0.2)  # 休眠0.2~1.2秒再发送请求
    response = requests.get(url, headers=headers, timeout=10)
    if response.status_code == 200:
        response.encoding = response.apparent_encoding
    return response.text


# 解析网页
def get_soup(htm):
    soup = bs4.BeautifulSoup(htm, 'html.parser')
    return soup


# 找到电影名
def find_name(soup):
    x = soup.find_all('p', class_="name")
    n = []
    for i in x:
        n.append(i.text)
    return n


# 找到电影上映时间
def get_time(soup):
    x = soup.find_all('p', class_="releasetime")
    n = []
    for i in x:
        n.append(i.text)
    return n


# 找到电影评分
def get_score(soup):
    x = soup.find_all('p', class_="score")
    n = []
    for i in x:
        if i.text is None:
            n.append(" ")
        else:
            n.append(i.text)
    return n


# 找到电影演员
def get_actor(soup):
    x = soup.find_all('p', class_="star")
    n = []
    for i in x:
        n.append(i.text)
    return n


# 找到电影图片
def get_picture(soup):
    x = soup.find_all('img', class_="board-img")
    n = []
    for i in x:
        n.append(i.get('data-src'))
    return n


def main():
    for i in range(0, 100, 10):
        time.sleep(random.random() + 10)  # 休眠0.2~1.2秒再发送请求
        url = f'https://maoyan.com/board/4?offset={i}'
        html = get_one_page(url)
        soup = get_soup(html)
        # print(soup)
        # 电影名
        name = find_name(soup)
        # 上映时间
        times = get_time(soup)
        # 评分
        score = get_score(soup)
        # 图片
        image = get_picture(soup)
        # 演员
        actor = get_actor(soup)

        # 保存csv文件
        df = pd.DataFrame({'电影名': name, '上映时间': times, '主演': actor, '图片': image})
        df.insert(2, '评分', '')
        # df = df.append(pd.DataFrame.from_dict({'电影名': name, '上映时间': times, '评分': score, '主演': actor, '图片': image}))
        # print(df)
        title = str(i) + '.csv'

        df.to_csv(title, encoding='utf-8')


if __name__ == '__main__':
    main()
