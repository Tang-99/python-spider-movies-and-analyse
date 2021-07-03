# -*- coding: utf-8 -*-
import os
import sys
import io
from pyecharts import Line
from pyecharts import Bar
from pyecharts import Pie
import pandas as pd
from collections import Counter
from pyecharts import WordCloud
from pyecharts import Map

from spider.douban.proxy import name_map

data = pd.read_csv("E:/pythonsoft/spider/douban/combine/电影高分排行榜.csv", encoding='utf-8')  # 读取数据
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')  # 改变标准输出的默认编码


def movies_years():
    # 柱状图
    data.rename(columns={'年代': 'years'}, inplace=True)
    # 重名一下，防止因为未对中文全支持
    target_dir = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "results")
    # 设置 保存目的目录
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    #     不存在 则创建
    print("分析结果保存在 ", target_dir, " 文件夹下...")
    title = '各年代上榜影片数'
    htmlName = title + '.html'
    htmlPath = os.path.join(target_dir, htmlName)

    n = data.groupby('years').count()
    # print(n)
    x = list(n.index)
    y = list(n['评分'])
    bar = Bar(title, title_top='top', title_pos='center', width=1000, height=600)
    kwargs = dict(
        label_text_color=None,
        is_label_show=True,
        legend_orient='vertical',
        legend_pos='left',
        is_more_utils='true',
        mark_point=["max", "min"],
        is_datazoom_show=True,
        datazoom_type="both",
        datazoom_range=[10, 25],
    )
    bar.add("电影", x, y, **kwargs)
    # bar.show_config()
    # 渲染后的图表 保存在目录下
    bar.render(htmlPath)


def movies_comment():
    data.rename(columns={'年代': 'years'}, inplace=True)

    target_dir = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "results")
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    print("分析结果保存在 ", target_dir, " 文件夹下...")
    title = '评分和评价人数'
    htmlName = title + '.html'
    htmlPath = os.path.join(target_dir, htmlName)

    x = data.groupby('years')[['评价人数', '评分']].mean()
    # print(x)
    # 标准化数据，使之落在一个区间
    s = (x - x.mean()) / x.std()
    # print(s)
    p = list(s.index)
    y = list(s['评分'])
    z = list(s['评价人数'])
    line = Line(title, title_top='bottom', title_pos='center', width=1000, height=600)
    kwargs = dict(
        label_text_color=None,
        # is_label_show=True,
        legend_orient='vertical',
        legend_pos='left',
        is_more_utils='true',
        is_datazoom_show=True,
        datazoom_type="inside",
    )
    line.add("评价人数", p, z, **kwargs)
    line.add("评分", p, y)
    # bar.show_config()
    # 20世纪早期的电影观看人数较少，但评分普遍较高，了20世纪中期之后的电影观看人数开始增加，但评分却略显平庸，到了本世纪，评分才有了上涨的趋势
    line.render(htmlPath)


def movies_type():
    target_dir = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "results")
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    print("分析结果保存在 ", target_dir, " 文件夹下...")
    title = '上榜电影类型'
    htmlName = title + '.html'
    htmlPath = os.path.join(target_dir, htmlName)

    # 将电影类型按照 ‘/’ 分割，并去空格
    types = data['电影类型'].str.split('/')
    l = []
    tl = []
    for i in range(853):
        l.extend(types[i])
    for i in l:
        tl.append(i.strip())
    c = Counter(tl)
    k = list(c.keys())
    v = list(c.values())
    # print(c)
    # print(k)
    # print(v)
    # print(count)
    pie = Pie(title, title_top='bottom', title_pos='center', width=1000, height=580)
    kwargs = dict(
        radius=(0, 70),
        label_text_color=None,
        is_label_show=True,
        legend_orient='vertical',
        legend_pos='left',
        is_more_utils='true',
        center=(55, 50)
    )
    pie.add("电影类型", k, v, **kwargs)
    pie.render(htmlPath)


