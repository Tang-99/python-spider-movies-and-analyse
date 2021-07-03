# -*- coding: utf-8 -*-

import glob
import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from spider.proxy import *
import random
import csv
import json
import sys
import codecs

labels = ['5星', '4星', '3星', '2星', '1星', '电影名称']
data = pd.read_csv("../Top20.csv", usecols=['电影名称', '口碑'])
# print(data)
# m = list(data['口碑'])
n = list(data['电影名称'])
# print(m)
# print(n)
m = data['口碑'].str.split('/', expand=True)
p = m
# print(p)
m['电影名称'] = n
# print(m)
m.to_csv('options.csv', header=labels)


