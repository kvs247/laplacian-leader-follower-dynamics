import os
string = 'data/laplacian7-20230206-102507/laplacian7-3.txt'

x = int(os.path.basename(string).split('.')[0].split('-')[1])

print(x)