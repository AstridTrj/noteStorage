import pandas as pd
import plotly.graph_objs as go
from plotly.offline import iplot
from plotly import tools


# 总价和面积箱型图
def draw_picture(pd_data: pd.DataFrame):
    # 准备数据
    trace0 = go.Box(
        y=pd_data.总价,
        name='总价',
        marker=dict(
            color='rgb(12, 12, 140)',
        )
    )
    trace1 = go.Box(
        y=pd_data.面积,
        name='面积',
        marker=dict(
            color='rgb(12, 128, 128)',
        )
    )
    data = [trace0, trace1]
    iplot(data)


def main():
    # 文件路径，注意根据自己所存路径修改
    path = "house_data.csv"
    # 利用pandas读取数据
    data = pd.read_csv(path, encoding='utf-8')
    print(data)
    # 绘图
    draw_picture(data)


if __name__ == "__main__":
    main()