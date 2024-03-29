import os
import csv

EDGE_NUM = 50
ARRIVAL_RATE = 25
TIME_SLOT = 10000     # 系统总运行时间(改掉)
RECEIVE_SLOT = 10    # 接受工作流的时间
FUNC_EXP_TIME = 26
BANDWIDTH = 100     # 数据传输带宽
DDL = 1.2      # 工作流的截止期（这玩意怎么整）
MAX_CACHE_NUM = 3   # 边缘服务器最多可缓存的函数种类数
REQ_PATH = os.path.abspath('./main_code/dataset')
ES_PATH = os.path.abspath('./main_code/data/edge servers')
SAVE_PATH = os.path.abspath('./main_code/result')
CLOUD_EDGE = 100

FUNC_TYPES = []
func_path = os.path.join(REQ_PATH, 'func_types.csv')
with open(func_path, 'r') as read_func:
    reader = csv.reader(read_func)
    next(reader)
    for row in reader:
        FUNC_TYPES.append(row[0])
