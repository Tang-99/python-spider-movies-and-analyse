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
from snownlp import SnowNLP

data = pd.read_csv("E:/pythonsoft/spider/douban/Top20.csv", encoding='utf-8')


def movies_type():
    target_dir = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "douban", "results")
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    print("分析结果保存在 ", target_dir, " 文件夹下...")
    title = 'Top30电影类型'
    htmlName = title + '.html'
    htmlPath = os.path.join(target_dir, htmlName)

    types = data['电影类型'].str.split('/')
    l = []
    tl = []
    for i in range(29):
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
    types = data['主演'].str.split('/')
    # print(types)
    l = []
    tl = []
    for i in range(29):
        l.extend(types[i])
    for i in l:
        tl.append(i.strip())
    c = Counter(tl)
    # print(c)
    k = list(c.keys())
    # print(k)
    v = list(c.values())
    # print(v)
    target_dir = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "douban", "results")
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    print("分析结果保存在 ", target_dir, " 文件夹下...")
    title = 'Top30演员出现次数'
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


def movies_comment():
    target_dir = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "douban", "results")
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    print("分析结果保存在 ", target_dir, " 文件夹下...")
    title = 'Top30评分和评论人数'
    htmlName = title + '.html'
    htmlPath = os.path.join(target_dir, htmlName)

    x = data.groupby('电影名称')[['评论人数', '评分']].mean()
    # print(x)
    s = (x - x.mean()) / x.std()
    # print(s)
    p = list(s.index)
    y = list(s['评分'])
    z = list(s['评论人数'])
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
    line.render(htmlPath)


def movies_sen():
    target_dir = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "results")
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    print("分析结果保存在 ", target_dir, " 文件夹下...")
    title = '战狼2评论情感分析'
    htmlName = title + '.html'
    htmlPath = os.path.join(target_dir, htmlName)

    df = pd.read_csv('E:/pythonsoft/spider/douban/comment_data/26363254.csv')

    to_drop = ['用户', '是否看过', '评分', '评论时间', '有用数']
    df.drop(to_drop, axis=1, inplace=True)
    # print(df)
    str = df.to_string(index=False, columns=['评论'], header=False)
    str = [i.strip() for i in str.split('\n')]
    sentimentslist = []
    for i in str:
        s = SnowNLP(i)
        sentimentslist.append(s.sentiments - 0.5)

    line = Line(title, title_top='bottom', title_pos='center', width=1000, height=600)
    kwargs = dict(
        label_text_color=None,
        # is_label_show=True,
        legend_orient='vertical',
        legend_pos='left',
        is_more_utils='true',
        is_datazoom_show=True,
        datazoom_type="inside",
        is_smooth=True,
        area_opacity=0.3,
    )
    # subtitle="接近0.5为积极，接近-0.5为消极
    line.add("情感积极度", [x for x in range(len(sentimentslist))], sentimentslist, **kwargs)
    # bar.show_config()
    line.render(htmlPath)


def movies_mo():
    target_dir = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "results")
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    print("分析结果保存在 ", target_dir, " 文件夹下...")
    title = '哪吒之魔童降世评论情感分析'
    htmlName = title + '.html'
    htmlPath = os.path.join(target_dir, htmlName)

    df = pd.read_csv('E:/pythonsoft/spider/douban/comment_data/26794435.csv')

    to_drop = ['用户', '是否看过', '评分', '评论时间', '有用数']
    df.drop(to_drop, axis=1, inplace=True)
    # print(df)
    str = df.to_string(index=False, columns=['评论'], header=False)
    str = [i.strip() for i in str.split('\n')]
    sentimentslist = []
    for i in str:
        s = SnowNLP(i)
        sentimentslist.append(s.sentiments - 0.5)

    line = Line(title, title_top='bottom', title_pos='center', width=1000, height=600)
    kwargs = dict(
        label_text_color=None,
        # is_label_show=True,
        legend_orient='vertical',
        legend_pos='left',
        is_more_utils='true',
        is_datazoom_show=True,
        datazoom_type="inside",
        is_smooth=True,
        area_opacity=0.3,
    )
    # subtitle="接近0.5为积极，接近-0.5为消极
    line.add("情感积极度", [x for x in range(len(sentimentslist))], sentimentslist, **kwargs)
    # bar.show_config()
    line.render(htmlPath)


def movies_liu():
    target_dir = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "results")
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    print("分析结果保存在 ", target_dir, " 文件夹下...")
    title = '流浪地球评论情感分析'
    htmlName = title + '.html'
    htmlPath = os.path.join(target_dir, htmlName)

    df = pd.read_csv('E:/pythonsoft/spider/douban/comment_data/26266893.csv')

    to_drop = ['用户', '是否看过', '评分', '评论时间', '有用数']
    df.drop(to_drop, axis=1, inplace=True)
    # print(df)
    str = df.to_string(index=False, columns=['评论'], header=False)
    str = [i.strip() for i in str.split('\n')]
    sentimentslist = []
    for i in str:
        s = SnowNLP(i)
        sentimentslist.append(s.sentiments - 0.5)

    line = Line(title, title_top='bottom', title_pos='center', width=1000, height=600)
    kwargs = dict(
        label_text_color=None,
        # is_label_show=True,
        legend_orient='vertical',
        legend_pos='left',
        is_more_utils='true',
        is_datazoom_show=True,
        datazoom_type="inside",
        is_smooth=True,
        area_opacity=0.3,
    )
    # subtitle="接近0.5为积极，接近-0.5为消极
    line.add("情感积极度", [x for x in range(len(sentimentslist))], sentimentslist, **kwargs)
    # bar.show_config()
    line.render(htmlPath)


