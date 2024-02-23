import matplotlib.pyplot as plt  
import pandas as pd
import numpy as np
import os

# 画图

# filepath = os.path.abspath('../..')
# task_input_filename = os.path.join(filepath, 'dataset/trace2018/batch_instance.csv')

# index_name=['1', '2', '3', '4', '5', '6', '7', '8', '9']
# df = pd.read_csv('instances.csv', header=None, names = index_name)  # 替换为你的CSV文件路径  
  
# # 假设你的CSV文件有两列，分别命名为'column1'和'column2'  
# # 你可以根据需要更改这些列名 

# x = df['6']  # 将'column1'列转换为numpy数组  
# y = df['8']  # 将'column2'列转换为numpy数组  
  
# # 使用polyfit函数进行线性拟合
# coefficients = np.polyfit(x, y, 1)
# p = np.poly1d(coefficients)

# # 绘制原始数据散点图和拟合曲线
# plt.scatter(x, y, label='Data')
# plt.plot(x, p(x), color='r', label='Fitted line')

# # 添加图例和标签
# plt.legend()
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('Linear Regression')
  
# # 保存图形  
# plt.savefig('scatter_plot.png')  # 保存为PNG文件



# 筛数据
