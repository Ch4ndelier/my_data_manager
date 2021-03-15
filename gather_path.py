import os
## gather the path we need
rootdir = os.path.join('./Datasets/miniIMU')
write_path = open('./Datasets/miniIMU/ori_paths.txt', 'w')
for (dirpath, dirnames, filenames) in os.walk(rootdir):
    for filename in filenames:
        if filename == 'IMU.txt':
            write_path.write(os.path.join(dirpath, filename) + '$')
            write_path.write(os.path.join(dirpath, 'Press.txt') + '$')
            write_path.write(os.path.join(dirpath, 'Press_processed.txt') + '$')
            write_path.write(os.path.join(dirpath, 'press_label.txt') + '\n')

write_path.close()
