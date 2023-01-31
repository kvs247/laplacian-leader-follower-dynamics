import numpy as np
import matplotlib.pyplot as plt

path3 = 'data/laplacian3-20230131-115435.txt'
path4 = 'data/laplacian4-20230131-115442.txt'
path5 = 'data/laplacian5-20230131-115446.txt'
path6 = 'data/laplacian6-20230131-115459.txt'
path7 = 'data/laplacian7-20230131-115545.txt'

numMats3 = (2 ** ((3 / 2) * (3 - 1))) - 2
numMats4 = (2 ** ((4 / 2) * (4 - 1))) - 2
numMats5 = (2 ** ((5 / 2) * (5 - 1))) - 2
numMats6 = (2 ** ((6 / 2) * (6 - 1))) - 2
numMats7 = (2 ** ((7 / 2) * (7 - 1))) - 2

with open(path3) as f:
    data3 = np.array(eval(f.read()))
ec3 = [dataObj['id'] for dataObj in data3 if dataObj['class'] == 'EC']
cc3 = [dataObj['id'] for dataObj in data3 if dataObj['class'] == 'CC']
cu3 = [dataObj['id'] for dataObj in data3 if dataObj['class'].startswith('CU')]
cudis3 = [dataObj['id'] for dataObj in data3 if dataObj['class'] == 'CU-dis']
cudegen3 = [dataObj['id'] for dataObj in data3 if dataObj['class'] == 'CU-degen']
cunondegen3 = [dataObj['id'] for dataObj in data3 if dataObj['class'] == 'CU-nondegen']

with open(path4) as f:
    data4 = np.array(eval(f.read()))
ec4 = [dataObj['id'] for dataObj in data4 if dataObj['class'] == 'EC']
cc4 = [dataObj['id'] for dataObj in data4 if dataObj['class'] == 'CC']
cu4 = [dataObj['id'] for dataObj in data4 if dataObj['class'].startswith('CU')]
cudis4 = [dataObj['id'] for dataObj in data4 if dataObj['class'] == 'CU-dis']
cudegen4 = [dataObj['id'] for dataObj in data4 if dataObj['class'] == 'CU-degen']
cunondegen4 = [dataObj['id'] for dataObj in data4 if dataObj['class'] == 'CU-nondegen']

with open(path5) as f:
    data5 = np.array(eval(f.read()))
ec5 = [dataObj['id'] for dataObj in data5 if dataObj['class'] == 'EC']
cc5 = [dataObj['id'] for dataObj in data5 if dataObj['class'] == 'CC']
cu5 = [dataObj['id'] for dataObj in data5 if dataObj['class'].startswith('CU')]
cudis5 = [dataObj['id'] for dataObj in data5 if dataObj['class'] == 'CU-dis']
cudegen5 = [dataObj['id'] for dataObj in data5 if dataObj['class'] == 'CU-degen']
cunondegen5 = [dataObj['id'] for dataObj in data5 if dataObj['class'] == 'CU-nondegen']

with open(path6) as f:
    data6 = np.array(eval(f.read()))
ec6 = [dataObj['id'] for dataObj in data6 if dataObj['class'] == 'EC']
cc6 = [dataObj['id'] for dataObj in data6 if dataObj['class'] == 'CC']
cu6 = [dataObj['id'] for dataObj in data6 if dataObj['class'].startswith('CU')]
cudis6 = [dataObj['id'] for dataObj in data6 if dataObj['class'] == 'CU-dis']
cudegen6 = [dataObj['id'] for dataObj in data6 if dataObj['class'] == 'CU-degen']
cunondegen6 = [dataObj['id'] for dataObj in data6 if dataObj['class'] == 'CU-nondegen']

with open(path7) as f:
    data7 = np.array(eval(f.read()))
ec7 = [dataObj['id'] for dataObj in data7 if dataObj['class'] == 'EC']
cc7 = [dataObj['id'] for dataObj in data7 if dataObj['class'] == 'CC']
cu7 = [dataObj['id'] for dataObj in data7 if dataObj['class'].startswith('CU')]
cudis7 = [dataObj['id'] for dataObj in data7 if dataObj['class'] == 'CU-dis']
cudegen7 = [dataObj['id'] for dataObj in data7 if dataObj['class'] == 'CU-degen']
cunondegen7 = [dataObj['id'] for dataObj in data7 if dataObj['class'] == 'CU-nondegen']

x = [3, 4, 5, 6, 7]
yEC = [len(ec3)/numMats3, len(ec4)/numMats4, len(ec5)/numMats5, len(ec6)/numMats6, len(ec7)/numMats7]
yCC = [len(cc3)/numMats3, len(cc4)/numMats4, len(cc5)/numMats5, len(cc6)/numMats6, len(cc7)/numMats7]
yCU = [len(cu3)/numMats3, len(cu4)/numMats4, len(cu5)/numMats5, len(cu6)/numMats6, len(cu7)/numMats7]

plt.plot(x, yEC, label='ec')
plt.plot(x, yCC, label='cc')
plt.plot(x, yCU, label='cu')
plt.legend()
plt.savefig('fig.png')

plt.close()

numCUMats3 = len(cu3)
numCUMats4 = len(cu4)
numCUMats5 = len(cu5)
numCUMats6 = len(cu6)
numCUMats7 = len(cu7)

yCUdis = [len(cudis3)/numCUMats3, len(cudis4)/numCUMats4, len(cudis5)/numCUMats5, len(cudis6)/numCUMats6, len(cudis7)/numCUMats7]
yCUdegen = [len(cudegen3)/numCUMats3, len(cudegen4)/numCUMats4, len(cudegen5)/numCUMats5, len(cudegen6)/numCUMats6, len(cudegen7)/numCUMats7]
yCUnondegen = [len(cunondegen3)/numCUMats3, len(cunondegen4)/numCUMats4, len(cunondegen5)/numCUMats5, len(cunondegen6)/numCUMats6, len(cunondegen7)/numCUMats7]

plt.plot(x, yCUdis, label='cu-dis')
plt.plot(x, yCUdegen, label='cu-degen')
plt.plot(x, yCUnondegen, label='cu-nondegen')
plt.legend()
plt.savefig('fig2.png')