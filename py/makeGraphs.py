import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

import matrixGeneration

# Draws a graph described by Laplacian matrix "mat" with unlabeled nodes.
def visualize_graph(id):
    matrix = matrixGeneration.getLaplacianFromId(id)
    dim = np.shape(matrix)[0]
    g = nx.Graph()
    for i in range(dim):
        for j in range(dim):
            if matrix[i][j] == -1:
                g.add_edge(i,j)
    nx.draw(g)
    plt.savefig(f'graphs/dim8/{id}.png')
    plt.close()

filepath = 'data.txt'
with open(filepath) as f:
    data = eval(f.read())

for id in data:
    visualize_graph(id)
