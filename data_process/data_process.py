import csv
import os
from tqdm import tqdm 

filepath = os.path.abspath('.')
task_filename = os.path.join(filepath, 'GraduationDesign/data_process/batch_task.csv')
instance_filename = os.path.join(filepath, 'GraduationDesign/data_process/batch_instance.csv')
common_filename = os.path.join(filepath, 'GraduationDesign/data_process/common.txt')

task_job_set = set()
instance_job_set = set()

with open(task_filename, 'r') as task_input_file, open(instance_filename, 'r') as instance_input_file, open('GraduationDesign/data_process/instance_job.csv', 'a') as instance_output_file, open('GraduationDesign/data_process/task_job.csv', 'a') as task_output_file, open('GraduationDesign/data_process/instance_job.csv', 'a') as instance_output_file, open(common_filename, 'a') as common_input_file, open(common_filename, 'r') as common_output_file:  
    task_reader = csv.reader(task_input_file)  
    instance_reader = csv.reader(instance_input_file)  
    task_writer = csv.writer(task_output_file)  
    instance_writer = csv.writer(instance_output_file)  

    # for row in tqdm(task_reader):
    #     task_job_set.add(row[2])
    # print('===================================')
    
    # for row in tqdm(instance_reader):
    #     instance_job_set.add(row[2])
    # print('===================================')

    # common_set = task_job_set & instance_job_set
    # # common_set写入txt
    # common_input_file.write(','.join(common_set))

    # common_list = common_output_file.read().split(',')
    # common_set = set(common_list)

    # print(common_set)

    # for row in tqdm(task_reader):
    #     if row[2] in common_set and row[1] != '1':
    #         task_writer.writerow(row)
    
    # for row in tqdm(instance_reader):
    #     if row[2] in common_set and row[0] != '1':
    #         instance_writer.writerow(row)