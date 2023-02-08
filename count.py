import numpy as np
import matplotlib.pyplot as plt
import glob
import sys
import os
import datetime


start = datetime.datetime.now()

data = dict({
    'EC': 0,
    'CC': 0,
    'CU-dis': 0,
    'CU-degen': 0,
    'CU-nondegen': 0
})

dataDir = 'data/v2/laplacian8-test'
files = glob.glob(f'{dataDir}/*.txt')
files.sort(key = lambda x: int(os.path.basename(x).split('.')[0].split('-')[1]))
for file in files:
    print(f' Loading {os.path.basename(file)}', end='\r')
    with open(file) as f:
        dataTemp = np.array(eval(f.read()))
        for dataDict in dataTemp:
            controlClass = dataDict['class']
            data[controlClass] += 1
print(f'runtime: {datetime.datetime.now() - start}')
print(data)
# with open('count-data.txt', 'w') as f:
#     f.write(str(data))