def movies_fu():
    target_dir = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "results")
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    print("分析结果保存在 ", target_dir, " 文件夹下...")
    title = '复仇者联盟4：终局之战评论情感分析'
    htmlName = title + '.html'
    htmlPath = os.path.join(target_dir, htmlName)

    df = pd.read_csv('E:/pythonsoft/spider/douban/comment_data/26100958.csv')

    to_drop = ['用户', '是否看过', '评分', '评论时间', '有用数']
    df.drop(to_drop, axis=1, inplace=True)
    # print(df)
    str = df.to_string(index=False, columns=['评论'], header=False)
    str = [i.strip() for i in str.split('\n')]
    sentimentslist = []
    for i in str:
        s = SnowNLP(i)
        sentimentslist.append(s.sentiments - 0.5)

    line = Line(title, title_top='bottom', title_pos='center', width=1000, height=600)
    kwargs = dict(
        label_text_color=None,
        # is_label_show=True,
        legend_orient='vertical',
        legend_pos='left',
        is_more_utils='true',
        is_datazoom_show=True,
        datazoom_type="inside",
        is_smooth=True,
        area_opacity=0.3,
    )
    # subtitle="接近0.5为积极，接近-0.5为消极
    line.add("情感积极度", [x for x in range(len(sentimentslist))], sentimentslist, **kwargs)
    # bar.show_config()
    line.render(htmlPath)


def movies_hong():
    target_dir = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "results")
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    print("分析结果保存在 ", target_dir, " 文件夹下...")
    title = '红海行动评论情感分析'
    htmlName = title + '.html'
    htmlPath = os.path.join(target_dir, htmlName)

    df = pd.read_csv('E:/pythonsoft/spider/douban/comment_data/26861685.csv')

    to_drop = ['用户', '是否看过', '评分', '评论时间', '有用数']
    df.drop(to_drop, axis=1, inplace=True)
    # print(df)
    str = df.to_string(index=False, columns=['评论'], header=False)
    str = [i.strip() for i in str.split('\n')]
    sentimentslist = []
    for i in str:
        s = SnowNLP(i)
        sentimentslist.append(s.sentiments - 0.5)

    line = Line(title, title_top='bottom', title_pos='center', width=1000, height=600)
    kwargs = dict(
        label_text_color=None,
        # is_label_show=True,
        legend_orient='vertical',
        legend_pos='left',
        is_more_utils='true',
        is_datazoom_show=True,
        datazoom_type="inside",
        is_smooth=True,
        area_opacity=0.3,
    )
    # subtitle="接近0.5为积极，接近-0.5为消极
    line.add("情感积极度", [x for x in range(len(sentimentslist))], sentimentslist, **kwargs)
    # bar.show_config()
    line.render(htmlPath)


def movies_tang():
    target_dir = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "results")
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    print("分析结果保存在 ", target_dir, " 文件夹下...")
    title = '唐人街探案2评论情感分析'
    htmlName = title + '.html'
    htmlPath = os.path.join(target_dir, htmlName)

    df = pd.read_csv('E:/pythonsoft/spider/douban/comment_data/26698897.csv')

    to_drop = ['用户', '是否看过', '评分', '评论时间', '有用数']
    df.drop(to_drop, axis=1, inplace=True)
    # print(df)
    str = df.to_string(index=False, columns=['评论'], header=False)
    str = [i.strip() for i in str.split('\n')]
    sentimentslist = []
    for i in str:
        s = SnowNLP(i)
        sentimentslist.append(s.sentiments - 0.5)

    line = Line(title, title_top='bottom', title_pos='center', width=1000, height=600)
    kwargs = dict(
        label_text_color=None,
        # is_label_show=True,
        legend_orient='vertical',
        legend_pos='left',
        is_more_utils='true',
        is_datazoom_show=True,
        datazoom_type="inside",
        is_smooth=True,
        area_opacity=0.3,
    )
    # subtitle="接近0.5为积极，接近-0.5为消极
    line.add("情感积极度", [x for x in range(len(sentimentslist))], sentimentslist, **kwargs)
    # bar.show_config()
    line.render(htmlPath)


def movies_mei():
    target_dir = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "results")
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    print("分析结果保存在 ", target_dir, " 文件夹下...")
    title = '美人鱼评论情感分析'
    htmlName = title + '.html'
    htmlPath = os.path.join(target_dir, htmlName)

    df = pd.read_csv('E:/pythonsoft/spider/douban/comment_data/19944106.csv')

    to_drop = ['用户', '是否看过', '评分', '评论时间', '有用数']
    df.drop(to_drop, axis=1, inplace=True)
    # print(df)
    str = df.to_string(index=False, columns=['评论'], header=False)
    str = [i.strip() for i in str.split('\n')]
    sentimentslist = []
    for i in str:
        s = SnowNLP(i)
        sentimentslist.append(s.sentiments - 0.5)

    line = Line(title, title_top='bottom', title_pos='center', width=1000, height=600)
    kwargs = dict(
        label_text_color=None,
        # is_label_show=True,
        legend_orient='vertical',
        legend_pos='left',
        is_more_utils='true',
        is_datazoom_show=True,
        datazoom_type="inside",
        is_smooth=True,
        area_opacity=0.3,
    )
    # subtitle="接近0.5为积极，接近-0.5为消极
    line.add("情感积极度", [x for x in range(len(sentimentslist))], sentimentslist, **kwargs)
    # bar.show_config()
    line.render(htmlPath)


