import os
os.environ['PYDEVD_DISABLE_FILE_VALIDATION'] = '1'
import subprocess
import re

# EDGE_NUM = 20       # 边缘服务器数量
# ARRIVAL_RATE = 25
# TIME_SLOT = 10000     # 系统总运行时间(改掉)
# RECEIVE_SLOT = 10    # 接受工作流的时间
# FUNC_EXP_TIME = 26
# BANDWIDTH = 100     # 数据传输带宽
# DDL = 1.2      # 工作流的截止期（这玩意怎么整）
# MAX_CACHE_NUM = 3   # 边缘服务器最多可缓存的函数种类数
# CLOUD_EDGE = 100


# 超参数列表
EDGE_NUM = [10, 20, 30, 40, 50]
ARRIVAL_RATE = [10, 20, 30, 40]
FUNC_EXP_TIME = [5, 10, 15, 20]
CLOUD_EDGE = [50, 100, 150, 200, 250, 300]


# RECEIVE_SLOT = [10, 20, 30]

def update_config(param_name, new_value):
    with open('main_code/config.py', 'r') as f:
        content = f.read()

    # 使用正则表达式查找并替换超参数的值
    content_new = re.sub(f'\\b{param_name}\\b = .*', f'{param_name} = {new_value}', content)
    with open('main_code/config.py', 'w') as f:
        f.write(content_new)


# for en in EDGE_NUM:
#     update_config('EDGE_NUM', en)
#     for ar in ARRIVAL_RATE:
#         update_config('ARRIVAL_RATE', ar)
#         for fet in FUNC_EXP_TIME:
#             update_config('FUNC_EXP_TIME', fet)

#             subprocess.run(['python', 'main_code/temp_main.py'])
#             subprocess.run(['python', 'main_code/dataset/generate_data.py'])
#             subprocess.run(['python', 'main_code/main.py'])
# # 使用示例
# update_config('ARRIVAL_RATE', 1000)
        
for ce in CLOUD_EDGE:
    update_config('CLOUD_EDGE', ce)

    subprocess.run(['python', 'main_code/temp_main.py'])
    subprocess.run(['python', 'main_code/dataset/generate_data.py'])
    subprocess.run(['python', 'main_code/main.py'])