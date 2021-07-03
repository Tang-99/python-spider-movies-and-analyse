# -*- coding: utf-8 -*-
import os
import random
import time

import pandas as pd
import requests
from bs4 import BeautifulSoup
from lxml import etree
from requests import exceptions

from spider.proxy import *


def get_movies(m_id):
    id = str(m_id)
    # 目标url
    url = "https://movie.douban.com/subject/" + id + "/"
    headers = {  # 这是请求头
        'User-Agent': random.choice(UserAgent)
    }
    # 爬取某些网页可能速度极慢，影响性能。设置超时时间。
    # timeout单位秒
    html_code = requests.get(url, headers=headers, timeout=5)
    # 采用bs众多html.parser 进行网页元素的采集
    soup = BeautifulSoup(html_code.text, "html.parser")
    movie_types = []
    movie_name = []
    movie_score = []
    movie_dic = []
    movie_act = []
    movie_info = []
    movie_com = []
    movie_opinions = []
    movie_imgs = []
    list1 = []
    list2 = []
    list3 = []

    # 获取元素并转为文本
    name = soup.find("span", attrs={"property": "v:itemreviewed"}).get_text()
    movie_name.append(name)

    pf = soup.find("strong", attrs={"property": "v:average"}).get_text()
    movie_score.append(pf)

    dy = soup.find("a", attrs={"rel": "v:directedBy"}).get_text()
    movie_dic.append(dy)

    jqjj = soup.find("span", attrs={"property": "v:summary"}).get_text()
    movie_info.append(jqjj)

    plrs = soup.find("span", attrs={"property": "v:votes"}).get_text()
    movie_com.append(plrs)

    # find_all 返回的是list 需要对其进行遍历输出
    yy = soup.find_all("a", attrs={"rel": "v:starring"})
    for item in yy:
        list2.append(item.get_text())
    # print(list2)
    # 以 / 分隔
    data2 = "/".join(list2)
    movie_act.append(data2)

    lx = soup.find_all("span", attrs={"property": "v:genre"})
    for _ in lx:
        # print(_.get_text())
        list1.append(_.get_text())
    # print(movie_types)
    data = "/".join(list1)
    # print(data)
    movie_types.append(data)

    kb = soup.find_all("span", attrs={"class": "rating_per"})
    for _ in kb:
        # print(_.get_text())
        list3.append(_.get_text().replace('%', ' '))
    # print(movie_types)
    data = "/".join(list3)
    # print(data)
    movie_opinions.append(data)

    img = soup.find("a", attrs={"class": "nbgnbg"}).img.get('src')
    movie_imgs.append((img))

    # print("电影名称：", name)
    # print("豆瓣评分：", pf)
    # print("导演：", dy)
    # print("剧情简介：", jqjj.replace("\n", "").replace(" ", "").replace("  ", "").strip())
    # print(len(lx))
    # print(yy)
    return movie_act, movie_dic, movie_info, movie_name, movie_types, movie_score, movie_com, movie_opinions, movie_imgs


m_id = 26363254
movies = get_movies(m_id)

movies_1 = pd.DataFrame(
    {'电影名称': movies[3], '电影类型': movies[4], '导演': movies[1], '主演': movies[0], '评分': movies[5], '口碑': movies[7],
     '评论人数': movies[6], '简介': movies[2], '图片': movies[8]})

for movie_id in movie_ids:
    m_id = str(movie_id)
    print(m_id)
    movies = get_movies(m_id)
    movies_1 = movies_1.append(pd.DataFrame(
        {'电影名称': movies[3], '电影类型': movies[4], '导演': movies[1], '主演': movies[0], '评分': movies[5], '口碑': movies[7],
         '评论人数': movies[6], '简介': movies[2], '图片': movies[8]}), ignore_index=True)
all_movies = movies_1
csv_file_1 = all_movies.to_csv("Top20.csv", encoding='utf-8')


def start_spider_comment():
    """
    指定需要爬取影评的影片
    :param movies_id_and_title_dict:
    :return:
    """
    if not os.path.exists('comment_data'):
        os.mkdir('comment_data')
        print("所有影评以片名名命保存在 comment_data 文件夹下...")
    number = 1
    for movie_id in movie_ids:
        print(movie_id)
        print(get_current_time() + ' ----->> 正在爬取第 ' + str(number) + '部影片')
        get_comment_info_to_cvs(movie_id)
        # get_comment_info_to_txt(movie_id, movie_name)
        number += 1
    print('====================>> Finsh time: ' + get_current_time() + ' <<====================')


def get_current_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def get_comment_info_to_cvs(movie_id):
    """
    爬取指定影片的短评并写入csv文件（文件以影片名命名）
    :param movie_id:
    :param movie_name:
    :return:
    """
    base_url = 'https://movie.douban.com/subject/' + str(movie_id) + '/comments?start='
    all_page_comments = [base_url + '{}'.format(x) for x in range(0, 401, 20)]
    headers = {  # 这是请求头
        'User-Agent': random.choice(UserAgent)
    }
    # 爬取某些网页可能速度极慢，影响性能。设置超时时间。
    # timeout单位秒
    filename = str(movie_id) + '.csv'
    filepath = os.path.join('comment_data', filename)
    number = 1
    for each_page in all_page_comments:
        try:
            timeouts = 600 * random.random()
            html = requests.get(each_page, headers=headers, timeout=timeouts)
            selector = etree.HTML(html.text)
            comments = selector.xpath("//div[@class='comment']")
            comments_all = []
            for each in comments:
                comments_all.append(get_comments(each))
            data = pd.DataFrame(comments_all)
            # 写入csv文件
            try:
                if number == 1:
                    csv_headers = ['用户', '是否看过', '评分', '评论时间', '有用数', '评论']
                    data.to_csv(filepath, header=csv_headers, index=False, mode='a+', encoding="utf-8")
                    number += 1
                else:
                    data.to_csv(filepath, header=False, index=False, mode='a+', encoding="utf-8")
            except UnicodeEncodeError:
                print("编码错误, 跳过...")
            data = []
        except:
            # print('跳过一个页面')
            continue


def get_comments(eachComment):
    commentlist = []
    user = eachComment.xpath("./h3/span[@class='comment-info']/a/text()")[0]  # 用户
    watched = eachComment.xpath("./h3/span[@class='comment-info']/span[1]/text()")[0]  # 是否看过
    rating = eachComment.xpath("./h3/span[@class='comment-info']/span[2]/@title")  # 五星评分
    if len(rating) > 0:
        rating = rating[0]

    comment_time = eachComment.xpath("./h3/span[@class='comment-info']/span[3]/@title")  # 评论时间
    if len(comment_time) > 0:
        comment_time = comment_time[0]
    else:
        comment_time = ' '

    votes = eachComment.xpath("./h3/span[@class='comment-vote']/span/text()")[0]  # "有用"数
    content = eachComment.xpath("./p/span/text()")[0]  # 评论内容

    commentlist.append(user)
    commentlist.append(watched)
    commentlist.append(rating)
    commentlist.append(comment_time)
    commentlist.append(votes)
    commentlist.append(content.strip())
    print(commentlist)
    return commentlist


if __name__ == '__main__':
    get_movies(m_id)

    # start_spider_comment()
