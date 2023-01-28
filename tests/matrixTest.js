import * as matrix from '../matrix.js'

console.log('');

generateRandomElementTest();
transposeTest();
sumTest();
generateAdjacencyMatrixTest();

// generateAdjacencyMatrix
function generateAdjacencyMatrixTest() {
    const dim = 9;
    for (let i = 0; i < 100; i++) {
        const mat = matrix.generateAdjacencyMatrix(dim);
        const matTranspose = matrix.transpose(mat);
        // check that the sum of 1s in the ith row and column are equal
        for (let i = 0; i < dim; i++) {
            const rowSum = mat[i].reduce((acc, ele) => acc += ele, 0);
            const columnSum = matTranspose[i].reduce((acc, ele) => acc += ele, 0);
            if (rowSum !== columnSum) {
                throw new Error('generateAdjacencyMatrix did not pass - not symmetric');
            };
        };
    };
    console.log('generateAdacencyMatrix passed');
    console.log('');
};


// generateRandomElement
// 1st check that values on the diagonal and below it are 0
function generateRandomElementTest() {
    for (let i = 3; i <= 5; i++) {
        for (let j = i; j >= 1; j--) {
            const testValue = matrix.generateRandomElement(i, j);
            if (testValue !== 0) {
                console.log('i: ', i, 'j :', j, 'value: ', testValue);
                throw new Error('generateRandomElementTest did not pass - nonzero element on or below diagonal');
            };
        };
    };
    // 2nd check that values above the diagonal and are either 0 or 1
    for (let i = 3; i <= 5; i++) {
        for (let j = i + 1; j <= 5; j++) {
            const testValue = matrix.generateRandomElement(i, j);
            if (!(testValue == 0 || testValue == 1)) {
                console.log('i: ', i, 'j :', j, 'value: ', testValue);
                throw new Error('generateRandomElementTest did not pass - element above diagonal that is not 0 nor 1');
            };
        };
    };
    console.log('generateRandomElement passed');
    console.log('');
};


// transpose
function transposeTest() {
    const testMatrix = [
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
    if (matrix.transpose(testMatrix).toString() !== expectedResult.toString()) { 
        console.log(matrix.transpose(testMatrix));
        throw new Error('transpose did not pass');
    };
    console.log('transpose passed');
    console.log('');
};

// sum
function sumTest() {
    const testMatrix1 = [
        [1, -1, 1],
        [2, 4, -1],
        [0, 1, 0]
    ];
    const testMatrix2 = [
        [0, 0, 0],
        [-2, 4, 2],
        [1, 5, -3]
    ];
    const expectedResult = [
        [1, -1, 1],
        [0, 8, 1],
        [1, 6, -3]
    ];
    if (matrix.sum(testMatrix1, testMatrix2).toString() !== expectedResult.toString()) {
        console.log(matrix.sum(testMatrix1, testMatrix2));
        throw new Error('sum did not pass');
    };
    console.log('sum passed');
    console.log('');
};