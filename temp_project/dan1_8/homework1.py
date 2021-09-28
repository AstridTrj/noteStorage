import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 为了显示中文，需要更换字体
plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']


# 绘制图像
def hand_data(data: pd.DataFrame):
    # 利用matplotlib绘制散点图  （Revise列与Anxiety列） s为点的大小
    plt.scatter(data['Revise'], data['Anxiety'], color='red', s=10)
    # 设置坐标标签，标签位置以及图表标题
    plt.xlabel("Revise")
    plt.ylabel("Anxiety")
    plt.show()

    # 利用pandas的boxplot绘制箱型图
    # 指定分析列为Revise列，用于分组的列为Gender列，即可得到不同性别的箱线图
    data.boxplot(column='Revise', by='Gender')
    plt.show()


def main():
    # 文件路径，注意根据自己所存路径修改
    path = "ExamAnxiety.csv"
    # 利用pandas读取数据
    data = pd.read_csv(path)
    # 简单查看数据基本信息
    print(data.describe())
    # 调用函数绘制图像
    hand_data(data)


if __name__ == "__main__":
    main()