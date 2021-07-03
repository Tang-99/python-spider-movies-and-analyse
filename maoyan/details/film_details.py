# -*- coding: utf-8 -*-
import csv
import json
import sys
import codecs
import requests
import time
import random

from requests.packages.urllib3.exceptions import InsecureRequestWarning

from bs4 import BeautifulSoup

from spider.proxy import *
import jsonpath
import json
import pymysql
import os
import pandas as pd
from lxml import etree


def trans16():
    f = open('../2016票房排行榜.json')
    data = json.load(f)
    datalist = data.get('list')
    Id16 = []
    for i in range(len(datalist)):
        Id16.append(datalist[i]['movieId'])
    # print(Id16)
    f.close()
    return Id16


def trans17():
    f = open('../2017票房排行榜.json')
    data = json.load(f)
    datalist = data.get('list')
    Id17 = []
    for i in range(len(datalist)):
        Id17.append(datalist[i]['movieId'])
    # print(Id16)
    f.close()
    return Id17


def trans18():
    f = open('../2018票房排行榜.json')
    data = json.load(f)
    datalist = data.get('list')
    Id18 = []
    for i in range(len(datalist)):
        Id18.append(datalist[i]['movieId'])
    # print(Id16)
    f.close()
    return Id18


def trans19():
    f = open('../2019票房排行榜.json')
    data = json.load(f)
    datalist = data.get('list')
    Id19 = []
    for i in range(len(datalist)):
        Id19.append(datalist[i]['movieId'])
    # print(Id16)
    f.close()
    return Id19


def trans20():
    f = open('../2020票房排行榜.json')
    data = json.load(f)
    datalist = data.get('list')
    Id20 = []
    for i in range(len(datalist)):
        Id20.append(datalist[i]['movieId'])
    # print(Id16)
    f.close()
    return Id20


def read_ip():
    """
    读取代理池，返回ip:port列表
    :return: list
    """
    # 最新爬虫数据文件名（列表推导式写法）
    file_name = [f for f in os.listdir("../../proxy_pool/") if f.split('.')[-1] == 'xlsx'][-1]
    # 读取文件
    proxy_list = pd.read_excel('../../proxy_pool/' + file_name)
    proxy_list['port'] = proxy_list['port'].astype('str')  # 先将端口号的整型转为字符串
    proxy_list['ip_port'] = proxy_list['ip'].str.cat(proxy_list['port'], sep=':')  # 组合成ip+port
    # print(list(proxy_list['ip_port']))
    return list(proxy_list['ip_port'])


def film_info(film_id, ip_port):
    # 请求头，随机使用一个UA
    header = {
        'user-agent': random.choice(UserAgent)
    }
    proxy_ip = 'http://' + ip_port
    proxies = {'http': proxy_ip}
    print(proxies)

    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    # 1.确定url地址 设置搜索链接页面url
    url = 'https://piaofang.maoyan.com/movie/' + str(film_id)
    time.sleep(10 * random.random() + 10)
    timeouts = 10 * random.random() + 10
    response = requests.get(url=url, headers=header, proxies=proxies, verify=False,
                            timeout=timeouts)  # 将对url进行请求后的返回值赋予response
    response.raise_for_status()
    response.encoding = response.apparent_encoding
    # print(response.text)
    soup = BeautifulSoup(response.text, "html.parser")

    movie_ztitle = []
    movie_etitle = []
    movie_img = []
    movie_category = []
    movie_source = []
    movie_id = []
    ob_male = []
    ob_female = []
    ob_city = []
    try:
        ztitle = soup.find("span", attrs={"class": "info-title-content"}).get_text()
        movie_ztitle.append(ztitle)
        print(ztitle)
    except:
        movie_ztitle.append('')

    try:
        etitle = soup.find("span", attrs={"class": "info-etitle-content"}).get_text()
        movie_etitle.append(etitle)
        # print(etitle)
    except:
        movie_etitle.append('')

    try:
        img = soup.find("img", attrs={"class": "need-handle-pic"}).get('src')
        movie_img.append(img)
        # print(img)
    except:
        movie_img.append('')

    try:
        cat = soup.find("p", attrs={"class": "info-category"}).get_text()
        movie_category.append(cat)
        # print(cat)
    except:
        movie_category.append('')

    try:
        sor = soup.find("span", attrs={"class": "score-info ellipsis-1"}).get_text()
        movie_source.append(sor)
        # print(sor)
    except:
        movie_source.append('')

    idf = film_id
    movie_id.append(idf)
    # print(idf)

    try:
        male = soup.find("div", attrs={"class": "persona-line-item male"}).get_text()
        ob_male.append(male)
        # print(male)
    except:
        ob_male.append('')

    try:
        female = soup.find("div", attrs={"class": "persona-line-item female"}).get_text()
        ob_female.append(female)
        # print(female)
    except:
        ob_female.append('')

    try:
        city = soup.find("div", attrs={"class": "persona-block hotarea"}).get_text()
        ob_city.append(city)
        # print(city)
    except:
        ob_city.append('')

    return movie_ztitle, movie_etitle, movie_img, movie_category, movie_source, movie_id, ob_male, ob_female, ob_city


# , ob_male, ob_female, ob_city


def film_to_csv(Id16, Id17, Id18, Id19, Id20, ip_port):
    movies = film_info(246063, random.choice(ip_port))
    print(random.choice(ip_port))
    movies_1 = pd.DataFrame(
        {'中文名': movies[0], '英文名': movies[1], '图片': movies[2], '类别': movies[3], '地区': movies[4], '电影编号': movies[5],
         '观影男性': movies[6], '观影女性': movies[7], '观影城市': movies[8]})
    # '观影男性': movies[6], '观影女性': movies[7], '观影城市': movies[8]

    idList = [246307, 246390, 78536, 246177, 247575]
    for film_id in Id20:
        movies = film_info(film_id, random.choice(ip_port))
        print(film_id)
        movies_1 = movies_1.append(pd.DataFrame(
            {'中文名': movies[0], '英文名': movies[1], '图片': movies[2], '类别': movies[3], '地区': movies[4], '电影编号': movies[5],
             '观影男性': movies[6], '观影女性': movies[7], '观影城市': movies[8]}))
        print(movies_1)
    all_movies = movies_1
    csv_file_1 = all_movies.to_csv("maoyan_20.csv", encoding='utf-8')
    #   '观影男性': movies[6], '观影女性': movies[7], '观影城市': movies[8]


if __name__ == '__main__':
    a = trans16()
    b = trans17()
    c = trans18()
    d = trans19()
    e = trans20()
    # film_info()
    f = read_ip()
    film_to_csv(a, b, c, d, e, f)