def movies_wo():
    target_dir = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "results")
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    print("分析结果保存在 ", target_dir, " 文件夹下...")
    title = '我和我的祖国评论情感分析'
    htmlName = title + '.html'
    htmlPath = os.path.join(target_dir, htmlName)

    df = pd.read_csv('E:/pythonsoft/spider/douban/comment_data/32659890.csv')

    to_drop = ['用户', '是否看过', '评分', '评论时间', '有用数']
    df.drop(to_drop, axis=1, inplace=True)
    # print(df)
    str = df.to_string(index=False, columns=['评论'], header=False)
    str = [i.strip() for i in str.split('\n')]
    sentimentslist = []
    for i in str:
        s = SnowNLP(i)
        sentimentslist.append(s.sentiments - 0.5)

    line = Line(title, title_top='bottom', title_pos='center', width=1000, height=600)
    kwargs = dict(
        label_text_color=None,
        # is_label_show=True,
        legend_orient='vertical',
        legend_pos='left',
        is_more_utils='true',
        is_datazoom_show=True,
        datazoom_type="inside",
        is_smooth=True,
        area_opacity=0.3,
    )
    # subtitle="接近0.5为积极，接近-0.5为消极
    line.add("情感积极度", [x for x in range(len(sentimentslist))], sentimentslist, **kwargs)
    # bar.show_config()
    line.render(htmlPath)


def movies_ba():
    target_dir = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "results")
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    print("分析结果保存在 ", target_dir, " 文件夹下...")
    title = '八佰评论情感分析'
    htmlName = title + '.html'
    htmlPath = os.path.join(target_dir, htmlName)

    df = pd.read_csv('E:/pythonsoft/spider/douban/comment_data/26754233.csv')

    to_drop = ['用户', '是否看过', '评分', '评论时间', '有用数']
    df.drop(to_drop, axis=1, inplace=True)
    # print(df)
    str = df.to_string(index=False, columns=['评论'], header=False)
    str = [i.strip() for i in str.split('\n')]
    sentimentslist = []
    for i in str:
        s = SnowNLP(i)
        sentimentslist.append(s.sentiments - 0.5)

    line = Line(title, title_top='bottom', title_pos='center', width=1000, height=600)
    kwargs = dict(
        label_text_color=None,
        # is_label_show=True,
        legend_orient='vertical',
        legend_pos='left',
        is_more_utils='true',
        is_datazoom_show=True,
        datazoom_type="inside",
        is_smooth=True,
        area_opacity=0.3,
    )
    # subtitle="接近0.5为积极，接近-0.5为消极
    line.add("情感积极度", [x for x in range(len(sentimentslist))], sentimentslist, **kwargs)
    # bar.show_config()
    line.render(htmlPath)


def movies_wobu():
    target_dir = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "results")
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    print("分析结果保存在 ", target_dir, " 文件夹下...")
    title = '我不是药神评论情感分析'
    htmlName = title + '.html'
    htmlPath = os.path.join(target_dir, htmlName)

    df = pd.read_csv('E:/pythonsoft/spider/douban/comment_data/26752088.csv')

    to_drop = ['用户', '是否看过', '评分', '评论时间', '有用数']
    df.drop(to_drop, axis=1, inplace=True)
    # print(df)
    str = df.to_string(index=False, columns=['评论'], header=False)
    str = [i.strip() for i in str.split('\n')]
    sentimentslist = []
    for i in str:
        s = SnowNLP(i)
        sentimentslist.append(s.sentiments - 0.5)

    line = Line(title, title_top='bottom', title_pos='center', width=1000, height=600)
    kwargs = dict(
        label_text_color=None,
        # is_label_show=True,
        legend_orient='vertical',
        legend_pos='left',
        is_more_utils='true',
        is_datazoom_show=True,
        datazoom_type="inside",
        is_smooth=True,
        area_opacity=0.3,
    )
    # subtitle="接近0.5为积极，接近-0.5为消极
    line.add("情感积极度", [x for x in range(len(sentimentslist))], sentimentslist, **kwargs)
    # bar.show_config()
    line.render(htmlPath)


def movies_zhong():
    target_dir = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "results")
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    print("分析结果保存在 ", target_dir, " 文件夹下...")
    title = '中国机长评论情感分析'
    htmlName = title + '.html'
    htmlPath = os.path.join(target_dir, htmlName)

    df = pd.read_csv('E:/pythonsoft/spider/douban/comment_data/30295905.csv')

    to_drop = ['用户', '是否看过', '评分', '评论时间', '有用数']
    df.drop(to_drop, axis=1, inplace=True)
    # print(df)
    str = df.to_string(index=False, columns=['评论'], header=False)
    str = [i.strip() for i in str.split('\n')]
    sentimentslist = []
    for i in str:
        s = SnowNLP(i)
        sentimentslist.append(s.sentiments - 0.5)

    line = Line(title, title_top='bottom', title_pos='center', width=1000, height=600)
    kwargs = dict(
        label_text_color=None,
        # is_label_show=True,
        legend_orient='vertical',
        legend_pos='left',
        is_more_utils='true',
        is_datazoom_show=True,
        datazoom_type="inside",
        is_smooth=True,
        area_opacity=0.3,
    )
    # subtitle="接近0.5为积极，接近-0.5为消极
    line.add("情感积极度", [x for x in range(len(sentimentslist))], sentimentslist, **kwargs)
    # bar.show_config()
    line.render(htmlPath)


