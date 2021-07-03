# -*- coding: utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
from spider.proxy import *
import random
import json
import csv


def get_movies(link):
    headers = {  # 这是请求头
        'User-Agent': random.choice(UserAgent)
    }
    movie_names = []
    movie_types = []
    movie_dis = []
    movie_grade = []
    movie_addr = []
    movie_actor = []
    movie_director = []
    movie_year = []
    movie_img = []
    r = requests.get(link, headers=headers, timeout=10)

    # 根据网页特点 选取bs 的 lxml进行元素获取
    #  lxml 支持HTML和XML的解析，支持XPath解析方式，且解析效率很高
    # Element是XML处理的核心类，Element对象可以直观的理解为XML的节点，大部分XML节点的处理都是围绕该类进行的。
    soup = BeautifulSoup(r.text, "lxml")

    for each in soup.find_all('div', class_='abstract'):
        a = each.text
        # .匹配任意字符，除了换行符
        # * 选择所有元素节点与元素名
        tp = re.search(r'类型: (.*)', a)
        if tp == None:
            movie_types.append(" ")
        else:
            movie_types.append(tp.group(1))
        actor = re.search(r'主演: (.*)', a)
        if actor == None:
            movie_actor.append(" ")
        else:
            movie_actor.append(actor.group(1))
        director = re.search(r'导演: (.*)', a)
        if director == None:
            movie_director.append(" ")
        else:
            movie_director.append(director.group(1))
        addr = re.search(r'制片国家/地区: (.*)', a)
        if addr == None:
            movie_addr.append(" ")
        else:
            movie_addr.append(addr.group(1))
        # 将具体年份转为年代 e.g 1998年 转为20世纪90年代
        year = re.search(r'年份: (.*)', a)
        if year == None:
            movie_year.append(" ")
        else:
            year_str = year.group(1)
            sj = int(year_str[:2]) + 1
            nd = year_str[2] + '0'
            movie_year.append(str(sj) + '世纪' + nd + '年代')

    # 查询所有class=title的div
    div_list = soup.find_all('div', class_='title')
    for each in div_list:
        movie_name = each.a.text.strip()  # 在div中，a标签的text的内容就是中文电影名称
        movie_names.append(movie_name)
    for each in soup.find_all('div', class_='rating'):
        a = each.text.split('\n')  # 在div中，第三个span的text的内容就是评价人数
        # 获取字符串中的数字
        x = re.sub("\D", "", a[3])
        movie_dis.append(int(x))
        movie_grade.append(float(a[2]))
    for each in soup.find_all('div', class_='post'):
        post = each.a.img.get('src')
        movie_img.append(post)

    return movie_names, movie_types, movie_dis, movie_grade, movie_addr, movie_actor, movie_director, movie_year, movie_img


def get_mshang():
    # link = "https://www.douban.com/doulist/240962/"
    movies = get_movies("https://www.douban.com/doulist/240962/")
    movies_1 = pd.DataFrame(
        {'电影名称': movies[0], '电影类型': movies[1], '导演': movies[6], '主演': movies[5], '评价人数': movies[2], '评分': movies[3],
         '国家/地区': movies[4], '年代': movies[7], '图片': movies[8]})
    for i in range(1, 19):
        # 总共19页，一页25个
        link = "https://www.douban.com/doulist/240962/?start=" + str(i * 25)
        movies = get_movies(link)
        movies_1 = movies_1.append(pd.DataFrame(
            {'电影名称': movies[0], '电影类型': movies[1], '导演': movies[6], '主演': movies[5], '评价人数': movies[2], '评分': movies[3],
             '国家/地区': movies[4], '年代': movies[7], '图片': movies[8]}), ignore_index=True)
    all_movies = movies_1

    csv_file_1 = all_movies.to_csv("E:/pythonsoft/spider/douban/combine/高分榜上.csv", encoding='utf-8')


def get_mzhong():
    movies = get_movies("https://www.douban.com/doulist/243559/")
    movies_2 = pd.DataFrame(
        {'电影名称': movies[0], '电影类型': movies[1], '导演': movies[6], '主演': movies[5], '评价人数': movies[2], '评分': movies[3],
         '国家/地区': movies[4], '年代': movies[7], '图片': movies[8]})
    for i in range(1, 11):
        # 总共11页，一页25个
        link = "https://www.douban.com/doulist/243559/?start=" + str(i * 25)
        movies = get_movies(link)
        movies_2 = movies_2.append(pd.DataFrame(
            {'电影名称': movies[0], '电影类型': movies[1], '导演': movies[6], '主演': movies[5], '评价人数': movies[2], '评分': movies[3],
             '国家/地区': movies[4], '年代': movies[7], '图片': movies[8]}), ignore_index=True)
    all_movies = movies_2

    csv_file_2 = all_movies.to_csv("E:/pythonsoft/spider/douban/combine/高分榜中.csv", encoding='utf-8')


def get_mxia():
    movies = get_movies("https://www.douban.com/doulist/248893/")
    movies_3 = pd.DataFrame(
        {'电影名称': movies[0], '电影类型': movies[1], '导演': movies[6], '主演': movies[5], '评价人数': movies[2], '评分': movies[3],
         '国家/地区': movies[4], '年代': movies[7], '图片': movies[8]})
    for i in range(1, 6):
        # 总共6页，一页25个
        link = "https://www.douban.com/doulist/248893/?start=" + str(i * 25)
        movies = get_movies(link)
        movies_3 = movies_3.append(pd.DataFrame(
            {'电影名称': movies[0], '电影类型': movies[1], '导演': movies[6], '主演': movies[5], '评价人数': movies[2], '评分': movies[3],
             '国家/地区': movies[4], '年代': movies[7], '图片': movies[8]}), ignore_index=True)
    all_movies = movies_3

    csv_file_3 = all_movies.to_csv("E:/pythonsoft/spider/douban/combine/高分榜下.csv", encoding='utf-8')


if __name__ == '__main__':
    get_mshang()
    get_mzhong()
    get_mxia()
