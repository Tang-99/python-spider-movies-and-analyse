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


def film_info():
    # 请求头，随机使用一个UA
    header = {
        'user-agent': random.choice(UserAgent)
    }
    film_id = 1328712

    # 1.确定url地址 设置搜索链接页面url
    url = 'http://piaofang.maoyan.com/movie/' + str(film_id)
    time.sleep(random.random() + 1)
    response = requests.get(url=url, headers=header, verify=False)  # 将对url进行请求后的返回值赋予response
    # response.raise_for_status()
    # response.encoding = response.apparent_encoding
    print(response.text)
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


    ztitle = soup.find("span", attrs={"class": "info-title-content"}).get_text()
    movie_ztitle.append(ztitle)
    print(ztitle)


    etitle = soup.find("span", attrs={"class": "info-etitle-content"}).get_text()
    movie_etitle.append(etitle)
    print(etitle)

    img = soup.find("img", attrs={"class": "need-handle-pic"}).get('src')
    movie_img.append(img)
    # print(img)

    cat = soup.find("p", attrs={"class": "info-category"}).get_text()
    movie_category.append(cat)
    # print(cat)

    sor = soup.find("span", attrs={"class": "score-info ellipsis-1"}).get_text()
    movie_source.append(sor)
    # print(sor)

    id = film_id
    movie_id.append(id)
    # print(id)

    male = soup.find("div", attrs={"class": "persona-line-item male"}).get_text()
    ob_male.append(male)
    # print(male)

    female = soup.find("div", attrs={"class": "persona-line-item female"}).get_text()
    ob_female.append(female)
    # print(female)

    city = soup.find("div", attrs={"class": "persona-block hotarea"}).get_text()
    ob_city.append(city)
    # print(city)

    return movie_ztitle, movie_etitle, movie_img, movie_category, movie_source, movie_id, ob_male, ob_female, ob_city


if __name__ == '__main__':
    film_info()
