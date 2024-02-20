import csv


'''
存储工作流信息
[ 工作流编号 | 截止期 | 顶点集 | 边集 ]
''' 
with open('temp_data/wf.csv', 'w', newline='') as wfcsv:
    w = csv.writer(wfcsv)
    w.writerow(["WF_Type", "Deadline", "Tasks", "Edges"])

    w.writerow(["WF_1", 15, "1,2,3,4,5,6", "(1,2),(1,3),(2,4),(3,5),(4,6),(5,6)"])
    w.writerow(["WF_2", 5, "1,2,3", "(1,2),(1,3),(2,3)"])
    w.writerow(["WF_3", 10, "1,2,3,4", "(1,2),(1,3),(2,4),(3,4)"])


'''
存储任务依赖关系
[ 任务所属工作流编号 | 任务编号 | 前驱 | 后继 | 函数类型 ]
'''
with open('temp_data/tasks.csv', 'w', newline='') as dagcsv:
    w = csv.writer(dagcsv)
    w.writerow(["WF_Type", "Task_id", "Predecessor", "Successor", "Func_types"])

    # # 根据 wf.csv 生成 tasks.csv (待续)
    # data = []
    # with open ('wf.csv', 'r') as wfcsv:
    #     reader = csv.DictReader(wfcsv)
    #     for row in reader:
    #         data.append(row['WF_num'])

    # 手动添加
    w.writerow(["WF_1", 1,"", "2,3", "A,B"])
    w.writerow(["WF_1", 2, "1", "4", "A,C"])
    w.writerow(["WF_1", 3, "1", "5", "B,C"])
    w.writerow(["WF_1", 4, "2", "6", "C,D"])
    w.writerow(["WF_1", 5, "3", "6", "C,E"])
    w.writerow(["WF_1", 6, "4,5", "", "D,E"])

    w.writerow(["WF_2", 1, "", "2,3", "A,B"])
    w.writerow(["WF_2", 2, "1", "3", "A,C"])
    w.writerow(["WF_2", 3, "1,2", "", "B,C"])

    w.writerow(["WF_3", 1, "", "2,3", "B,C"])
    w.writerow(["WF_3", 2, "1", "4", "B,C"])
    w.writerow(["WF_3", 3, "1", "4", "B,C"])
    w.writerow(["WF_3", 4, "2,3", "", "B,C"])



'''
存储函数信息
[ 函数类型 | 所需CPU | 数据量 | 冷启动时间 | 执行时间 ]
'''
with open('temp_data/functions.csv', 'w', newline='') as funcsv:
    w = csv.writer(funcsv)
    w.writerow(["Func_type", "CPU", "Mem", "Cold_st", "Exec_time"])

    w.writerow(["A", 0.5, 2, 1, 5])
    w.writerow(["B", 0.8, 1.5, 1, 5])
    w.writerow(["C", 0.3, 3, 1, 5])
    w.writerow(["D", 1.5, 2.5, 1, 5])
    w.writerow(["E", 0.6, 1, 1, 5])