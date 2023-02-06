import numpy as np
import datetime

path = '/home/kyle/code/laplacian-leader-follower-dynamics/data/laplacian8-20230201-075334.txt'


start = datetime.datetime.now()
with open(path, 'r') as f:
    data = np.array(f.read())
print(f'runtime: {datetime.datetime.now() - start}')