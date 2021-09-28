import pandas as pd
import plotly.graph_objs as go
from plotly.offline import iplot


# top20学校的总分和学科水平柱状图
def draw_picture(pd_data: pd.DataFrame):
    # 构造 trace1
    trace1 = go.Bar(
        x=pd_data.学校名称,
        y=pd_data.总分,
        name="总分",
        marker=dict(color='rgba(255, 174, 255, 0.5)',
                    line=dict(color='rgb(0,0,0)', width=1.5)),
        text=pd_data.省市)
    # 构造 trace2
    trace2 = go.Bar(
        x=pd_data.学校名称,
        y=pd_data.学科水平,
        name="学科水平",
        marker=dict(color='rgba(255, 255, 128, 0.5)',
                    line=dict(color='rgb(0,0,0)', width=1.5)),
        text=pd_data.省市)
    data = [trace1, trace2]
    # barmode：设置条形图的形式，“group”为分组条形图
    layout = go.Layout(barmode="group")
    fig = go.Figure(data=data, layout=layout)
    iplot(fig)  # 显示图片(网页显示)


def main():
    # 文件路径，注意根据自己所存路径修改
    path = "China_school_top20.xlsx"
    # 利用pandas读取数据
    data = pd.read_excel(path)
    print(data)
    # 绘图
    draw_picture(data)


if __name__ == "__main__":
    main()