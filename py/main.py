import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

import matrixGeneration
import matrixMath


# Draws a graph described by Laplacian matrix "mat" with unlabeled nodes.
def visualize_graph(matrix):
    dim = np.shape(matrix)[0]
    g = nx.Graph()
    for i in range(dim):
        for j in range(dim):
            if matrix[i][j] == -1:
                g.add_edge(i,j)
    nx.draw(g)
    plt.savefig('graph.png')


id = '082133405'
matrix = matrixGeneration.getLaplacianFromId(id)
# matrix = [
#     [2,-1,-1,0,0,0,0,0],
#     [-1,2,-1,0,0,0,0,0],
#     [-1,-1,4,-1,-1,0,0,0],
#     [0,0,-1,2,0,-1,0,0],
#     [0,0,-1,0,2,-1,0,0],
#     [0,0,0,-1,-1,4,-1,-1],
#     [0,0,0,0,0,-1,1,0],
#     [0,0,0,0,0,-1,0,1]
# ]
# matrix = matrixGeneration.generateLaplacianMatrix(4)
[evals, evecs] = matrixMath.getEigenState(matrix)
matrixMath.printMatrix(matrix)
# print(evals)
# print(evals.size)
# print(np.unique(evals).size)
# print(evecs)
print(matrixMath.pbhTest(matrix, evals, evecs))
visualize_graph(matrix)
