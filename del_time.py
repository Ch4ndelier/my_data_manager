IMU_PATH = './Datasets/miniIMU/ori_paths.txt'


def del_time(press_path, write_path):
    f2 = open(write_path, 'w')
    with open(press_path, 'r+') as f:
        for line in f.readlines():
            if len(line.split()) == 3:
                line = line.split()[2] + '\n'
            f2.write(line)
    f2.close()


data_path_list = []
with open(IMU_PATH, 'r+') as f:
    for line in f.readlines():
        data_path_list.append(line[:-1].split('$'))

# print(data_path_list)
for data_path in data_path_list:
    print(data_path)
    del_time(data_path[1], data_path[2])
