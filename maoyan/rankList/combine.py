# coding=utf-8
import os
import pandas as pd
import glob


def hebing():
    csv_list = glob.glob('*.csv')
    print(u'共发现%s个CSV文件' % len(csv_list))
    print(u'正在处理............')
    for i in csv_list:
        fr = open(i, 'r', encoding='utf-8').read()
        with open('猫眼电影排行榜.csv', 'a', encoding='utf-8') as f:
            f.write(fr)
    print(u'合并完毕！')


def quchong(file):
    df = pd.read_csv(file, encoding='utf-8')
    datalist = df.drop_duplicates(keep=False)
    datalist.reset_index(drop=True, inplace=True)
    datalist.to_csv(file, encoding='utf-8')
    print('结束')


if __name__ == '__main__':
    hebing()
    quchong("猫眼电影排行榜.csv")
