import csv
import os
from tqdm import tqdm
import pandas as pd

# 提取相交job

# filepath = os.path.abspath('.')
# task_filename = os.path.join(filepath, 'GraduationDesign/data_process/batch_task.csv')
# instance_filename = os.path.join(filepath, 'GraduationDesign/data_process/batch_instance.csv')
# common_filename = os.path.join(filepath, 'GraduationDesign/data_process/common.txt')

# task_job_set = set()
# instance_job_set = set()

# with open(task_filename, 'r') as task_input_file, open(instance_filename, 'r') as instance_input_file, open('GraduationDesign/data_process/instance_job.csv', 'a') as instance_output_file, open('GraduationDesign/data_process/task_job.csv', 'a') as task_output_file, open('GraduationDesign/data_process/instance_job.csv', 'a') as instance_output_file, open(common_filename, 'a') as common_input_file, open(common_filename, 'r') as common_output_file:  
#     task_reader = csv.reader(task_input_file)  
#     instance_reader = csv.reader(instance_input_file)  
#     task_writer = csv.writer(task_output_file)  
#     instance_writer = csv.writer(instance_output_file)  

#     for row in tqdm(task_reader):
#         task_job_set.add(row[2])
#     print('===================================')
    
#     for row in tqdm(instance_reader):
#         instance_job_set.add(row[2])
#     print('===================================')

#     common_set = task_job_set & instance_job_set
#     # common_set写入txt
#     common_input_file.write(','.join(common_set))

#     common_list = common_output_file.read().split(',')
#     common_set = set(common_list)

#     print(common_set)

#     for row in tqdm(task_reader):
#         if row[2] in common_set and row[1] != '1':
#             task_writer.writerow(row)
    
#     for row in tqdm(instance_reader):
#         if row[2] in common_set and row[0] != '1':
#             instance_writer.writerow(row)




# tasks.csv / instance.csv

# filepath = os.path.abspath('.')
# task_filename = os.path.join(filepath, 'GraduationDesign/data_process/batch_task.csv')
# instance_filename = os.path.join(filepath, 'GraduationDesign/data_process/batch_instance.csv')

# n = 1000
# with open(task_filename, 'r') as task_file, open(os.path.join(path, 'GraduationDesign/data_process/task_100.csv'), 'a') as task_w_file:
#     task_reader = csv.reader(task_file)
#     task_writer = csv.writer(task_w_file)
#     for i in tqdm(range(n)):
#         row = next(task_reader)
#         task_writer.writerow(row)

# job_set = {'j_49', 'j_66', 'j_79', 'j_230', 'j_293', 'j_583', 'j_783'}

# with open(task_filename, 'r') as task_r_file, open(instance_filename, 'r') as instance_r_file, open(os.path.join(filepath,'GraduationDesign/data_process/tasks.csv'), 'a') as task_w_file, open(os.path.join(filepath,'GraduationDesign/data_process/instances.csv'), 'a') as instance_w_file:
#     task_reader = csv.reader(task_r_file)
#     instance_reader = csv.reader(instance_r_file)
#     task_writer = csv.writer(task_w_file)
#     instance_writer = csv.writer(instance_w_file)

#     # for row in tqdm(task_reader):
#     #     if row[2] in job_set:
#     #         task_writer.writerow(row)
#     # print("===========================")

#     for row in tqdm(instance_reader):
#         if row[2] in job_set:
#             instance_writer.writerow(row)
#     print("===========================")


# 提取出job相同的 instance_all, task_all

filepath = os.path.abspath('../..')
task_input_filename = os.path.join(filepath, 'dataset/trace2018/batch_task.csv')
task_output_filename = os.path.join(filepath, 'dataset/trace2018/tasks_all.csv')
instance_input_filename = os.path.join(filepath, 'dataset/trace2018/batch_instance.csv')
instance_output_filename = os.path.join(filepath, 'dataset/trace2018/instances_all.csv')
common_filename = os.path.join(os.path.abspath('.'), 'data_process/common.txt')


with open(task_input_filename, 'r') as task_input_file, open(instance_input_filename, 'r') as instance_input_file, open(task_output_filename, 'w') as task_output_file, open(instance_output_filename, 'w') as instance_output_file, open(common_filename, 'r') as common_output_file:
    task_reader = csv.reader(task_input_file)  
    instance_reader = csv.reader(instance_input_file)  
    task_writer = csv.writer(task_output_file)  
    instance_writer = csv.writer(instance_output_file)  

    common_list = common_output_file.read().split(',')
    common_set = set(common_list)

    for row in tqdm(task_reader):
        if row[2] in common_set:
            task_writer.writerow(row)
    
    print("==============================")
    
    for row in tqdm(instance_reader):
        if row[2] in common_set and row[0]:
            instance_writer.writerow(row)



# 先洗掉不要的字段
# filepath = os.path.abspath('.')
# task_filename = os.path.join(filepath, 'data_process/tasks.csv')

# index_name=['task_name', 'inst_num', 'job_name', 'task_type', 'status', 'start_time', 'end_time' ,  'plan_cpu', 'plan_mem']
# df = pd.read_csv(task_filename, header=None, names = index_name)

# df2 = df.drop(['task_type', 'status'], axis = 1)
# df2.to_csv("new_tasks.csv", mode='a', header=None, index=0)