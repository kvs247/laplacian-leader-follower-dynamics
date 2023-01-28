import * as matrixMath from '../matrixMath.js';

transposeTest();
sumTest();
changeMatrixParityTest();

// transpose
function transposeTest() {
    const inputMatrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12]
    ];
    const expectedResult = [
        [1, 4, 7, 10],
        [2, 5, 8, 11],
        [3, 6, 9, 12]
    ];
    if (matrixMath.transpose(inputMatrix).toString() !== expectedResult.toString()) { 
        console.log(matrixMath.transpose(inputMatrix));
        throw new Error('transpose did not pass');
    };
    console.log('transpose passed');
    console.log('');
};

// sum
function sumTest() {
    const inputMatrix1 = [
        [1, -1, 1],
        [2, 4, -1],
        [0, 1, 0]
    ];
    const inputMatrix2 = [
        [0, 0, 0],
        [-2, 4, 2],
        [1, 5, -3]
    ];
    const expectedResult = [
        [1, -1, 1],
        [0, 8, 1],
        [1, 6, -3]
    ];
    if (matrixMath.sum(inputMatrix1, inputMatrix2).toString() !== expectedResult.toString()) {
        console.log(matrixMath.sum(inputMatrix1, inputMatrix2));
        throw new Error('sum did not pass');
    };
    console.log('sum passed');
    console.log('');
}

// changeMatrixParity
function changeMatrixParityTest() {
    const inputMatrix = [
        [1, -1, 1],
        [2, 4, -1],
        [0, 1, 0]
    ];
    const expectedResult = [
        [-1, 1, -1],
        [-2, -4, 1],
        [0, -1, 0]
    ];
    if (matrixMath.changeMatrixParity(inputMatrix).toString() !== expectedResult.toString()) {
        console.log(matrixMath.changeMatrixParity(inputMatrix));
        throw new Error('changeMatrixParity did not pass');
    };
    console.log('changeMatirxParity passed');
    console.log('');
}