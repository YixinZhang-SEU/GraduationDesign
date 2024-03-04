import csv
import os
import numpy as np
import sys
import random
abs_path = os.path.abspath('./main_code')
sys.path.append(abs_path)
import config


'''
生成tasks.csv
'''
# func_types = []
# func_path = os.path.abspath('./main_code/dataset/func_types.csv')
# with open(func_path, 'r') as read_func:
#     reader = csv.reader(read_func)
#     next(reader)
#     for row in reader:
#         func_types.append(row[0])

# task_write_path = os.path.abspath('./main_code/dataset/tasks.csv')
# task_read_path = os.path.abspath('./data_process/tasks.csv')


# pred = {}
# with open(task_read_path, 'r') as read_task:
#     reader = csv.reader(read_task)
#     for row in reader:
#         task_id = row[0][1]
#         wf_id = row[2]
#         predecessors = row[0][2:].split('_')[1:]
#         if wf_id not in pred.keys():
#             pred[wf_id] = {}
#         pred[wf_id][task_id] = predecessors

# succ = {}
# for key, value in pred.items():
#     if key not in succ.keys():
#         succ[key] = {}
#     for key1, value1 in value.items():
#         for elem in value1:
#             if elem not in succ[key].keys():
#                 succ[key][elem] = []
#             succ[key][elem].append(key1)


# with open(task_read_path, 'r') as read_task, open(task_write_path, 'w') as write_task:
#     reader = csv.reader(read_task)
#     writer = csv.writer(write_task)
#     header = ['WF_Type', 'Task_id', 'Predecessor', 'Successor']
#     writer.writerow(header)

#     for row in reader:
#         wf_type = row[2]
#         task_id = row[0][1]
#         predecessors = ""
#         successcors = ""
#         if task_id in pred[wf_type].keys():
#             for elem in pred[wf_type][task_id]:
#                 predecessors += elem
#                 predecessors += " "
#         if task_id in succ[wf_type].keys():
#             for elem in succ[wf_type][task_id]:
#                 successcors += elem
#                 successcors += " "
#         # func_num = row[1]
#         # funcs = ""
#         # for i in range(int(func_num)):
#         #     funcs += random.choice(func_types)
#         #     funcs += " "

#         writer.writerow([wf_type, task_id, predecessors, successcors])


'''
生成server_wfs.csv : 服务器到达工作流数量
'''

RECEIVE_SLOT = config.RECEIVE_SLOT
EDGE_NUM = config.EDGE_NUM
ARRIVAL_RATE = config.ARRIVAL_RATE

# 所有工作流类型
wf_list = []
wf_path = os.path.abspath('./main_code/dataset/wf.csv')
with open(wf_path, 'r') as read_wf:
    reader = csv.reader(read_wf)
    next(reader)
    for row in reader:
        wf_list.append(row[0])      # WF_Type字段

# 生成每个服务器每秒到达工作流数量，并随机生成工作流类型，存入wf_nums.csv
wf_nums_path = os.path.abspath('./main_code/dataset/server_wfs.csv')
with open(wf_nums_path, 'w') as write_wf_nums:
    writer = csv.writer(write_wf_nums)
    for i in range(RECEIVE_SLOT):
        row = []
        row.append(i)
        for server in range(EDGE_NUM):
            arrivals = np.random.poisson(ARRIVAL_RATE)
            tmp = ""
            for _ in range(arrivals):
                tmp += random.choice(wf_list)  # 随机选择一种工作流
                tmp += " "
            row.append(tmp)
        writer.writerow(row)