def movies_wode():
    target_dir = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "results")
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    print("分析结果保存在 ", target_dir, " 文件夹下...")
    title = '我和我的家乡评论情感分析'
    htmlName = title + '.html'
    htmlPath = os.path.join(target_dir, htmlName)

    df = pd.read_csv('E:/pythonsoft/spider/douban/comment_data/35051512.csv')

    to_drop = ['用户', '是否看过', '评分', '评论时间', '有用数']
    df.drop(to_drop, axis=1, inplace=True)
    # print(df)
    str = df.to_string(index=False, columns=['评论'], header=False)
    str = [i.strip() for i in str.split('\n')]
    sentimentslist = []
    for i in str:
        s = SnowNLP(i)
        sentimentslist.append(s.sentiments - 0.5)

    line = Line(title, title_top='bottom', title_pos='center', width=1000, height=600)
    kwargs = dict(
        label_text_color=None,
        # is_label_show=True,
        legend_orient='vertical',
        legend_pos='left',
        is_more_utils='true',
        is_datazoom_show=True,
        datazoom_type="inside",
        is_smooth=True,
        area_opacity=0.3,
    )
    # subtitle="接近0.5为积极，接近-0.5为消极
    line.add("情感积极度", [x for x in range(len(sentimentslist))], sentimentslist, **kwargs)
    # bar.show_config()
    line.render(htmlPath)


def movies_su8():
    target_dir = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "results")
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    print("分析结果保存在 ", target_dir, " 文件夹下...")
    title = '速度与激情8评论情感分析'
    htmlName = title + '.html'
    htmlPath = os.path.join(target_dir, htmlName)

    df = pd.read_csv('E:/pythonsoft/spider/douban/comment_data/26260853.csv')

    to_drop = ['用户', '是否看过', '评分', '评论时间', '有用数']
    df.drop(to_drop, axis=1, inplace=True)
    # print(df)
    str = df.to_string(index=False, columns=['评论'], header=False)
    str = [i.strip() for i in str.split('\n')]
    sentimentslist = []
    for i in str:
        s = SnowNLP(i)
        sentimentslist.append(s.sentiments - 0.5)

    line = Line(title, title_top='bottom', title_pos='center', width=1000, height=600)
    kwargs = dict(
        label_text_color=None,
        # is_label_show=True,
        legend_orient='vertical',
        legend_pos='left',
        is_more_utils='true',
        is_datazoom_show=True,
        datazoom_type="inside",
        is_smooth=True,
        area_opacity=0.3,
    )
    # subtitle="接近0.5为积极，接近-0.5为消极
    line.add("情感积极度", [x for x in range(len(sentimentslist))], sentimentslist, **kwargs)
    # bar.show_config()
    line.render(htmlPath)


def movies_zhuo():
    target_dir = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "results")
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    print("分析结果保存在 ", target_dir, " 文件夹下...")
    title = '捉妖记2评论情感分析'
    htmlName = title + '.html'
    htmlPath = os.path.join(target_dir, htmlName)

    df = pd.read_csv('E:/pythonsoft/spider/douban/comment_data/26575103.csv')

    to_drop = ['用户', '是否看过', '评分', '评论时间', '有用数']
    df.drop(to_drop, axis=1, inplace=True)
    # print(df)
    str = df.to_string(index=False, columns=['评论'], header=False)
    str = [i.strip() for i in str.split('\n')]
    sentimentslist = []
    for i in str:
        s = SnowNLP(i)
        sentimentslist.append(s.sentiments - 0.5)

    line = Line(title, title_top='bottom', title_pos='center', width=1000, height=600)
    kwargs = dict(
        label_text_color=None,
        # is_label_show=True,
        legend_orient='vertical',
        legend_pos='left',
        is_more_utils='true',
        is_datazoom_show=True,
        datazoom_type="inside",
        is_smooth=True,
        area_opacity=0.3,
    )
    # subtitle="接近0.5为积极，接近-0.5为消极
    line.add("情感积极度", [x for x in range(len(sentimentslist))], sentimentslist, **kwargs)
    # bar.show_config()
    line.render(htmlPath)


def movies_xi():
    target_dir = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "results")
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    print("分析结果保存在 ", target_dir, " 文件夹下...")
    title = '西虹市首富评论情感分析'
    htmlName = title + '.html'
    htmlPath = os.path.join(target_dir, htmlName)

    df = pd.read_csv('E:/pythonsoft/spider/douban/comment_data/27605698.csv')

    to_drop = ['用户', '是否看过', '评分', '评论时间', '有用数']
    df.drop(to_drop, axis=1, inplace=True)
    # print(df)
    str = df.to_string(index=False, columns=['评论'], header=False)
    str = [i.strip() for i in str.split('\n')]
    sentimentslist = []
    for i in str:
        s = SnowNLP(i)
        sentimentslist.append(s.sentiments - 0.5)

    line = Line(title, title_top='bottom', title_pos='center', width=1000, height=600)
    kwargs = dict(
        label_text_color=None,
        # is_label_show=True,
        legend_orient='vertical',
        legend_pos='left',
        is_more_utils='true',
        is_datazoom_show=True,
        datazoom_type="inside",
        is_smooth=True,
        area_opacity=0.3,
    )
    # subtitle="接近0.5为积极，接近-0.5为消极
    line.add("情感积极度", [x for x in range(len(sentimentslist))], sentimentslist, **kwargs)
    # bar.show_config()
    line.render(htmlPath)


