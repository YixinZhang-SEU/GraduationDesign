import csv
import math
 
 
# 计算距离
def getDistance(latA, lonA, latB, lonB):
    ra = 6378140  # 赤道半径
    rb = 6356755  # 极半径
    flatten = (ra - rb) / ra  # Partial rate of the earth
    # change angle to radians
    radLatA = math.radians(latA)
    radLonA = math.radians(lonA)
    radLatB = math.radians(latB)
    radLonB = math.radians(lonB)
 
    pA = math.atan(rb / ra * math.tan(radLatA))
    pB = math.atan(rb / ra * math.tan(radLatB))
    x = math.acos(math.sin(pA) * math.sin(pB) + math.cos(pA) * math.cos(pB) * math.cos(radLonA - radLonB))
    c1 = (math.sin(x) - x) * (math.sin(pA) + math.sin(pB)) ** 2 / math.cos(x / 2) ** 2
    c2 = (math.sin(x) + x) * (math.sin(pA) - math.sin(pB)) ** 2 / math.sin(x / 2) ** 2
    dr = flatten / 8 * (c1 - c2)
    distance = ra * (x + dr)
    distance = round(distance / 1000, 4)
    # return f'{distance}km'
    return distance

# 经纬度放到coordinate数组中
def csv_proc(filename):
    coordinate = []
    with open(filename, 'r') as rf:
        reader = csv.reader(rf)
        next(reader)    # 跳过表头
        for row in reader:
            coordinate.append([float(row[1]), float(row[2])])
    return coordinate, len(coordinate)


# 转换成距离，写入到csv中
def writeCSV():
    coordinate, len = csv_proc('site-optus-melbCBD.csv')
    with open('server-dist.csv', 'w', newline = '') as wf:
        w = csv.writer(wf)

        sno = []
        for i in range(len):
            sno.append(i)
        w.writerow(sno)

        for i in range(1, len):
            data = []
            data.append(i)  # 编号
            for j in range (1, len):
                if i == j:
                    data.append(0)
                else:
                    data.append(getDistance(coordinate[i][0], coordinate[i][1], coordinate[j][0], coordinate[j][1]))
            w.writerow(data)

def main():
    writeCSV()

if __name__ == '__main__':
    main()