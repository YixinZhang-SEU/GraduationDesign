import csv
import config

func_dict = {}
with open('temp_data/functions.csv', 'r') as rcsv:
    reader = csv.DictReader(rcsv)
    for row in reader:
        value = []
        value += [float(row['CPU']), float(row['Mem']), float(row['Cold_st']), float(row['Exec_time'])]
        func_dict[row['Func_type']] = value


class Function:
    def __init__(self, func_type, belong_server, belong_wf, belong_task):
        self.func_type = func_type
        self.cpu = func_dict[func_type][0]
        self.mem = func_dict[func_type][1]
        self.cold_st = func_dict[func_type][2]
        self.exec_time = func_dict[func_type][3]
        self.start_time = 0
        self.finish_time = self.exec_time
        self.belong_server = belong_server
        self.belong_wf = belong_wf
        self.belong_task = belong_task


    # def __hash__(self):  
    #     return hash((self.belong_wf, self.belong_task))  


    # def __eq__(self, other):  
    #     if isinstance(other, Function):  
    #         return self.belong_wf == other.belong_wf and self.belong_task == other.belong_task
    #     return False
    

    # 函数单程传输时间，加到finish_time中
    # 传输时间 + 传播时间 = 数据量/带宽 + 距离/传播速度
    def funcTransTime(self, exec_server, dists):    # exec_server 指执行的服务器，这个函数给finish_time增加往返时间
        # exec_server = belong_server 则无需任何操作
        if exec_server == self.belong_server:
            return 0
        else:
            t1 = self.mem / config.BANDWIDTH
            t2 = dists[self.belong_server][exec_server] * 2
            return t1 + t2