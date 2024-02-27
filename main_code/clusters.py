import servers
import pandas as pd
import random
import os
import config

es_filename = os.path.join(config.ES_PATH, 'server-dist.csv')
func_filename = os.path.join(config.REQ_PATH, 'functions.csv')


class Cluster:
    def __init__(self, edge_num):
        self.server_pool = []       # 资源池
        self.dists = []             # 服务器之间的距离矩阵
        self.edge_num = edge_num    # 边缘服务器数量

        # dists初始化
        # 云服务器
        dist = [0]
        for i in range (edge_num):
            dist.append(10)
        self.dists.append(dist)
        dist = [10]
        # 边缘服务器
        rcsv = pd.read_csv(es_filename, nrows = edge_num + 1)  
        for row in rcsv.itertuples(index=False):
            for d in row[1:edge_num + 1]:
                dist.append(d)
            self.dists.append(dist)
            dist = [10]

        # server_pool初始化
        func_types = []     # 函数所有种类
        rcsv = pd.read_csv(func_filename)
        for row in rcsv.itertuples(index=False):
            func_types.append(row[0])
        # 云服务器
        cloud_server = servers.Server(0, 10000, 10000000, func_types)
        self.server_pool.append(cloud_server)
        # 边缘服务器
        for i in range(1, edge_num + 1):
            self.server_pool.append(servers.Server(i, random.uniform(1, 4), random.randint(1024, 4096), random.sample(func_types, random.randint(1, int(len(func_types)/2) + 1))))

        
