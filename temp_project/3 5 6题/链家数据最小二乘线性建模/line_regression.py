import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 为了显示中文，需要更换字体
plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']


# 数据拟合建模, 计算出拟合直线斜率和截距
def fit_data(df_data: pd.DataFrame):
    # 取出面积和总价
    area, price = df_data['面积'], df_data['总价']
    # 利用最小二乘法拟合数据，得到直线斜率和截距
    # 计算面积和总价的均值
    area_average, price_average = np.mean(area), np.mean(price)
    first, second = 0, 0
    # 根据最小二乘公式迭代计算
    for i in range(len(area)):
        first += (area[i] - area_average) * (price[i] - price_average)
        second += (area[i] - area_average) ** 2
    # 计算斜率
    slope = first / float(second)
    # 计算截距
    dis = price_average - slope * area_average
    return slope, dis


# 绘图展示
def draw_data(data: pd.DataFrame, slope: float, distance: float):
    # 绘制数据散点图  可看出大体分布
    plt.scatter(data['面积'], data['总价'], color='red', s=0.3)
    # 绘制最小二乘拟合的直线
    plt.plot(data['面积'], slope * data['面积'] + distance, color='black', linewidth=1, label='y = %.2fx + %.2f' % (slope, distance))
    # 设置坐标标签，标签位置以及图表标题
    plt.xlabel("The area of the house")
    plt.ylabel("The price of the house")
    plt.legend(loc='upper left')
    plt.title("北京市各区房屋面积和总价关系图")
    # 显示图像
    plt.show()


def main():
    path = "data.csv"
    house_data = pd.read_csv(path)
    slope, distance = fit_data(house_data)
    draw_data(house_data, slope, distance)


if __name__ == "__main__":
    main()