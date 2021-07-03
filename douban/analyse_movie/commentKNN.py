# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np


def createDataSet():
    """创建数据集"""
    # 每组数据包含的1，2，3，4，5星比例；
    # 很差 较差 还行 推荐 力荐
    # df = pd.read_csv('options.csv', usecols=['5星', '4星', '3星', '2星', '1星'])
    # ar = df.values.tolist()
    # print(ar)
    # print(df)
    group = np.array([[5.0, 19.1, 45.7, 23.8, 6.4],
                      [10.6, 41.8, 37.1, 8.4, 2.2],
                      [74.7, 21.9, 2.9, 0.3, 0.2],
                      [28.0, 48.2, 19.7, 3.0, 1.1],
                      [10.5, 27.3, 49.2, 11.3, 1.6],
                      [5.2, 14.0, 45.5, 26.8, 8.4],
                      [53.9, 35.7, 9.6, 0.7, 0.1],
                      [35.0, 50.0, 13.7, 1.1, 0.2],
                      [9.8, 42.3, 40.3, 6.4, 1.2],
                      [8.5, 16.1, 27.2, 17.2, 31.0],
                      [0.9, 1.8, 12.3, 31.6, 53.5],
                      [4.0, 9.7, 35.3, 35.9, 15.3],
                      [48.4, 37.4, 12.9, 1.1, 0.2],
                      [47.2, 41.5, 10.5, 0.6, 0.1],
                      [54.7, 38.2, 6.6, 0.4, 0.1],
                      [42.3, 39.2, 16.4, 1.6, 0.4],
                      [29.3, 48.1, 19.8, 2.4, 0.5],
                      [2.6, 8.2, 36.6, 37.4, 15.1],
                      [1.3, 3.8, 27.1, 38.4, 29.3],
                      [3.9, 16.1, 51.3, 24.3, 4.4],
                      [5.7, 7.6, 28.2, 27.5, 31.1],
                      [6.5, 6.0, 23.6, 30.2, 33.7],
                      [10.8, 31.8, 44.1, 11.1, 2.2],
                      [25.0, 46.4, 25.2, 2.9, 0.5],
                      [20.0, 42.4, 30.9, 5.3, 1.4],
                      [8.1, 32.8, 45.0, 11.0, 3.1],
                      [3.6, 8.9, 35.3, 34.4, 17.7],
                      [47.6, 42.0, 9.9, 0.4, 0.1],

                      ])
    # group1 = np.array(ar)
    # print(ar)
    # 每组数据对应的标签类型；
    labels = ['还行', '推荐', '力荐', '推荐', '还行', '还行', '力荐',
              '推荐', '推荐', '很差', '很差', '较差', '力荐', '力荐',
              '力荐', '力荐', '推荐', '较差', '较差', '还行', '较差',
              '较差', '还行', '推荐', '推荐', '还行', '还行', '力荐',
              ]
    return group, labels


def classify(inx, dataSet, labels, k):
    """
    KNN分类算法实现
    :param inx:要预测电影的数据, e.g.[5.0, 19.1, 45.7, 23.8, 6.4]
    :param dataSet:传入已知数据集，e.g. group 相当于x
    :param labels:传入标签，e.g. labels相当于y
    :param k:KNN里面的k，也就是我们要选择几个近邻
    :return:电影类新的排序
    """
    dataSetSize = dataSet.shape[0]  # (6,2) -- 6行2列 ===> 6 获取行数
    # tile会重复inx， 把它重复成(dataSetSize, 1)型的矩阵
    # (x1 - y1), (x2 - y2)
    diffMat = np.tile(inx, (dataSetSize, 1)) - dataSet
    # 平方
    sqDiffMat = diffMat ** 2
    # 相加, axis=1行相加
    sqDistance = sqDiffMat.sum(axis=1)
    # 开根号
    distance = sqDistance ** 0.5
    # 排序索引： 输出的是序列号index， 而不是值
    sortedDistIndicies = distance.argsort()
    # print(sortedDistIndicies)

    classCount = {}
    for i in range(k):
        # 获取排前k个的标签名；
        voteLabel = labels[sortedDistIndicies[i]]
        classCount[voteLabel] = classCount.get(voteLabel, 0) + 1

    sortedClassCount = sorted(classCount.items(),
                              key=lambda d: float(d[1]),
                              reverse=True)
    return sortedClassCount[0][0]


def resultType():
    # 读取数据集
    df = pd.read_csv('../options.csv', usecols=['5星', '4星', '3星', '2星', '1星'])
    af = pd.read_csv('../options.csv')
    ar = df.values.tolist()
    list1 = []
    # print(ar)
    # 对数据集进行算法分析
    for item in ar:
        # print(item)
        result = classify(item, group, label, 6)
        # print(result)
        list1.append(result)

    # print(list1)
    af['推荐度'] = list1
    print(af)
    csv_file = af.to_csv('Top30.csv', encoding='utf-8', index=False)



if __name__ == '__main__':
    group, label = createDataSet()
    resultType()

