// matrix generation

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

// matrix functions

// returns nested array of transpose of input matrix
export function transpose(matrix) {
    return matrix[0].map((_, colIndex) => matrix.map(row => row[colIndex]));
}

// adds two matrices together
export function sum(matrix1, matrix2) {
    const n = matrix1.length;
    if (n != matrix2.length) {
        console.log('Error: trying to add two matrices of unequal dimension');
        return;
    };

    const result = [...matrix1];
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            result[i][j] = matrix1[i][j] + matrix2[i][j]; 
        };
    };

    return result;
}

// changes parity of matrix
export function changeMatrixParity(matrix) {
    const result = [];
    for (let i = 0; i < matrix.length; i++) {
        const row = matrix[i].map(x => -x);
        result.push(row);
    }

    return result;
}