import matplotlib.pyplot as plt
import pandas as pd

# 为了显示中文，需要更换字体
plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']


def draw_box(df_data: pd.DataFrame):
    # 指定分析列为总价列，用于分组的列为城区列，即可得到各城区的箱线图
    df_data.boxplot(column='总价', by='城区')
    plt.title('北京东二手房总价分析', fontsize=10)
    plt.show()


def main():
    path = "data.csv"
    house_data = pd.read_csv(path)
    draw_box(house_data)


if __name__ == "__main__":
    main()