def movies_su7():
    target_dir = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "results")
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    print("分析结果保存在 ", target_dir, " 文件夹下...")
    title = '速度与激情7评论情感分析'
    htmlName = title + '.html'
    htmlPath = os.path.join(target_dir, htmlName)

    df = pd.read_csv('E:/pythonsoft/spider/douban/comment_data/23761370.csv')

    to_drop = ['用户', '是否看过', '评分', '评论时间', '有用数']
    df.drop(to_drop, axis=1, inplace=True)
    # print(df)
    str = df.to_string(index=False, columns=['评论'], header=False)
    str = [i.strip() for i in str.split('\n')]
    sentimentslist = []
    for i in str:
        s = SnowNLP(i)
        sentimentslist.append(s.sentiments - 0.5)

    line = Line(title, title_top='bottom', title_pos='center', width=1000, height=600)
    kwargs = dict(
        label_text_color=None,
        # is_label_show=True,
        legend_orient='vertical',
        legend_pos='left',
        is_more_utils='true',
        is_datazoom_show=True,
        datazoom_type="inside",
        is_smooth=True,
        area_opacity=0.3,
    )
    # subtitle="接近0.5为积极，接近-0.5为消极
    line.add("情感积极度", [x for x in range(len(sentimentslist))], sentimentslist, **kwargs)
    # bar.show_config()
    line.render(htmlPath)


def movies_fu3():
    target_dir = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "results")
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    print("分析结果保存在 ", target_dir, " 文件夹下...")
    title = '复仇者联盟3：无限战争评论情感分析'
    htmlName = title + '.html'
    htmlPath = os.path.join(target_dir, htmlName)

    df = pd.read_csv('E:/pythonsoft/spider/douban/comment_data/24773958.csv')

    to_drop = ['用户', '是否看过', '评分', '评论时间', '有用数']
    df.drop(to_drop, axis=1, inplace=True)
    # print(df)
    str = df.to_string(index=False, columns=['评论'], header=False)
    str = [i.strip() for i in str.split('\n')]
    sentimentslist = []
    for i in str:
        s = SnowNLP(i)
        sentimentslist.append(s.sentiments - 0.5)

    line = Line(title, title_top='bottom', title_pos='center', width=1000, height=600)
    kwargs = dict(
        label_text_color=None,
        # is_label_show=True,
        legend_orient='vertical',
        legend_pos='left',
        is_more_utils='true',
        is_datazoom_show=True,
        datazoom_type="inside",
        is_smooth=True,
        area_opacity=0.3,
    )
    # subtitle="接近0.5为积极，接近-0.5为消极
    line.add("情感积极度", [x for x in range(len(sentimentslist))], sentimentslist, **kwargs)
    # bar.show_config()
    line.render(htmlPath)


def movies_xiu():
    target_dir = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "results")
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    print("分析结果保存在 ", target_dir, " 文件夹下...")
    title = '羞羞的铁拳评论情感分析'
    htmlName = title + '.html'
    htmlPath = os.path.join(target_dir, htmlName)

    df = pd.read_csv('E:/pythonsoft/spider/douban/comment_data/27038183.csv')

    to_drop = ['用户', '是否看过', '评分', '评论时间', '有用数']
    df.drop(to_drop, axis=1, inplace=True)
    # print(df)
    str = df.to_string(index=False, columns=['评论'], header=False)
    str = [i.strip() for i in str.split('\n')]
    sentimentslist = []
    for i in str:
        s = SnowNLP(i)
        sentimentslist.append(s.sentiments - 0.5)

    line = Line(title, title_top='bottom', title_pos='center', width=1000, height=600)
    kwargs = dict(
        label_text_color=None,
        # is_label_show=True,
        legend_orient='vertical',
        legend_pos='left',
        is_more_utils='true',
        is_datazoom_show=True,
        datazoom_type="inside",
        is_smooth=True,
        area_opacity=0.3,
    )
    # subtitle="接近0.5为积极，接近-0.5为消极
    line.add("情感积极度", [x for x in range(len(sentimentslist))], sentimentslist, **kwargs)
    # bar.show_config()
    line.render(htmlPath)


def movies_feng():
    target_dir = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "results")
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    print("分析结果保存在 ", target_dir, " 文件夹下...")
    title = '疯狂的外星人评论情感分析'
    htmlName = title + '.html'
    htmlPath = os.path.join(target_dir, htmlName)

    df = pd.read_csv('E:/pythonsoft/spider/douban/comment_data/25986662.csv')

    to_drop = ['用户', '是否看过', '评分', '评论时间', '有用数']
    df.drop(to_drop, axis=1, inplace=True)
    # print(df)
    str = df.to_string(index=False, columns=['评论'], header=False)
    str = [i.strip() for i in str.split('\n')]
    sentimentslist = []
    for i in str:
        s = SnowNLP(i)
        sentimentslist.append(s.sentiments - 0.5)

    line = Line(title, title_top='bottom', title_pos='center', width=1000, height=600)
    kwargs = dict(
        label_text_color=None,
        # is_label_show=True,
        legend_orient='vertical',
        legend_pos='left',
        is_more_utils='true',
        is_datazoom_show=True,
        datazoom_type="inside",
        is_smooth=True,
        area_opacity=0.3,
    )
    # subtitle="接近0.5为积极，接近-0.5为消极
    line.add("情感积极度", [x for x in range(len(sentimentslist))], sentimentslist, **kwargs)
    # bar.show_config()
    line.render(htmlPath)


