import { transpose, sum, changeMatrixParity, printMatrix } from './matrixMath.js'

// random matrix generation

// generate random Laplacian matrix
export function generateLaplacianMatrix(n) {
    const adjacencyMatrix = generateAdjacencyMatrix(n);
    for (let i = 0; i < n; i++) {
        const rowSum = adjacencyMatrix[i].reduce((sum, x) => sum + x);
        adjacencyMatrix[i][i] = -rowSum;
    };

    return changeMatrixParity([...adjacencyMatrix]);
}

// generate random adjacency matrix
export function generateAdjacencyMatrix(dim) {
    if (dim < 3) {
        console.log('Error: n < 3 for matrix dimension n.');
        return;
    };

    const result = [];
    for (let i = 0; i < dim; i++) {
        const row = [];
        for (let  j = 0; j < dim; j++) {
            row.push(generateRandomElement(i, j));
        };
        result.push(row);
    };

    const resultTranspose = transpose(result);

    return sum(result, resultTranspose);
}

// for i, j indexing a matrices rows and columns, returns 0 for elements on or below diagonal and either 1 or 0 at random for elements above the diagonal
export function generateRandomElement(i, j) {
    if (j <= i) {
        return 0;
    } else {
        return Math.round(Math.random());
    };
}



