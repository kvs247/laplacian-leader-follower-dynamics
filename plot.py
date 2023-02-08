import matplotlib.pyplot as plt

filepath = 'data/v2/counts.txt'
with open(filepath) as f:
    data = eval(f.read())

x = list(map(int, data.keys()))
yEC = x.copy()
yCC = x.copy()
yCU = x.copy()
yCUDIS = x.copy()
yCUDEGEN = x.copy()
yCUNONDEGEN = x.copy()

for index, (key, value) in enumerate(data.items()):
    # print(index, key, value)
    dim = int(key)
    numMatrices = 2 ** (dim / 2 * (dim - 1))
    ####
    if dim == 8:
        numMatrices = 81000000
    yEC[index] = value['EC'] / numMatrices
    yCC[index] = value['CC'] / numMatrices
    numCUMatrices = value['CU-dis'] + value['CU-degen'] + value['CU-nondegen']
    yCU[index] = numCUMatrices / numMatrices

    yCUDIS[index] = value['CU-dis'] / numCUMatrices
    yCUDEGEN[index] = value['CU-degen'] / numCUMatrices
    yCUNONDEGEN[index] = value['CU-nondegen'] / numCUMatrices

plt.plot(x, yEC, label='ec', color='green')
plt.plot(x, yCC, label='cc', color='blue')
plt.plot(x, yCU, label='cu', color='purple')
plt.legend()
plt.savefig('fig.png')
plt.show()

plt.close()

plt.plot(x, yCUDIS, label='cu-dis', color='blue')
plt.plot(x, yCUDEGEN, label='cu-degen', color='purple')
plt.plot(x, yCUNONDEGEN, label='cu-nondegen', color='red')
plt.legend()
plt.savefig('fig2.png')