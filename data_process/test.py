import matplotlib.pyplot as plt  
import pandas as pd
import numpy as np
import os
import csv

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
# task
task_file = os.path.abspath('./data_process/tasks.csv')
task_write = os.path.abspath('./data_process/tasks_filtered.csv')
with open(task_file, 'r') as task_input_file, open(task_write, 'w') as task_output_file:
    task_reader = csv.reader(task_input_file)
    wf_writer = csv.writer(task_output_file)

    header = ['WF_Type', 'Func_Num', 'Exec_Time']
    wf_writer.writerow(header)
    for row in task_reader:
        wf_writer.writerow([row[2], row[1], int(row[6])-int(row[5])])

# instance
instance_file = os.path.abspath('./data_process/instances.csv')
instance_write = os.path.abspath('./data_process/instance_filtered.csv')
with open(instance_file, 'r') as instance_input_file, open(instance_write, 'w') as instance_output_file:
    instance_reader = csv.reader(instance_input_file)
    instance_writer = csv.writer(instance_output_file)

    header = ['WF_Type', 'Task_id', 'Exec_Time', 'CPU', 'Mem']
    instance_writer.writerow(header)
    for row in instance_reader:
        instance_writer.writerow([row[2], row[1][1], int(row[6])-int(row[5]), float(row[10])/100.0, float(row[12])*1000])