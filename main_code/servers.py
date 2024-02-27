import numpy as np
import csv
import random
import workflows
import os
import config

filename = os.path.join(config.REQ_PATH, 'wf.csv')

# 所有工作流类型
wf_dict = {}
wf_types = []
with open(filename, 'r') as rcsv:
    reader = csv.DictReader(rcsv)
    for row in reader:
        value = []
        value += [row['Deadline'], row['Tasks']]
        wf_dict[row['WF_Type']] = value
        wf_types.append(row['WF_Type'])


class Server:
    def __init__(self, server_id, cpu_capacity, mem_capacity, func_types):
        self.server_id = server_id          # 0表示云服务器， 否则表示边缘服务器编号
        self.cpu_capacity = cpu_capacity    # 当前可用cpu
        self.mem_capacity = mem_capacity    # 当前可用内存       
        self.executing_queue = []   # 执行队列 [func(.obj)]
        self.workflow_queue = {}    # 接收到的工作流队列 {wf_id, wf(.obj)}
        self.func_types = {}                # 缓存的函数列表 {函数类型: 上一次使用时间}，-1表示从未使用过
        for f_type in func_types:
            self.func_types[f_type] = -1


    # 接收工作流，解构，把任务拆解成函数，按照任务的拓扑顺序（？）加入到等待队列中
    def receive_workflow(self, workflow_id, server_id, arrival_time):
        this_wf = workflows.Workflow(workflow_id, server_id, arrival_time)
        self.workflow_queue[workflow_id] = this_wf    # 工作流整体添加到服务器的工作流队列中
        # print(f"wf rec, workflow_type is {self.workflow_queue[workflow_id].wf_type}") #, task_id_0 is {this_wf.tasks[0]} task_0_parents are {this_wf.tasks[0].isOK()}.")
        # print(f"func_types of server {self.server_id} are {self.func_types}.")



        

        
        


        
        

    