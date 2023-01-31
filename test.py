path = '/home/kyle/code/laplacian-leader-follower-dynamics/data/laplacian3-20230131083052.txt'

with open(path) as f:
    data = f.read()

data = np.array(eval(data))
print(type(data))