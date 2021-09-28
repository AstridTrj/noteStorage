import pandas as pd
import plotly.graph_objs as go
from plotly.offline import iplot
import pandas as pd
# 不同装修类型所占比例
def draw_picture(pd_data: pd.DataFrame):
    count_data = pd_data['装修'].value_counts()
    # 准备数据
    pie1 = count_data.values
    labels = count_data.index
    # figure
    fig = {
        "data": [
            {
                "values": pie1,  # 值
                "labels": labels,  # 标签
                "domain": {"x": [0, 1]},
                "name": "不同装修类型所占比例",
                "hoverinfo": "label+percent",
                "hole": .3,
                "type": "pie"
            }, ],
        "layout": {
            "title": "不同装修类型所占比例",
            "annotations": [
                {"font": {"size": 20},
                 "showarrow": False,
                 "text": "",
                 "x": 0.3,
                 "y": 1
                 },
            ]
        }
    }
    iplot(fig)


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