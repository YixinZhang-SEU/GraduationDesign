import csv
import os

max_trans_dist = 0.2    # 最大传输距离
readfile = os.path.abspath('./main_code/data/edge servers/server-dist.csv')
writefile = os.path.abspath('./main_code/data/edge servers/dists.csv')


# 读取文件
def csv_proc(filename):
    adj_matrix = []
    with open(filename, 'r') as rf:
        reader = csv.reader(rf)
        next(reader)    # 跳过表头
        for row in reader:
            tmp_list = []
            for i in range(1, len(row)):
                tmp_list.append(round(float(row[i]), 2))
            adj_matrix.append(tmp_list)
    return adj_matrix


# 计算最短路径
def floyd_warshall(adj_matrix):
    # 初始化距离矩阵
    n = len(adj_matrix)
    dist = [[float('inf')] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0
            elif adj_matrix[i][j] <= max_trans_dist:
                dist[i][j] = adj_matrix[i][j]

    # # 更新距离矩阵
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist


# 写入csv文件
def writeCsv(dist):
    with open(writefile, 'w', newline='') as wf:
        w = csv.writer(wf)
        for row in dist:
            tmp_list = []
            for elem in row:
                tmp_list.append(round(elem, 3))
            w.writerow(tmp_list)



if __name__ == '__main__':
    adj_matrix = csv_proc(readfile)
    result = floyd_warshall(adj_matrix)
    writeCsv(result)

