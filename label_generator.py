import numpy as np

# generate the press label


def filter(read_path, write_path):
    data = np.loadtxt(read_path, usecols=(0, 1, 2), dtype=int, delimiter=',')
    f = open(write_path, 'w')
    print(data.mean(0))
    mean = data.mean(0)
    out = []
    for line in data:
        cnt = 0
        for i in range(3):
            if line[i] + 35 < mean[i]:
                cnt += 1
        if cnt > 1:
            out.append(0)
            f.write('0\n')
        else:
            out.append(1)
            f.write('1\n')
    f.close()


IMU_PATH = './Datasets/miniIMU/ori_paths.txt'
data_path_list = []
with open(IMU_PATH, 'r+') as f:
    for line in f.readlines():
        data_path_list.append(line[:-1].split('$'))

for data_path in data_path_list:
    print(data_path[2], data_path[3])
    filter(data_path[2], data_path[3])
