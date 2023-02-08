import glob
import numpy as np
import os

data = []

filepath = 'data/v2/laplacian8-test'
files = glob.glob(f'{filepath}/*.txt')
files.sort(key = lambda x: int(os.path.basename(x).split('.')[0].split('-')[1]))
for file in files:
    print(f' Loading {os.path.basename(file)}', end='\r')
    with open(file) as f:
        dataTemp = np.array(eval(f.read()))
        for dataDict in dataTemp:
            controlClass = dataDict['class']
            if controlClass == 'CU-nondegen':
                id = dataDict['id']
                id = id[0:2] + id[3:]
                data.append(id)

print(data)
with open('data.txt', 'w') as f:
    f.write(str(data))
