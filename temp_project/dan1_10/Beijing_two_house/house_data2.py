import pandas as pd
import plotly.graph_objs as go
from plotly.offline import iplot


# 不同年份建成房数目
def draw_picture(pd_data: pd.DataFrame):
    count_data = pd_data['建成年份'].value_counts()
    # 构造 trace1
    trace1 = go.Bar(
        x=count_data.index,
        y=count_data.values,
        name="不同年份建成数目",
        marker=dict(color='rgba(255, 174, 255, 0.5)',
                    line=dict(color='rgb(0,0,0)', width=1.5)))
    # barmode：设置条形图的形式，“group”为分组条形图
    layout = go.Layout(barmode="group")
    fig = go.Figure(data=trace1, layout=layout)
    iplot(fig)  # 显示图片(网页显示)


def main():
    # 文件路径，注意根据自己所存路径修改
    path = "house_data.csv"
    # 利用pandas读取数据
    data = pd.read_csv(path)
    print(data)
    # 绘图
    draw_picture(data)


if __name__ == "__main__":
    main()