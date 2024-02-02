import csv
import os
from tqdm import tqdm 

filepath = os.path.abspath('.')
task_filename = os.path.join(filepath, 'GraduationDesign/data_process/batch_task.csv')
instance_filename = os.path.join(filepath, 'GraduationDesign/data_process/batch_instance.csv')


# n = 1000
# with open(task_filename, 'r') as task_file, open(os.path.join(path, 'GraduationDesign/data_process/task_100.csv'), 'a') as task_w_file:
#     task_reader = csv.reader(task_file)
#     task_writer = csv.writer(task_w_file)
#     for i in tqdm(range(n)):
#         row = next(task_reader)
#         task_writer.writerow(row)

job_set = {'j_49', 'j_66', 'j_79', 'j_230', 'j_293', 'j_583', 'j_783'}

with open(task_filename, 'r') as task_r_file, open(instance_filename, 'r') as instance_r_file, open(os.path.join(filepath,'GraduationDesign/data_process/tasks.csv'), 'a') as task_w_file, open(os.path.join(filepath,'GraduationDesign/data_process/instances.csv'), 'w') as instance_w_file:
    task_reader = csv.reader(task_r_file)
    instance_reader = csv.reader(instance_r_file)
    task_writer = csv.writer(task_w_file)
    instance_writer = csv.writer(instance_w_file)

    # for row in tqdm(task_reader):
    #     if row[2] in job_set:
    #         task_writer.writerow(row)
    # print("===========================")

    for row in tqdm(instance_reader):
        if row[2] in job_set:
            instance_writer.writerow(row)
    print("===========================")