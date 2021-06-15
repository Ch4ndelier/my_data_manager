import os
# gather the path we need
rootdir = os.path.join('/Users/liujunyuan/data_manager/BM3D/DIV2K_train_HR/')
write_path = open('/Users/liujunyuan/data_manager/BM3D/paths.txt', 'w')
for (dirpath, dirnames, filenames) in os.walk(rootdir):
    for filename in filenames:
        write_path.write(os.path.join(dirpath, filename) + '\n')

write_path.close()