def movies_hai():
    target_dir = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "results")
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    print("分析结果保存在 ", target_dir, " 文件夹下...")
    title = '海王评论情感分析'
    htmlName = title + '.html'
    htmlPath = os.path.join(target_dir, htmlName)

    df = pd.read_csv('E:/pythonsoft/spider/douban/comment_data/3878007.csv')

    to_drop = ['用户', '是否看过', '评分', '评论时间', '有用数']
    df.drop(to_drop, axis=1, inplace=True)
    # print(df)
    str = df.to_string(index=False, columns=['评论'], header=False)
    str = [i.strip() for i in str.split('\n')]
    sentimentslist = []
    for i in str:
        s = SnowNLP(i)
        sentimentslist.append(s.sentiments - 0.5)

    line = Line(title, title_top='bottom', title_pos='center', width=1000, height=600)
    kwargs = dict(
        label_text_color=None,
        # is_label_show=True,
        legend_orient='vertical',
        legend_pos='left',
        is_more_utils='true',
        is_datazoom_show=True,
        datazoom_type="inside",
        is_smooth=True,
        area_opacity=0.3,
    )
    # subtitle="接近0.5为积极，接近-0.5为消极
    line.add("情感积极度", [x for x in range(len(sentimentslist))], sentimentslist, **kwargs)
    # bar.show_config()
    line.render(htmlPath)

def movies_bian4():
    target_dir = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "results")
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    print("分析结果保存在 ", target_dir, " 文件夹下...")
    title = '变形金刚4：绝迹重生评论情感分析'
    htmlName = title + '.html'
    htmlPath = os.path.join(target_dir, htmlName)

    df = pd.read_csv('E:/pythonsoft/spider/douban/comment_data/7054604.csv')

    to_drop = ['用户', '是否看过', '评分', '评论时间', '有用数']
    df.drop(to_drop, axis=1, inplace=True)
    # print(df)
    str = df.to_string(index=False, columns=['评论'], header=False)
    str = [i.strip() for i in str.split('\n')]
    sentimentslist = []
    for i in str:
        s = SnowNLP(i)
        sentimentslist.append(s.sentiments - 0.5)

    line = Line(title, title_top='bottom', title_pos='center', width=1000, height=600)
    kwargs = dict(
        label_text_color=None,
        # is_label_show=True,
        legend_orient='vertical',
        legend_pos='left',
        is_more_utils='true',
        is_datazoom_show=True,
        datazoom_type="inside",
        is_smooth=True,
        area_opacity=0.3,
    )
    # subtitle="接近0.5为积极，接近-0.5为消极
    line.add("情感积极度", [x for x in range(len(sentimentslist))], sentimentslist, **kwargs)
    # bar.show_config()
    line.render(htmlPath)


def movies_qian():
    target_dir = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "results")
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    print("分析结果保存在 ", target_dir, " 文件夹下...")
    title = '前任3：再见前任评论情感分析'
    htmlName = title + '.html'
    htmlPath = os.path.join(target_dir, htmlName)

    df = pd.read_csv('E:/pythonsoft/spider/douban/comment_data/26662193.csv')

    to_drop = ['用户', '是否看过', '评分', '评论时间', '有用数']
    df.drop(to_drop, axis=1, inplace=True)
    # print(df)
    str = df.to_string(index=False, columns=['评论'], header=False)
    str = [i.strip() for i in str.split('\n')]
    sentimentslist = []
    for i in str:
        s = SnowNLP(i)
        sentimentslist.append(s.sentiments - 0.5)

    line = Line(title, title_top='bottom', title_pos='center', width=1000, height=600)
    kwargs = dict(
        label_text_color=None,
        # is_label_show=True,
        legend_orient='vertical',
        legend_pos='left',
        is_more_utils='true',
        is_datazoom_show=True,
        datazoom_type="inside",
        is_smooth=True,
        area_opacity=0.3,
    )
    # subtitle="接近0.5为积极，接近-0.5为消极
    line.add("情感积极度", [x for x in range(len(sentimentslist))], sentimentslist, **kwargs)
    # bar.show_config()
    line.render(htmlPath)


def movies_du():
    target_dir = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "results")
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    print("分析结果保存在 ", target_dir, " 文件夹下...")
    title = '毒液：致命守护者评论情感分析'
    htmlName = title + '.html'
    htmlPath = os.path.join(target_dir, htmlName)

    df = pd.read_csv('E:/pythonsoft/spider/douban/comment_data/3168101.csv')

    to_drop = ['用户', '是否看过', '评分', '评论时间', '有用数']
    df.drop(to_drop, axis=1, inplace=True)
    # print(df)
    str = df.to_string(index=False, columns=['评论'], header=False)
    str = [i.strip() for i in str.split('\n')]
    sentimentslist = []
    for i in str:
        s = SnowNLP(i)
        sentimentslist.append(s.sentiments - 0.5)

    line = Line(title, title_top='bottom', title_pos='center', width=1000, height=600)
    kwargs = dict(
        label_text_color=None,
        # is_label_show=True,
        legend_orient='vertical',
        legend_pos='left',
        is_more_utils='true',
        is_datazoom_show=True,
        datazoom_type="inside",
        is_smooth=True,
        area_opacity=0.3,
    )
    # subtitle="接近0.5为积极，接近-0.5为消极
    line.add("情感积极度", [x for x in range(len(sentimentslist))], sentimentslist, **kwargs)
    # bar.show_config()
    line.render(htmlPath)

