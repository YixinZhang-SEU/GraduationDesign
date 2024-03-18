import os
import csv
import config
import random
import functions as F




functionFile = os.path.abspath('./data_process/instance_filtered.csv')
funcDict = {}
with open(functionFile, 'r') as read_func:
    reader = csv.reader(read_func)
    next(reader)
    for row in reader:
        if row[0] not in funcDict.keys():
            funcDict[row[0]] = {}
        if row[1] not in funcDict[row[0]].keys():
            funcDict[row[0]][row[1]] = []
        funcDict[row[0]][row[1]].append([row[2], row[3], row[4], random.choice(config.FUNC_TYPES)])


class Task(object):

    def __init__(self, belong_server, wf_type, belong_wf, task_id, children, parents):
        self.belong_server = belong_server      # 该任务隶属的服务器
        self.belong_wf = belong_wf              # 隶属工作流
        self.task_id = task_id  # 该任务编号
        self.functions = {}       # 该任务拆分成的函数 {func_id, func(.obj)}
        self.children = children                    # 该任务的后继
        self.parents = parents.split()           # 该任务的前驱
        if len(self.parents) == 0:
            self.predecessors_left = 0      # 该任务的前驱剩余未完成的数量
        else:
            self.predecessors_left = len(self.parents)
        # print(f"^^^^^task {self.task_id} parents are {self.parents}, pr_len = {len(self.parents)}, pred are {self.predecessors_left}")

        # self.exec_start_time = 0                    # 该任务被调度器接收的时间（即开始执行的时间）
        self.finish_time = 0

        # 将函数列表的元素转化成函数类对象
        func_id = 0
        for func_list in funcDict[wf_type][task_id]:
            self.functions[func_id] = F.Function(func_id, self.belong_server, self.belong_wf, self.task_id, func_list[3], func_list[0], func_list[1], func_list[2])
            func_id += 1

        self.functions_left = len(self.functions)        # 该任务的函数剩余未完成数量

        
    # 判断该任务是否可以开始运行
    def isOK(self):
        return self.parents == '' or self.predecessors_left == 0
    
    # 判断该任务是否已经运行完成
    def isDone(self):
        return self.functions_left == 0
    
    # 更改开始执行时间
    def changeStartTime(self, execute_time):
        # self.exec_start_time = execute_time
        for func in self.functions.values():
            func.start_time = execute_time
