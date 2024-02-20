import servers
import pandas as pd
import random


class Cluster:
    def __init__(self, edge_num, arrival_rate):
        self.server_pool = []       # 资源池
        self.dists = []             # 服务器之间的距离矩阵
        self.edge_num = edge_num    # 边缘服务器数量
        self.arrival_rate = arrival_rate    # 边缘服务器的工作流到达率

        # dists初始化
        # 云服务器
        dist = [0]
        for i in range (edge_num):
            dist.append(10)
        self.dists.append(dist)
        dist = [10]
        # 边缘服务器
        rcsv = pd.read_csv('data/edge servers/server-dist.csv', nrows = edge_num + 1)  
        for row in rcsv.itertuples(index=False):
            for d in row[1:edge_num + 1]:
                dist.append(d)
            self.dists.append(dist)
            dist = [10]

        # server_pool初始化
        arrival_rate = 0.4      # 工作流到达率，平均每秒到达 0.4 个工作流
        func_types = []     # 函数所有种类
        rcsv = pd.read_csv('temp_data/functions.csv')
        for row in rcsv.itertuples(index=False):
            func_types.append(row[0])
        # 云服务器
        cloud_server = servers.Server(0, 10000, 10000000, func_types, arrival_rate)
        self.server_pool.append(cloud_server)
        # 边缘服务器
        for i in range(1, edge_num + 1):
            self.server_pool.append(servers.Server(i, random.uniform(1, 4), random.randint(1024, 4096), random.sample(func_types, random.randint(1, int(len(func_types)/2) + 1)), arrival_rate))

        