def movies_gong():
    target_dir = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "results")
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    print("分析结果保存在 ", target_dir, " 文件夹下...")
    title = '功夫瑜伽评论情感分析'
    htmlName = title + '.html'
    htmlPath = os.path.join(target_dir, htmlName)

    df = pd.read_csv('E:/pythonsoft/spider/douban/comment_data/26182910.csv')

    to_drop = ['用户', '是否看过', '评分', '评论时间', '有用数']
    df.drop(to_drop, axis=1, inplace=True)
    # print(df)
    str = df.to_string(index=False, columns=['评论'], header=False)
    str = [i.strip() for i in str.split('\n')]
    sentimentslist = []
    for i in str:
        s = SnowNLP(i)
        sentimentslist.append(s.sentiments - 0.5)

    line = Line(title, title_top='bottom', title_pos='center', width=1000, height=600)
    kwargs = dict(
        label_text_color=None,
        # is_label_show=True,
        legend_orient='vertical',
        legend_pos='left',
        is_more_utils='true',
        is_datazoom_show=True,
        datazoom_type="inside",
        is_smooth=True,
        area_opacity=0.3,
    )
    # subtitle="接近0.5为积极，接近-0.5为消极
    line.add("情感积极度", [x for x in range(len(sentimentslist))], sentimentslist, **kwargs)
    # bar.show_config()
    line.render(htmlPath)


def movies_feichi():
    target_dir = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "results")
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    print("分析结果保存在 ", target_dir, " 文件夹下...")
    title = '飞驰人生评论情感分析'
    htmlName = title + '.html'
    htmlPath = os.path.join(target_dir, htmlName)

    df = pd.read_csv('E:/pythonsoft/spider/douban/comment_data/30163509.csv')

    to_drop = ['用户', '是否看过', '评分', '评论时间', '有用数']
    df.drop(to_drop, axis=1, inplace=True)
    # print(df)
    str = df.to_string(index=False, columns=['评论'], header=False)
    str = [i.strip() for i in str.split('\n')]
    sentimentslist = []
    for i in str:
        s = SnowNLP(i)
        sentimentslist.append(s.sentiments - 0.5)

    line = Line(title, title_top='bottom', title_pos='center', width=1000, height=600)
    kwargs = dict(
        label_text_color=None,
        # is_label_show=True,
        legend_orient='vertical',
        legend_pos='left',
        is_more_utils='true',
        is_datazoom_show=True,
        datazoom_type="inside",
        is_smooth=True,
        area_opacity=0.3,
    )
    # subtitle="接近0.5为积极，接近-0.5为消极
    line.add("情感积极度", [x for x in range(len(sentimentslist))], sentimentslist, **kwargs)
    # bar.show_config()
    line.render(htmlPath)

def movies_liehuo():
    target_dir = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "results")
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    print("分析结果保存在 ", target_dir, " 文件夹下...")
    title = '烈火英雄评论情感分析'
    htmlName = title + '.html'
    htmlPath = os.path.join(target_dir, htmlName)

    df = pd.read_csv('E:/pythonsoft/spider/douban/comment_data/30221757.csv')

    to_drop = ['用户', '是否看过', '评分', '评论时间', '有用数']
    df.drop(to_drop, axis=1, inplace=True)
    # print(df)
    str = df.to_string(index=False, columns=['评论'], header=False)
    str = [i.strip() for i in str.split('\n')]
    sentimentslist = []
    for i in str:
        s = SnowNLP(i)
        sentimentslist.append(s.sentiments - 0.5)

    line = Line(title, title_top='bottom', title_pos='center', width=1000, height=600)
    kwargs = dict(
        label_text_color=None,
        # is_label_show=True,
        legend_orient='vertical',
        legend_pos='left',
        is_more_utils='true',
        is_datazoom_show=True,
        datazoom_type="inside",
        is_smooth=True,
        area_opacity=0.3,
    )
    # subtitle="接近0.5为积极，接近-0.5为消极
    line.add("情感积极度", [x for x in range(len(sentimentslist))], sentimentslist, **kwargs)
    # bar.show_config()
    line.render(htmlPath)

def movies_zhuluo():
    target_dir = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "results")
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    print("分析结果保存在 ", target_dir, " 文件夹下...")
    title = '侏罗纪世界2评论情感分析'
    htmlName = title + '.html'
    htmlPath = os.path.join(target_dir, htmlName)

    df = pd.read_csv('E:/pythonsoft/spider/douban/comment_data/26416062.csv')

    to_drop = ['用户', '是否看过', '评分', '评论时间', '有用数']
    df.drop(to_drop, axis=1, inplace=True)
    # print(df)
    str = df.to_string(index=False, columns=['评论'], header=False)
    str = [i.strip() for i in str.split('\n')]
    sentimentslist = []
    for i in str:
        s = SnowNLP(i)
        sentimentslist.append(s.sentiments - 0.5)

    line = Line(title, title_top='bottom', title_pos='center', width=1000, height=600)
    kwargs = dict(
        label_text_color=None,
        # is_label_show=True,
        legend_orient='vertical',
        legend_pos='left',
        is_more_utils='true',
        is_datazoom_show=True,
        datazoom_type="inside",
        is_smooth=True,
        area_opacity=0.3,
    )
    # subtitle="接近0.5为积极，接近-0.5为消极
    line.add("情感积极度", [x for x in range(len(sentimentslist))], sentimentslist, **kwargs)
    # bar.show_config()
    line.render(htmlPath)

