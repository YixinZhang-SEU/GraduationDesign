import csv
import config
import os

func_path = os.path.join(config.REQ_PATH, 'func_types.csv')
funcTypeDict = {}
with open(func_path, 'r') as read_func:
    reader = csv.reader(read_func)
    next(reader)
    for row in reader:
        if row[0] not in funcTypeDict.keys():
            funcTypeDict[row[0]] = []
        funcTypeDict[row[0]] += [row[1], row[2]]


class Function:
    def __init__(self, func_id, belong_server, belong_wf, belong_task, func_type, exec_time, cpu, mem):
        self.func_id = func_id
        self.func_type = func_type
        self.cpu = float(cpu)
        self.mem = float(mem)
        self.cold_st = float(funcTypeDict[func_type][0])
        self.cache_mem = int(funcTypeDict[func_type][1])
        self.exec_time = float(exec_time)
        self.start_time = 0
        self.finish_time = self.exec_time
        self.belong_server = belong_server
        self.belong_wf = belong_wf
        self.belong_task = belong_task
        self.exec_server = -1
            

    # 函数单程传输时间，加到finish_time中
    # 传输时间 + 传播时间 = 数据量/带宽 + 距离/传播速度
    # flag = 1: 函数本身；flag = 0: 函数镜像
    def funcTransTime(self, exec_server, dists, flag):    # exec_server 指执行的服务器，这个函数给finish_time增加往返时间
        # exec_server = belong_server 则无需任何操作
        if exec_server == self.belong_server:
            return 0
        else:
            if flag == 1: 
                t1 = self.mem / config.BANDWIDTH
            else:
                t1 = self.cache_mem / config.BANDWIDTH
            t2 = dists[self.belong_server][exec_server] * 2
            return t1 + t2