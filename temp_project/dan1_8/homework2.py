import numpy as np
import matplotlib.pyplot as plt

alpha = 0.2  # 学习率
eps = 1e-4  # 误差阈值

friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
max_x = max(friends)  # 用于归一化  防止数据溢出
friends = [x / max_x for x in friends]
friends = np.array(friends)


# 利用矩阵的方式求解最小二乘参数
def solve_by_gd_matrix():
    x0 = [1.0 for i in range(9)]
    # 将friends转化为矩阵形式
    xarray = np.column_stack((friends, x0))
    xmatrix = np.mat(xarray, float)
    # 将minutes转化为矩阵形式
    yarray = np.array(minutes)
    ymatrix = np.mat(yarray, float)
    # 计算最小二乘参数
    theta = (xmatrix.T * xmatrix).I * xmatrix.T * ymatrix.T
    theta = theta.tolist()
    print(theta[0][0])

    # 绘制数据散点图  可看出大体分布
    plt.scatter(friends, minutes, color='red', s=10)
    # 绘制最小二乘拟合的直线
    plt.plot(friends, theta[0][0] * friends + theta[1][0], color='black', linewidth=1,
             label='y = %.2f x %.2f' % (theta[0][0], theta[1][0]))
    # 设置坐标标签，标签位置以及图表标题
    plt.xlabel("Number of friends")
    plt.ylabel("Minutes online")
    # 显示图像
    plt.show()


# 利用梯度下降方式求解最小二乘参数
def solve_by_gradient():
    # m为friends数组长度  也即人数个数
    m = len(friends)
    # a为斜率，b为截距，初始设置为0
    a, b = 0, 0
    sse, sse_new = 0, 0
    grad_a, grad_b = 0, 0
    count = 0
    # 循环迭代，可设置迭代次数
    for step in range(10000):
        count += 1
        # 计算每次的梯度，并更新a和b
        for i in range(m):
            # 计算梯度
            base = a * friends[i] + b - minutes[i]
            grad_a += friends[i] * base
            grad_b += base
            grad_a = grad_a / m
            grad_b = grad_b / m
            # 利用计算的梯度和设置的步长更新a，b
            a -= alpha * grad_a
            b -= alpha * grad_b

            # 损失函数： 均方差Mean Squared Error, MSE
            for j in range(m):
                sse_new += (a * friends[j] + b - minutes[j]) ** 2
        # 如果满足误差阈值则退出迭代
        if abs(sse_new - sse) < eps:
            break
        else:
            sse = sse_new
    # 查看迭代得到的参数
    print('{0} * x  {1}'.format(a, b))
    print("count is: ", count)

    # 绘制数据散点图  可看出大体分布
    plt.scatter(friends, minutes, color='red', s=10)
    # 绘制最小二乘拟合的直线
    plt.plot(friends, a * friends + b, color='black', linewidth=1,
             label='y = %.2f x %.2f' % (a, b))
    # 设置坐标标签，标签位置以及图表标题
    plt.xlabel("Number of friends")
    plt.ylabel("Minutes online")
    # 显示图像
    plt.show()


if __name__ == "__main__":
    solve_by_gradient()
    solve_by_gd_matrix()