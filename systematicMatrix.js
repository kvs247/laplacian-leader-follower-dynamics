// systematic matrix generation
import * as matrixMath from './matrixMath.js';

let x = getAllLaplacianMatrices(4);
x.forEach(matrixMath.printMatrix);

// get array of all Laplacian matrices for dimension > 2
export function getAllLaplacianMatrices(dim) {
    const result = [];
    const numElementsAboveDiag = (dim / 2) * (dim - 1); // explanation somewhere
    const allBinaryVectors = getAllBinaryVectors(numElementsAboveDiag);
    for (let elements of allBinaryVectors) {
        const tempMatrix = [];
        // this loop iterates over every row of the temporary matrix
        for (let zerosThisRow = 1; zerosThisRow <= dim; zerosThisRow++) {
            const row = elements.slice(0, dim - zerosThisRow).padStart(dim, '0').split('').map(Number);
            tempMatrix.push(row);
            elements = elements.slice(dim - zerosThisRow);
        }; 
        const tempMatrixTranspose = matrixMath.transpose(tempMatrix);
        const newLaplacianMatrix = matrixMath.sum(tempMatrix, tempMatrixTranspose);
        for (let i = 0; i < dim; i++) {
            const rowSum = newLaplacianMatrix[i].reduce((sum, x) => sum + x);
            newLaplacianMatrix[i][i] = -rowSum;
        };
        result.push(newLaplacianMatrix);
    };
    return result;
}

// get array containing all binary vectors for the given dimension as a string
// NOTE: this does not include the zero vector or all 1s vector
export function getAllBinaryVectors(dim) {
    const result = [];
    for (let i = 1; i < (2 ** dim) - 1; i++) {
        result.push(i.toString(2).padStart(dim, '0'));
    };
    return result;
}