def movies_xulong():
    target_dir = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "results")
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    print("分析结果保存在 ", target_dir, " 文件夹下...")
    title = '寻龙诀评论情感分析'
    htmlName = title + '.html'
    htmlPath = os.path.join(target_dir, htmlName)

    df = pd.read_csv('E:/pythonsoft/spider/douban/comment_data/3077412.csv')

    to_drop = ['用户', '是否看过', '评分', '评论时间', '有用数']
    df.drop(to_drop, axis=1, inplace=True)
    # print(df)
    str = df.to_string(index=False, columns=['评论'], header=False)
    str = [i.strip() for i in str.split('\n')]
    sentimentslist = []
    for i in str:
        s = SnowNLP(i)
        sentimentslist.append(s.sentiments - 0.5)

    line = Line(title, title_top='bottom', title_pos='center', width=1000, height=600)
    kwargs = dict(
        label_text_color=None,
        # is_label_show=True,
        legend_orient='vertical',
        legend_pos='left',
        is_more_utils='true',
        is_datazoom_show=True,
        datazoom_type="inside",
        is_smooth=True,
        area_opacity=0.3,
    )
    # subtitle="接近0.5为积极，接近-0.5为消极
    line.add("情感积极度", [x for x in range(len(sentimentslist))], sentimentslist, **kwargs)
    # bar.show_config()
    line.render(htmlPath)


def movies_xiyou():
    target_dir = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "results")
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    print("分析结果保存在 ", target_dir, " 文件夹下...")
    title = '西游伏妖篇评论情感分析'
    htmlName = title + '.html'
    htmlPath = os.path.join(target_dir, htmlName)

    df = pd.read_csv('E:/pythonsoft/spider/douban/comment_data/25801066.csv')

    to_drop = ['用户', '是否看过', '评分', '评论时间', '有用数']
    df.drop(to_drop, axis=1, inplace=True)
    # print(df)
    str = df.to_string(index=False, columns=['评论'], header=False)
    str = [i.strip() for i in str.split('\n')]
    sentimentslist = []
    for i in str:
        s = SnowNLP(i)
        sentimentslist.append(s.sentiments - 0.5)

    line = Line(title, title_top='bottom', title_pos='center', width=1000, height=600)
    kwargs = dict(
        label_text_color=None,
        # is_label_show=True,
        legend_orient='vertical',
        legend_pos='left',
        is_more_utils='true',
        is_datazoom_show=True,
        datazoom_type="inside",
        is_smooth=True,
        area_opacity=0.3,
    )
    # subtitle="接近0.5为积极，接近-0.5为消极
    line.add("情感积极度", [x for x in range(len(sentimentslist))], sentimentslist, **kwargs)
    # bar.show_config()
    line.render(htmlPath)

def movies_gangjiong():
    target_dir = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "results")
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    print("分析结果保存在 ", target_dir, " 文件夹下...")
    title = '港囧评论情感分析'
    htmlName = title + '.html'
    htmlPath = os.path.join(target_dir, htmlName)

    df = pd.read_csv('E:/pythonsoft/spider/douban/comment_data/25710912.csv')

    to_drop = ['用户', '是否看过', '评分', '评论时间', '有用数']
    df.drop(to_drop, axis=1, inplace=True)
    # print(df)
    str = df.to_string(index=False, columns=['评论'], header=False)
    str = [i.strip() for i in str.split('\n')]
    sentimentslist = []
    for i in str:
        s = SnowNLP(i)
        sentimentslist.append(s.sentiments - 0.5)

    line = Line(title, title_top='bottom', title_pos='center', width=1000, height=600)
    kwargs = dict(
        label_text_color=None,
        # is_label_show=True,
        legend_orient='vertical',
        legend_pos='left',
        is_more_utils='true',
        is_datazoom_show=True,
        datazoom_type="inside",
        is_smooth=True,
        area_opacity=0.3,
    )
    # subtitle="接近0.5为积极，接近-0.5为消极
    line.add("情感积极度", [x for x in range(len(sentimentslist))], sentimentslist, **kwargs)
    # bar.show_config()
    line.render(htmlPath)

if __name__ == "__main__":  # 起到一个初始化或者调用函数的作用
    # movies_type()
    # movies_actor()
    # movies_comment()
    # movies_sen()
    # movies_fu()
    # movies_hong()
    # movies_liu()
    # movies_mo()
    # movies_mei()
    # movies_tang()
    # movies_wo()
    # movies_wode()
    # movies_ba()
    # movies_zhong()
    # movies_su7()
    # movies_su8()
    # movies_xi()
    # movies_fu3()
    # movies_wobu()
    # movies_zhuo()
    # movies_hai()
    # movies_xiu()
    # movies_feng()
    # movies_bian4()
    # movies_qian()
    # movies_du()
    # movies_gong()
    # movies_feichi()
    # movies_liehuo()
    # movies_zhuluo()
    # movies_xulong()
    # movies_xiyou()
    movies_gangjiong()
