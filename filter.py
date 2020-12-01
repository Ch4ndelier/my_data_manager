import numpy as np
import matplotlib.pyplot as plt
Path = "./Datasets/miniIMU/20201127 15:47:28 /IMURecord/Press_processed.txt"
data = np.loadtxt(Path, usecols=(0, 1, 2), dtype=int, delimiter=',')
print(data)
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
    else:
        out.append(1)

N = len(out)
cnt = 0
for i in range(N):
    if i and out[i] > out[i - 1]:
        cnt += 1
        print(i)

print('cnt', cnt)
plt.plot(out)
plt.show()
