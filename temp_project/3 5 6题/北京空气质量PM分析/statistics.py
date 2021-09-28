import numpy as np
import pandas as pd


# 数据读取与基本信息展示
def base_info():
    # 文件所在路径  可修改
    file_name = "D:\BaiduNetdiskDownload\data_hand\BeijingPM20100101_20151231.csv"
    df_data = pd.read_csv(file_name, encoding='utf-8')
    # 设置显示信息
    pd.set_option('display.max_columns', None)
    # 基本信息查看，包括数据，数据综述，数据的信息情况
    # print(df_data.head())
    # print(df_data.describe())
    # print(df_data.info())
    return df_data


# 问题1解决
def question_one(pd_data: pd.DataFrame):
    # 仅读取相关列（与PM浓度有关的列6， 7， 8， 9及年份列1）
    use_data = pd_data.iloc[:, [1, 6, 7, 8, 9]]
    # 将列名PM_US Post修改为PM_US_Post，防止出错,两种方法，第一种会有警告 但不影响
    # use_data.rename(columns=lambda x: x.replace(' ', '_'), inplace=True)
    use_data.columns = ['year', 'PM_Dongsi', 'PM_Dongsihuan', 'PM_Nongzhanguan', 'PM_US_Post']
    print(use_data.columns)
    # 查看每列缺失情况
    print("Total data rows: %d" % len(use_data))
    for column in use_data:
        print("Missing number of %s: %d" % (column, len(use_data) - len(use_data[column].dropna())))

    # 求平均值,axis=1为求每行平均值, 警告不影响
    # 计算过程：先计算每条数据各地点的平均值，再计算每年的平均值
    use_data['pm_average'] = use_data.iloc[:, 1:5].mean(axis=1)
    mean_data = use_data.groupby('year')['pm_average'].mean()
    print(mean_data)
    # 文件存取路径可自行修改，默认生成到当前文件夹下
    mean_data.to_csv('question_one.csv')


# 问题2解决
def question_two(pd_data: pd.DataFrame):
    # 取相关列，包括年 月 和PM相关列
    use_data = pd_data.iloc[:, [1, 2, 6, 7, 8, 9]]
    # 求多个PM相关列的平均值作为该条数据的PM浓度
    use_data['pm_average'] = use_data.iloc[:, 2:6].mean(axis=1)
    # 根据年份和月份分组计算，得到每年每个月份的PM浓度情况
    mean_data = use_data.groupby(['year', 'month'])['pm_average'].mean()
    print(mean_data.head())
    # 将结果存入本地文件
    mean_data.to_csv('question_two.csv')


def main():
    df_data = base_info()
    # question_one(df_data)
    # question_two(df_data)


if __name__ == "__main__":
    main()