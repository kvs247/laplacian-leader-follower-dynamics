import * as randomMatrix from '../randomMatrix.js'

import * as matrixMath from '../matrixMath.js'

console.log('');

generateLaplacianMatrixTest();
generateAdjacencyMatrixTest();
generateRandomElementTest();

console.log('all tests passed');
console.log('');

// generateLaplacianMatrix
function generateLaplacianMatrixTest() {
    const dim = 9;
    for (let i = 0; i < 100; i++) {
        const mat = randomMatrix.generateLaplacianMatrix(dim);
        const matTranspose = matrixMath.transpose(mat);
        // check that the sum of 1s in the ith row and column are both zero
        for (let i = 0; i < dim; i++) {
            const rowSum = mat[i].reduce((acc, ele) => acc += ele, 0);
            const columnSum = matTranspose[i].reduce((acc, ele) => acc += ele, 0);
            if (!(rowSum == 0 && columnSum == 0)) {
                throw new Error('generateAdjacencyMatrix did not pass - not symmetric');
            };
        };
    };
    console.log('generateLaplacianMatrix passed');
    console.log('');
};

// generateAdjacencyMatrix
function generateAdjacencyMatrixTest() {
    const dim = 9;
    for (let i = 0; i < 100; i++) {
        const mat = randomMatrix.generateAdjacencyMatrix(dim);
        const matTranspose = matrixMath.transpose(mat);
        // check that the sum of 1s in the ith row and column are equal
        for (let i = 0; i < dim; i++) {
            const rowSum = mat[i].reduce((acc, ele) => acc += ele, 0);
            const columnSum = matTranspose[i].reduce((acc, ele) => acc += ele, 0);
            if (rowSum !== columnSum) {
                throw new Error('generateAdjacencyMatrix did not pass - not symmetric');
            };
        };
    };
    console.log('generateAdjacencyMatrix passed');
    console.log('');
};


// generateRandomElement
// 1st check that values on the diagonal and below it are 0
function generateRandomElementTest() {
    for (let i = 3; i <= 5; i++) {
        for (let j = i; j >= 1; j--) {
            const testValue = randomMatrix.generateRandomElement(i, j);
            if (testValue !== 0) {
                console.log('i: ', i, 'j :', j, 'value: ', testValue);
                throw new Error('generateRandomElementTest did not pass - nonzero element on or below diagonal');
            };
        };
    };
    // 2nd check that values above the diagonal and are either 0 or 1
    for (let i = 3; i <= 5; i++) {
        for (let j = i + 1; j <= 5; j++) {
            const testValue = randomMatrix.generateRandomElement(i, j);
            if (!(testValue == 0 || testValue == 1)) {
                console.log('i: ', i, 'j :', j, 'value: ', testValue);
                throw new Error('generateRandomElementTest did not pass - element above diagonal that is not 0 nor 1');
            };
        };
    };
    console.log('generateRandomElement passed');
    console.log('');
};


