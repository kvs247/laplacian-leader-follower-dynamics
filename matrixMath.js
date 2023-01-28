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