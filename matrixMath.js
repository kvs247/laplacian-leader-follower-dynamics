import * as math from 'mathjs';

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

export function printMatrix(matrix) {
    console.log('');
    for (let i = 0; i < matrix.length; i++) {
        let row = '|';
        for (let j = 0; j < matrix.length; j++) {
            const value = matrix[i][j];
            if (value < 0) {
                row += ` ${value}`; // one space
            } else {
                row += `  ${value}`; // two spaces
            };
        };
        row += ' |';
        console.log(row);
    };
    console.log('');
}

// get 2D array containing all binary vectors for the given dimension as an array
// NOTE: this does not include the zero vector or all 1s vector
export function getControlSet(n) {
    let binaryString = '';
    for (let i = 1; i < Math.pow(2, n)-1; i++) {
        binaryString += i.toString(2).padStart(n, '0');
    };

    const binaryArray = binaryString.split('').map(Number);
    const controlSet = [];
    while (binaryArray.length) { controlSet.push(binaryArray.splice(0, n)) };

    return controlSet;
}

// calculate eigenstate of given matrix
export function getEigenState(matrix) {
    const result = [];
    const eigenVectors = []; 
    const eigenState = math.eigs(matrix);
    const eigenValues = eigenState.values.map(zeroFloatCorrection);
    const vectors = eigenState.vectors;
    for (let i = 0; i < vectors.length; i++) {
        eigenVectors.push(math.column(vectors, i).flat().map(zeroFloatCorrection));
    };

    for (let i = 0; i < eigenValues.length; i++) {
        result.push([eigenValues[i], eigenVectors[i]]);
    };

    return result;
}

// returns zero for values with size (abs) less than 1e-10
// this is necessary since zero-sum float errors will cause PBH test to fail
export function zeroFloatCorrection(x) {
    if (math.abs(x) < 1e-10) {
        return 0;
    } else {
        return x;
    };
}
