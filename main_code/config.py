import os

EDGE_NUM = 50       # 边缘服务器数量
ARRIVAL_RATE = 0.5    # 工作流到达率
TIME_SLOT = 1000     # 系统总运行时间
RECEIVE_SLOT = 60    # 接受工作流的时间
FUNC_EXP_TIME = 5   # 函数休眠时间
BANDWIDTH = 100     # 数据传输带宽
DDL = 1.2      # 工作流的截止期（这玩意怎么整）
REQ_PATH = os.path.abspath('./main_code/dataset')
ES_PATH = os.path.abspath('./main_code/data/edge servers')
SAVE_PATH = os.path.abspath('./main_code/result')