def movies_actor():
    data.rename(columns={'年代': 'years'}, inplace=True)
    types = data['主演'].str.split('/')
    # 数据分割
    # print(types)
    l = []
    tl = []
    for i in range(853):
        l.extend(types[i])
    for i in l:
        tl.append(i.strip())
    c = Counter(tl)
    # print(c)
    k = list(c.keys())
    # print(k)
    v = list(c.values())
    # print(v)
    target_dir = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "results")
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    print("分析结果保存在 ", target_dir, " 文件夹下...")
    title = '演员出现次数'
    htmlName = title + '.html'
    htmlPath = os.path.join(target_dir, htmlName)

    wordcloud = WordCloud(title, title_top='top', title_pos='center', width=1300, height=700)
    kwargs = dict(
        # label_text_color=None,
        # # is_label_show=True,
        # legend_orient='vertical',
        # legend_pos='left',
        is_more_utils='true',
        # mark_point=["max"],
        # is_datazoom_show=True,
        # datazoom_type="slider",
        # datazoom_range=[10, 25],
    )
    wordcloud.add("演员", k, v, **kwargs)
    # bar.show_config()v
    wordcloud.render(htmlPath)


def movies_country():
    data.rename(columns={'年代': 'years'}, inplace=True)
    types = data['国家/地区'].str.split('/')
    # print(types)
    l = []
    tl = []
    for i in range(853):
        l.extend(types[i])
    for i in l:
        tl.append(i.strip())
    c = Counter(tl)
    # print(c)
    ct = {k: v for k, v in c.items() if v > 10}
    ce = {k: v for k, v in c.items() if v > 8}
    # print(c)
    ke = list(ce.keys())

    # print(k)
    ve = list(ce.values())
    # print(v)
    target_dir = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "results")
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    print("分析结果保存在 ", target_dir, " 文件夹下...")
    title = '上榜电影数大于8部的国家和地区'
    titlet = '上榜电影数大于10部的国家和地区'
    titleM = '上榜电影各国数量地图'
    htmlName = title + '.html'
    htmlNamet = titlet + '.html'
    htmlNameM = titleM + '.html'
    htmlPath = os.path.join(target_dir, htmlName)
    htmlPatht = os.path.join(target_dir, htmlNamet)
    htmlPathM = os.path.join(target_dir, htmlNameM)
    kt = list(ct.keys())
    vt = list(ct.values())

    pie = Pie(titlet, title_top='bottom', title_pos='center', width=1000, height=500)
    kwargs = dict(
        radius=(0, 70),
        label_text_color=None,
        is_label_show=True,
        legend_orient='vertical',
        legend_pos='left',
        is_more_utils='true',
        center=(55, 50)
    )
    pie.add("电影类型", kt, vt, **kwargs)
    pie.render(htmlPatht)

    bar = Bar(title, title_top='bottom', title_pos='center', width=1000, height=500)
    kwargs = dict(
        label_text_color=None,
        # is_label_show=True,
        legend_orient='vertical',
        legend_pos='left',
        is_more_utils='true',
        mark_point=["max"],
        xaxis_interval=0,
        xaxis_rotate=30,
        yaxis_rotate=30,
        is_datazoom_show=True,
        datazoom_type="inside",
    )
    bar.add("国家/地区", ke, ve, **kwargs)
    # bar.show_config()v
    bar.render(htmlPath)

    c['中国'] = 152
    mc = list(c.keys())
    print(mc)
    nc = list(c.values())
    print(nc)
    map = Map(titleM, title_top='bottom', title_pos='center', width=1300, height=700)
    kwargs = dict(
        maptype="world",
        is_visualmap=True,
        name_map=name_map,
        is_map_symbol_show=False,
        is_roam=True,
        is_more_utils='true',

    )
    map.add("国家/地区", mc, nc, **kwargs)
    # bar.show_config()v
    map.render(htmlPathM)


if __name__ == "__main__":  # 起到一个初始化或者调用函数的作用
    movies_years()
    movies_comment()
    movies_type()
    movies_actor()
    movies_country()
