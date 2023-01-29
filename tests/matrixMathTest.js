import * as matrixMath from '../matrixMath.js';
import { sqrt } from 'mathjs';

transposeTest();
sumTest();
changeMatrixParityTest();
getControlSetTest();
zeroFloatCorrectionTest();
getEigenStateTest();

console.log('all tests passed');
console.log('');

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

// getControlSet
function getControlSetTest() {
    const inputDim = 3;
    const expectedResult = [
        [ 0, 0, 1 ],
        [ 0, 1, 0 ],
        [ 0, 1, 1 ],
        [ 1, 0, 0 ],
        [ 1, 0, 1 ],
        [ 1, 1, 0 ]
      ];
    if (matrixMath.getControlSet(inputDim).toString() !== expectedResult.toString()) {
        console.log(matrixMath.getControlSet(inputDim));
        throw new Error('getAllBinaryVectors did not pass');
    };
    console.log('getControlSet passed');
    console.log('');
}

// NEED TO MAKE TEST FOR EIGENSTATES
// getEigenState
// function getEigenStateTest() {
//     const rootTwo = sqrt(2);
//     const inputMatrix = [
//         [1, 0, 1],
//         [0, 1, 0],
//         [1, 0, 1]
//     ];
//     const expectedResult = [
//         [0, [rootTwo, 0, -rootTwo]],
//         [1, [0, 1, 0]],
//         [2, [rootTwo, 0, rootTwo]]
//     ];
//     if (matrixMath.getEigenState(inputMatrix).toString() !== expectedResult.toString()) {
//         throw new Error('getEigenStateTest')
//         console.log(matrixMath.getEigenState(inputMatrix));
//     };
//     console.log('getEigenState passed');
//     console.log('');
// }

// zeroFloatCorrection
function zeroFloatCorrectionTest() {
    if (matrixMath.zeroFloatCorrection(1e2) !== 1e2) {
        throw new Error('zeroFloatCorrection did not pass');
    };
    if (matrixMath.zeroFloatCorrection(1e0) !== 1e0) {
        throw new Error('zeroFloatCorrection did not pass');
    };
    if (matrixMath.zeroFloatCorrection(1e-2) !== 1e-2) {
        throw new Error('zeroFloatCorrection did not pass');
    };
    if (matrixMath.zeroFloatCorrection(1e-5) !== 1e-5) {
        throw new Error('zeroFloatCorrection did not pass');
    };
    if (matrixMath.zeroFloatCorrection(1e-9) !== 1e-9) {
        throw new Error('zeroFloatCorrection did not pass');
    };
    if (matrixMath.zeroFloatCorrection(1e-11) !== 0) {
        throw new Error('zeroFloatCorrection did not pass');
    };
    if (matrixMath.zeroFloatCorrection(1e-15) !== 0) {
        throw new Error('zeroFloatCorrection did not pass');
    };
    console.log('zeroFloatCorrection passed');
    console.log('');
}