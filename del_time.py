press_path = "./Datasets/miniIMU/20201127 10:26:58 /IMURecord/Press.txt"
write_path = "./test.txt"
f2 = open(write_path, 'w')
with open(press_path, 'r+') as f:
    for line in f.readlines():
        if len(line.split()) == 3:
            line = line.split()[2] + '\n'
        f2.write(line)
f2.close()
