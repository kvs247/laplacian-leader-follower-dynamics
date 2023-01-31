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


# id = '07180207'
# matrix = matrixGeneration.getLaplacianFromId(id)
# [evals, evecs] = matrixMath.getEigenState(matrix)
# matrixMath.printMatrix(matrix)
# # print(evals)
# # print(evals.size)
# # print(np.unique(evals).size)
# # print(evecs)
# print(matrixMath.pbhTest(matrix, evals, evecs))
# # visualize_graph(matrix)
