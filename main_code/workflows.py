import random
import csv
import tasks
from collections import OrderedDict
import os
import config

wfFile = os.path.join(config.REQ_PATH, 'wf.csv')
taskFile = os.path.join(config.REQ_PATH, 'tasks.csv')
saveFile = os.path.join(config.SAVE_PATH, '1.csv')

with open(saveFile, mode='w', newline='') as savefile:  
    writer = csv.writer(savefile)
    writer.writerow(['wf_id', 'start_time', 'finish_time', 'exec_time', 'wf_type'])


def get_wfDict(wfFile):
    wf_dict = {}
    with open(wfFile, 'r') as rcsv:
        reader = csv.DictReader(rcsv)
        for row in reader:
            value = []
            value += [row['Deadline'], row['Tasks']]
            wf_dict[row['WF_Type']] = value
    return wf_dict

def get_wfTypes(wfFile):
    wf_types = []
    with open(wfFile, 'r') as rcsv:
        reader = csv.DictReader(rcsv)
        for row in reader:
            wf_types.append(row['WF_Type'])
    return wf_types


class Workflow:
    def __init__(self, wf_id, server_id, arrival_time, wf_type):
        wf_type_list = get_wfTypes(wfFile)
        wf_dict = get_wfDict(wfFile)
        self.wf_id = wf_id      # 工作流编号
        self.wf_type = wf_type   # 工作流类型
        self.arrival_time = arrival_time      # 工作流到达时间
        self.belong_server = server_id
        self.deadline = arrival_time + int(wf_dict[self.wf_type][0])  # 截止期
        self.tasks = OrderedDict()       # 有序字典，所有任务  {任务id, 任务对象obj}
        self.executing_tasks = {}       # {task_id, task(.obj)}

        with open(taskFile, 'r') as rcsv:
            reader = csv.DictReader(rcsv)
            all_rows = list(reader)
            for row in reversed(all_rows):
                if row['WF_Type'] == self.wf_type:
                    sucs = row['Successor'].split()
                    successors = []
                    if len(sucs) != 0:
                        for suc in sucs:
                            successors.append(self.tasks[suc])
                    this_task = tasks.Task(self.belong_server, self.wf_type, self.wf_id, row['Task_id'], successors, row['Predecessor'])
                    self.tasks[row['Task_id']] = this_task
        
        self.tasks = OrderedDict(reversed(self.tasks.items()))
        self.tasks_left = len(self.tasks)       # 尚未运行的任务数量
        # print(f"Init tasks of wf {self.wf_id} are {self.tasks}.")


    def isCompleted(self):
        return self.tasks_left == 0
    

    def calSatisfaction(self, finish_time):
        with open(saveFile, mode='a', newline='') as savefile:
            writer = csv.writer(savefile)
            writer.writerow([self.wf_id, self.arrival_time, finish_time, finish_time - self.arrival_time, self.wf_type])
        # print(f"Workflow {self.wf_id} is completed, the time is {finish_time}.")