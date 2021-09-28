import pandas as pd
import plotly.graph_objs as go
from plotly.offline import iplot


def draw_picture(pd_data: pd.DataFrame):
    col = list(pd_data.columns)
    col = [i.replace(' ', '') for i in col]
    pd_data.columns = col
    # 设置折线trace1
    # go.Scatter可以创建一个散点图或者折线图的对象，我们将其命名为trace1
    trace1 = go.Scatter(
        x=pd_data.电影名,
        y=pd_data.评论数,
        mode="lines+markers",  # 我们要绘制折线图，所以将mode设置为“lines”
        name="学科水平",  # 将这条折线命名为学科水平
        marker=dict(color='rgba(16, 112, 2, 0.8)'),
        # maker用来定义点的性质，如颜色、大小等
        text=pd_data.评分)  # 将学校名称一列设置为悬停文本（鼠标悬停在图片上方显示的内容）

    # 添加图层layout
    layout = dict(title='Top20电影评论数折线图',  # 设置图像的标题
                  xaxis=dict(title='Top20电影评论数折线图', ticklen=5, zeroline=False)
                  # 设置x轴名称，x轴刻度线的长度，不显示零线
                  )

    # 将data与layout组合为一个图像
    fig = dict(data=trace1, layout=layout)
    # 绘制图像
    iplot(fig)


def main():
    # 文件路径，注意根据自己所存路径修改
    path = "douban_movie_top20.csv"
    # 利用pandas读取数据
    data = pd.read_csv(path)
    print(data)
    # 绘图
    draw_picture(data)


if __name__ == "__main__":
    main()