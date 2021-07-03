# -*- coding: utf-8 -*-
import glob
import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
from spider.proxy import *
import random
import csv
import json
import sys
import codecs


def trans16():
    f = open('../2016票房排行榜.json')
    data = json.load(f)
    data = data.get('list')
    # print(data)
    f.close()

    f = codecs.open('2016票房排行榜.csv', 'w', 'utf_8_sig')  # 解决写入csv时中文乱码
    writer = csv.writer(f)
    writer.writerow(["boxDesc", "movieId", "movieName"])
    for item in data:
        writer.writerow([item['boxDesc'], item['movieId'], item['movieName']])
    f.close()
    print("转换完成")

    # df = pd.read_csv('2016票房排行榜.csv', sep=',', encoding='utf-8')
    # print(df)
    # df.to_csv('2016票房排行榜.csv')


def trans17():
    f = open('../2017票房排行榜.json')
    data = json.load(f)
    data = data.get('list')
    # print(data)
    f.close()

    f = codecs.open('2017票房排行榜.csv', 'w', 'utf_8_sig')  # 解决写入csv时中文乱码
    writer = csv.writer(f)
    writer.writerow(["boxDesc", "movieId", "movieName"])
    for item in data:
        writer.writerow([item['boxDesc'], item['movieId'], item['movieName']])
    f.close()
    print("转换完成")


def trans18():
    f = open('../2018票房排行榜.json')
    data = json.load(f)
    data = data.get('list')
    # print(data)
    f.close()

    f = codecs.open('2018票房排行榜.csv', 'w', 'utf_8_sig')  # 解决写入csv时中文乱码
    writer = csv.writer(f)
    writer.writerow(["boxDesc", "movieId", "movieName"])
    for item in data:
        writer.writerow([item['boxDesc'], item['movieId'], item['movieName']])
    f.close()
    print("转换完成")


def trans19():
    f = open('../2019票房排行榜.json')
    data = json.load(f)
    data = data.get('list')
    # print(data)
    f.close()

    f = codecs.open('2019票房排行榜.csv', 'w', 'utf_8_sig')  # 解决写入csv时中文乱码
    writer = csv.writer(f)
    writer.writerow(["boxDesc", "movieId", "movieName"])
    for item in data:
        writer.writerow([item['boxDesc'], item['movieId'], item['movieName']])
    f.close()
    print("转换完成")


def trans20():
    f = open('../2020票房排行榜.json')
    data = json.load(f)
    data = data.get('list')
    # print(data)
    f.close()

    f = codecs.open('2020票房排行榜.csv', 'w', 'utf_8_sig')  # 解决写入csv时中文乱码
    writer = csv.writer(f)
    writer.writerow(["boxDesc", "movieId", "movieName"])
    for item in data:
        writer.writerow([item['boxDesc'], item['movieId'], item['movieName']])
    f.close()
    print("转换完成")


if __name__ == '__main__':
    trans16()
    trans17()
    trans18()
    trans19()
    trans20()
